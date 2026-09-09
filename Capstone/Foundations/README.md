# Iris Data Workflow

## Project Description
This project builds a data analysis workflow for the classic Iris flower dataset using pandas, NumPy, Matplotlib, and Seaborn. It covers loading the data, cleaning it with reusable functions, running exploratory analysis, and producing visualizations of the relationships between flower measurements and species. Detailed explanations, interpretation, and academic citations are in `module_summary.pdf`.

## What Was Built
- `data_workflow.ipynb` — Jupyter Notebook with the full workflow: data loading, cleaning functions, EDA functions, three visualizations, and a written summary/interpretation.
- `iris.csv` — the dataset used by the notebook.
- `requirements.txt` — dependencies generated with `pip freeze` from a clean virtual environment holding only this project's packages.
- `module_summary.pdf` — written report with academic citations (see this file for detailed explanations, interpretation, and references — not repeated here).

## Dataset
**Iris Plants Dataset** (Fisher's Iris data, 150 samples, 4 features + species label)
Source: [UCI Machine Learning Repository — Iris Data Set](https://archive.ics.uci.edu/dataset/53/iris)

`iris.csv` in this folder is the same data as `bezdekIris.data`, with a header row added (`sepal_length, sepal_width, petal_length, petal_width, species`).

## How to Run the Project

### 1. Install dependencies
```
pip install -r requirements.txt
```

### 2. Open and run the notebook
```
jupyter notebook data_workflow.ipynb
```
Then run all cells in order (Cell → Run All). The notebook expects `iris.csv` to be in the same folder.

To regenerate `requirements.txt` after adding packages:
```
pip freeze > requirements.txt
```

## Reflection Questions

### Bias Awareness
Poor data cleaning could introduce bias in a few concrete ways here. Applying one outlier threshold to the whole dataset rather than within each species could unfairly flag legitimate values in a species that naturally has more spread (for example Virginica), skewing later analysis against that group. Removing "duplicate" rows dataset-wide also assumes identical rows are true duplicates rather than two flowers that happen to share measurements; on a larger or messier dataset that assumption could quietly discard valid data. In this project, outliers are flagged in a new column instead of deleted, and cleaning is done with named, documented functions so every step is visible and reversible rather than being a bias-introducing black box.

### Future Integration Reflections
**Machine learning workflow changes:** To turn this into an ML pipeline, the notebook would need a train/test (or train/validation/test) split done before any statistics are computed on the data, to avoid leaking test information into cleaning or feature decisions. The cleaning and EDA functions here are already reusable, so they would sit at the front of a `scikit-learn` `Pipeline`, followed by encoding the `species` column as a numeric target and scaling the four numeric features.

**Preparing data for a neural network:** A neural network would additionally need the numeric features standardized (zero mean, unit variance) rather than left in raw centimeters, and the species labels one-hot encoded rather than kept as strings. Because the Iris dataset only has 150 rows, it would also need augmentation or a much larger dataset, plus careful batching and a fixed random seed, to train a network without immediately overfitting.

**Agentic automation potential:** An agent could take over the repetitive parts of this workflow — automatically profiling a new CSV, flagging likely outliers and missing-value patterns, choosing which plots best show separation between categories, and drafting the first pass of the summary/interpretation text for a human to review and correct. It could also watch for schema or distribution drift if this workflow were re-run on new data over time, and re-run the notebook automatically when the source file changes.
