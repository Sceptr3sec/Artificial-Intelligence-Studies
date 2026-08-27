import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

np.random.seed(42)

num_samples = 1000

file_sizes = np.random.randint(1, 1001, num_samples)
compilation_times = np.random.normal(0.5 * file_sizes, 50, num_samples)
import_counts = np.random.randint(0, 21, num_samples)
entropy_values = np.random.uniform(0, 8, num_samples)
section_counts = np.random.randint(1, 11, num_samples)

X = pd.DataFrame({
    "file_size": file_sizes,
    "compilation_time": compilation_times,
    "import_count": import_counts,
    "entropy": entropy_values,
    "section_count": section_counts
})

risk_score = (
    0.1 * file_sizes
    + 0.5 * compilation_times
    + 2 * import_counts
    + 3 * entropy_values
    + 5 * section_counts
    + np.random.normal(0, 10, num_samples)
)

y = (risk_score >= 239).astype(int)

print(X.head())

print("\nRisk Score Statistics:")
print("Minimum:", risk_score.min())
print("Maximum:", risk_score.max())
print("Mean:", risk_score.mean())
print("Median:", np.median(risk_score))

print("First 20 labels:", y[:20])
print("Benign:", np.sum(y == 0))
print("Malware:", np.sum(y == 1))

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression()

model.fit(X_train, y_train)

print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)

y_pred = model.predict(X_test)

print("Predictions:", y_pred[:20])
print("Actual:     ", y_test[:20])

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("\n--- Model Evaluation ---")
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1:", f1)

print("\nConfusion Matrix:")
print(cm)

probabilities = model.predict_proba(X_test)[:, 1]

print("\nFirst 5 predicted probabilities:", probabilities[:5])

malware_probabilities = model.predict_proba(X_test)[:, 1]

for i, probability in enumerate(malware_probabilities):
    if y_test[i] == 1 and 0.5 <= probability <= 0.8:
        print(
            "Index:", i,
            "| Probability:", probability,
            "| Actual:", y_test[i]
        )

target = X_test.iloc[161].copy()

print("\n--- Attack Target ---")
print(target)

original_probability = model.predict_proba(
    target.to_frame().T
)[0, 1]

original_prediction = model.predict(
    target.to_frame().T
)[0]

print("\nActual Label:", y_test[161])
print("Original Probability:", original_probability)
print("Original Prediction:", original_prediction)

#Model Interrogation#

print("\n--- Model Coefficients ---")

for feature, coefficient in zip(
    X.columns,
    model.coef_[0]
):
    print(feature, ":", coefficient)

attack = target.copy()
current_entropy = target["entropy"]

while current_entropy > 0:
    attack["entropy"] = current_entropy

    attack_df = attack.to_frame().T

    attack_probability = model.predict_proba(
        attack_df
    )[0, 1]

    attack_prediction = model.predict(
        attack_df
    )[0]

    if attack_prediction == 0:
        print("\nEvasion successful!")
        print("Original entropy:", target["entropy"])
        print("Boundary entropy:", current_entropy)
        print("Malware probability:", attack_probability)
        print(
            "Entropy reduction:",
            target["entropy"] - current_entropy
        )
        break

    current_entropy -= 0.01