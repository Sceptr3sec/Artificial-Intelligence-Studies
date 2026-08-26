import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

num_samples = 200

cvss_score = np.random.uniform(1.0, 10.0, num_samples)

print(cvss_score[:10])

noise = np.random.normal(0, 3, num_samples)

remediation_days = 30 - (2 * cvss_score) + noise

print("\nCVSS:", cvss_score[:5])
print("Remediation Days:", remediation_days[:5])

# Calculate means
x_mean = np.mean(cvss_score)
y_mean = np.mean(remediation_days)

# Calculate slope
numerator = np.sum(
    (cvss_score - x_mean) * (remediation_days - y_mean)
)

denominator = np.sum(
    (cvss_score - x_mean) ** 2
)

m = numerator / denominator

# Calculate intercept
c = y_mean - (m * x_mean)

print("Intercept:", c)
print("\nSlope (m):", m)
print("\nMean CVSS Score:", x_mean)
print("Mean Remediation Days:", y_mean)


# ----- ONE OBSERVATION -----

actual = remediation_days[0]
x = cvss_score[0]

predicted = (m * x) + c
residual = actual - predicted

print("\nFirst Observation")
print("CVSS:", x)
print("Actual:", actual)
print("Predicted:", predicted)
print("Residual:", residual)


# ----- OUR MODEL ACROSS ALL 200 OBSERVATIONS -----

predictions = (m * cvss_score) + c

residuals = remediation_days - predictions

squared_residuals = residuals ** 2

rss = np.sum(squared_residuals)


# ----- INTENTIONALLY BAD MODEL -----

bad_m = 1
bad_c = 10

bad_predictions = (bad_m * cvss_score) + bad_c
bad_residuals = remediation_days - bad_predictions
bad_rss = np.sum(bad_residuals ** 2)

print("\nOur Model RSS:", rss)
print("Bad Model RSS:", bad_rss)


# ----- PLOT -----

plt.scatter(
    cvss_score,
    remediation_days,
    label="Observed Vulnerabilities"
)

plt.plot(
    cvss_score,
    predictions,
    label="OLS Regression Line"
)

plt.xlabel("CVSS Score")
plt.ylabel("Remediation Days")
plt.title("Vulnerability Remediation Linear Regression")
plt.legend()

plt.show()