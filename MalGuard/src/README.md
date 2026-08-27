MalGuard

MalGuard is a small adversarial machine learning lab that demonstrates the lifecycle of a binary malware classifier: synthetic feature generation, logistic regression training, model evaluation, feature analysis, and a targeted evasion attack.

The project was built as a hands-on introduction to classification and adversarial ML concepts relevant to AI security and red teaming.

Project Goal

MalGuard predicts whether a file is:

0 — Benign

1 — Malware

The classifier uses five synthetic PE-style features:

file_size

compilation_time

import_count

entropy

section_count

The dataset contains 1,000 synthetic samples with a balanced 50/50 benign-malware split.

Model

MalGuard uses scikit-learn's LogisticRegression.

The project covers binary classification, train/test splitting, sigmoid intuition, decision thresholds, confusion matrices, accuracy, precision, recall, F1 score, feature coefficients, prediction probabilities, and adversarial evasion.

Baseline Results

On the held-out test set, the model produced:

[[102   4]
 [  3  91]]

This corresponds to:

True Negatives: 102

False Positives: 4

False Negatives: 3

True Positives: 91

Accuracy: 96.5%

Precision: ~95.8%

Recall: ~96.8%

False negatives are particularly important from a security perspective because they represent malicious samples classified as benign.

Learned Feature Influence

The trained logistic regression model learned:

file_size         : 0.02118175520119904
compilation_time  : 0.12072370972868522
import_count      : 0.43893351770747124
entropy           : 0.7466023827062278
section_count     : 1.1615439591100332

All coefficients were positive, meaning increasing those features pushed the model toward the malware class.

These coefficients were then used to guide adversarial testing rather than randomly modifying inputs.

Targeted Evasion Attack

A correctly detected malware sample was selected:

file_size          369.000000
compilation_time   299.047129
import_count        14.000000
entropy              4.168586
section_count        3.000000

Original result:

Actual Label:        Malware
Predicted Label:     Malware
Malware Probability: 0.700777

Entropy was selected as the attack feature because its positive coefficient meant reducing entropy should move the prediction toward the benign class.

An iterative search reduced entropy while keeping every other feature unchanged.

Successful evasion:

Original entropy:             4.168585524067103
Boundary entropy:             3.028585524067127
Entropy reduction:            1.14

Original malware probability: 0.700777
Modified malware probability: 0.499969

Original prediction:          Malware
Modified prediction:          Benign

The attack successfully converted a true positive into a false negative by changing a single feature.

Security Finding

Feature-Space Evasion via Entropy Manipulation

Observation: The classifier relied strongly enough on entropy that reducing the feature by approximately 1.14 moved a malicious sample across the decision boundary.

Impact: An attacker capable of influencing features consumed by the classifier may be able to reduce the malware probability sufficiently to cause a false-negative classification.

Result:

Malware → Benign
70.08%  → 49.997%

This demonstrates how feature dependence and decision thresholds can create an adversarial attack surface.

Limitations

This project uses synthetic data and performs a feature-space attack.

It does not prove that a real PE file can always be modified to produce the same entropy change while preserving malicious functionality.

Future extensions could include:

Training on real PE metadata or EMBER-style features

Performing realizable PE transformations

Testing transferability across multiple classifiers

Adding adversarial training

Comparing decision thresholds

Adding feature validation and distribution monitoring

Run

Create a virtual environment:

python -m venv .venv

Install dependencies:

pip install -r requirements.txt

Run the project scripts from the repository root.

Portfolio Summary

Synthetic PE Features
        ↓
Logistic Regression
        ↓
Probability
        ↓
Decision Threshold
        ↓
Benign / Malware
        ↓
Model Inspection
        ↓
Targeted Feature Manipulation
        ↓
Decision-Boundary Evasion
        ↓
False Negative

MalGuard is intentionally small. The focus is on understanding a model well enough to attack it, not simply training a classifier.