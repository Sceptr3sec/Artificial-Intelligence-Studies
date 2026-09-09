from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from typing import Dict, List, Optional

# RAGAS imports
try:
    from ragas import SingleTurnSample, EvaluationDataset
    from ragas.metrics import BleuScore, ResponseRelevancy, Faithfulness, RougeScore
    from ragas import evaluate
    RAGAS_AVAILABLE = True
except ImportError:
    RAGAS_AVAILABLE = False


def evaluate_response_quality(question: str, answer: str, contexts: List[str],
                               reference: Optional[str] = None) -> Dict[str, float]:
    """Evaluate response quality using RAGAS metrics.

    Always computes:
        - Faithfulness: does the answer stick to what's in the retrieved context?
        - Response Relevancy: does the answer actually address the question?

    Additionally, when a `reference` (ground-truth) answer is supplied, also computes:
        - BleuScore / RougeScore: lexical overlap between the answer and the reference.
    These reference-based metrics are optional because they require a labeled
    ground-truth answer, which isn't available for live, ad hoc chat questions,
    but they can be used for a curated evaluation_dataset.txt (see evaluate_dataset.py).
    (Note: ragas' NonLLMContextPrecisionWithReference metric was considered too,
    but it scores retrieved context against a *reference context*, not a reference
    *answer* — a different kind of label we don't collect here.)

    Args:
        question: the user's question.
        answer: the model's generated answer.
        contexts: the retrieved context chunks used to generate the answer.
        reference: optional ground-truth answer, enabling reference-based metrics.

    Returns:
        Dict mapping metric name -> score, or {"error": "..."} on bad input/failure.
    """
    if not RAGAS_AVAILABLE:
        return {"error": "RAGAS not available"}

    # Handle empty/malformed inputs with a clear error message instead of crashing
    if not question or not isinstance(question, str):
        return {"error": "A non-empty 'question' string is required"}
    if not answer or not isinstance(answer, str):
        return {"error": "A non-empty 'answer' string is required"}
    if contexts is None:
        contexts = []
    contexts = [c for c in contexts if isinstance(c, str) and c.strip()]

    try:
        # Create evaluator LLM
        evaluator_llm = LangchainLLMWrapper(ChatOpenAI(model="gpt-3.5-turbo"))

        # Create evaluator embeddings
        evaluator_embeddings = LangchainEmbeddingsWrapper(
            OpenAIEmbeddings(model="text-embedding-3-small")
        )

        # Core metrics that don't require a ground-truth reference
        metrics = [
            Faithfulness(llm=evaluator_llm),
            ResponseRelevancy(llm=evaluator_llm, embeddings=evaluator_embeddings),
        ]

        sample_kwargs = {
            "user_input": question,
            "response": answer,
            "retrieved_contexts": contexts if contexts else [""],
        }

        # Additional documented metrics when a reference answer is available
        if reference:
            sample_kwargs["reference"] = reference
            metrics.append(BleuScore())
            metrics.append(RougeScore())

        sample = SingleTurnSample(**sample_kwargs)
        dataset = EvaluationDataset(samples=[sample])

        results = evaluate(
            dataset=dataset,
            metrics=metrics,
        )

        # Convert results to a plain dict of metric_name -> score
        results_df = results.to_pandas()
        scores: Dict[str, float] = {}
        for column in results_df.columns:
            if column in ("user_input", "response", "retrieved_contexts", "reference"):
                continue
            value = results_df[column].iloc[0]
            if isinstance(value, (int, float)):
                scores[column] = float(value)

        return scores

    except Exception as e:
        return {"error": str(e)}
