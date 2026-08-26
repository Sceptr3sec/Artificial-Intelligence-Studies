import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

np.random.seed(42)

num_samples = 500

cvss_score = np.random.uniform(
    1.0, 10.0, num_samples
)

affected_systems = np.random.randint(
    1, 501, num_samples
)

vuln_age_days = np.random.randint(
    1, 366, num_samples
)

exploit_available = np.random.randint(
    0, 2, num_samples
)

internet_facing = np.random.randint(
    0, 2, num_samples
)

noise = np.random.normal(
    0, 3, num_samples
)

remediation_days = (
    35
    - (1.5 * cvss_score)
    + (0.01 * affected_systems)
    + (0.02 * vuln_age_days)
    - (4 * exploit_available)
    - (3 * internet_facing)
    + noise
)

data = pd.DataFrame({
    "cvss_score": cvss_score,
    "affected_systems": affected_systems,
    "vuln_age_days": vuln_age_days,
    "exploit_available": exploit_available,
    "internet_facing": internet_facing,
    "remediation_days": remediation_days
})

print(data.head())

X = data[
    [
        "cvss_score",
        "affected_systems",
        "vuln_age_days",
        "exploit_available",
        "internet_facing"
    ]
]

y = data["remediation_days"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nLearned Intercept:")
print(model.intercept_)

print("\nLearned Coefficients:")

for feature, coefficient in zip(
    X.columns,
    model.coef_
):
    print(feature, ":", coefficient)

mae = mean_absolute_error(y_test, y_pred)

rmse = np.sqrt(
    mean_squared_error(y_test, y_pred)
)

r2 = r2_score(y_test, y_pred)

print("\n--- Model Evaluation ---")
print("MAE:", mae)
print("RMSE:", rmse)
print("R²:", r2)

residuals = y_test - y_pred

plt.scatter(y_pred, residuals)

plt.axhline(
    y=0,
    linestyle="--"
)

plt.xlabel("Predicted Remediation Days")
plt.ylabel("Residual")
plt.title("Residual Analysis")

plt.show()

joblib.dump(
    model,
    "models/vulnfix_linear_regression.pkl"
)