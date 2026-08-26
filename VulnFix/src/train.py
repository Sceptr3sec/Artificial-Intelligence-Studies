import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

np.random.seed(42)

num_samples = 200

cvss_score = np.random.uniform(1.0, 10.0, num_samples)

noise = np.random.normal(0, 3, num_samples)

remediation_days = 30 - (2 * cvss_score) + noise

X = cvss_score.reshape(-1, 1)
y = remediation_days

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

print("\nLearned Intercept:", model.intercept_)
print("Learned Slope:", model.coef_[0])

y_pred = model.predict(X_test)

print("\nFirst 5 Test Predictions")

for i in range(5):
    print(
        "CVSS:", X_test[i][0],
        "| Actual:", y_test[i],
        "| Predicted:", y_pred[i]
    )

mae = mean_absolute_error(y_test, y_pred)

rmse = np.sqrt(
    mean_squared_error(y_test, y_pred)
)

r2 = r2_score(y_test, y_pred)

print("\n--- Model Evaluation ---")
print("MAE:", mae)
print("RMSE:", rmse)
print("R²:", r2)