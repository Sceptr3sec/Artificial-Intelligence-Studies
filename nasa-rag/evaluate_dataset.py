#!/usr/bin/env python3
"""
Batch evaluation of the NASA RAG chat system against evaluation_dataset.txt.

For each question in the dataset, this script:
  1. Retrieves relevant documents from ChromaDB (rag_client)
  2. Formats them into context
  3. Generates an answer with the LLM (llm_client)
  4. Scores the answer with RAGAS (ragas_evaluator)

It prints a per-question breakdown and an aggregate (mean) score per metric,
and writes the full results to evaluation_results.json.

Usage:
    python evaluate_dataset.py \\
        --openai-key YOUR_KEY \\
        --chroma-dir ./chroma_db_openai \\
        --collection-name nasa_space_missions_text \\
        --dataset evaluation_dataset.txt
"""

import argparse
import json
import os
import re
import statistics
from pathlib import Path
from typing import Dict, List

from dotenv import load_dotenv

import rag_client
import llm_client
import ragas_evaluator

load_dotenv()  # loads OPENAI_API_KEY from a local .env file, if present


def parse_dataset(path: str) -> List[Dict[str, str]]:
    """Parse evaluation_dataset.txt into a list of question records.

    Expects blocks separated by blank lines, each containing
    Category / Mission / Question / Expected fields. Lines starting with '#'
    are treated as comments and ignored.
    """
    text = Path(path).read_text(encoding="utf-8")
    blocks = [b for b in re.split(r"\n\s*\n", text) if b.strip()]

    records = []
    for block in blocks:
        record = {}
        for line in block.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if ":" not in line:
                continue
            key, _, value = line.partition(":")
            record[key.strip().lower()] = value.strip()
        if "question" in record:
            records.append(record)
    return records


def run_evaluation(openai_key: str, chroma_dir: str, collection_name: str,
                    dataset_path: str, n_docs: int = 3, model: str = "gpt-3.5-turbo") -> Dict:
    """Run every dataset question through the full RAG pipeline and score it."""

    import os
    os.environ["CHROMA_OPENAI_API_KEY"] = openai_key

    collection = rag_client.initialize_rag_system(chroma_dir, collection_name)
    records = parse_dataset(dataset_path)

    if not records:
        raise ValueError(f"No questions found in {dataset_path}")

    per_question_results = []
    metric_totals: Dict[str, List[float]] = {}

    for i, record in enumerate(records, start=1):
        question = record["question"]
        mission = record.get("mission", "all")

        docs_result = rag_client.retrieve_documents(collection, question, n_docs, mission)

        contexts_list = []
        context = ""
        if docs_result and docs_result.get("documents") and docs_result["documents"][0]:
            contexts_list = docs_result["documents"][0]
            context = rag_client.format_context(contexts_list, docs_result["metadatas"][0])

        answer = llm_client.generate_response(openai_key, question, context, [], model)

        scores = ragas_evaluator.evaluate_response_quality(question, answer, contexts_list)

        result = {
            "index": i,
            "category": record.get("category", "uncategorized"),
            "mission": mission,
            "question": question,
            "answer": answer,
            "num_contexts_retrieved": len(contexts_list),
            "scores": scores,
        }
        per_question_results.append(result)

        print(f"\n[{i}/{len(records)}] ({result['category']}) {question}")
        print(f"  Answer: {answer[:200]}{'...' if len(answer) > 200 else ''}")
        if "error" in scores:
            print(f"  Evaluation error: {scores['error']}")
        else:
            for metric_name, score in scores.items():
                print(f"  {metric_name}: {score:.3f}")
                metric_totals.setdefault(metric_name, []).append(score)

    aggregate = {
        metric: {
            "mean": statistics.mean(values),
            "min": min(values),
            "max": max(values),
            "n": len(values),
        }
        for metric, values in metric_totals.items()
    }

    print("\n" + "=" * 60)
    print("AGGREGATE SCORES")
    print("=" * 60)
    for metric, stats in aggregate.items():
        print(f"{metric}: mean={stats['mean']:.3f}  min={stats['min']:.3f}  max={stats['max']:.3f}  (n={stats['n']})")

    return {"per_question": per_question_results, "aggregate": aggregate}


def main():
    parser = argparse.ArgumentParser(description="Batch-evaluate the NASA RAG chat system")
    parser.add_argument("--openai-key", default=os.environ.get("OPENAI_API_KEY"),
                       help="OpenAI API key (defaults to OPENAI_API_KEY env var / .env file)")
    parser.add_argument("--chroma-dir", default="./chroma_db_openai", help="ChromaDB persist directory")
    parser.add_argument("--collection-name", default="nasa_space_missions_text", help="Collection name")
    parser.add_argument("--dataset", default="evaluation_dataset.txt", help="Path to evaluation dataset")
    parser.add_argument("--n-docs", type=int, default=3, help="Documents to retrieve per question")
    parser.add_argument("--model", default="gpt-3.5-turbo", help="OpenAI chat model")
    parser.add_argument("--output", default="evaluation_results.json", help="Where to save full results")
    args = parser.parse_args()

    if not args.openai_key:
        parser.error("No OpenAI key found. Pass --openai-key, set OPENAI_API_KEY, or add it to a .env file.")

    results = run_evaluation(
        openai_key=args.openai_key,
        chroma_dir=args.chroma_dir,
        collection_name=args.collection_name,
        dataset_path=args.dataset,
        n_docs=args.n_docs,
        model=args.model,
    )

    Path(args.output).write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"\nFull results written to {args.output}")


if __name__ == "__main__":
    main()
