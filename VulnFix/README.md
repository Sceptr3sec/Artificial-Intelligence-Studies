# VulnFix

VulnFix is a small machine-learning security project that predicts vulnerability remediation time with linear regression, then red-teams the trained model for unsafe out-of-distribution behavior.

The project was built to demonstrate the full path from first-principles regression through model evaluation and adversarial testing rather than treating `LinearRegression().fit()` as a black box.

## What it demonstrates

- Simple linear regression implemented from the underlying slope/intercept calculations
- Ordinary Least Squares intuition through residuals and Residual Sum of Squares (RSS)
- Train/test splitting and held-out evaluation
- Multiple linear regression using five vulnerability features
- MAE, RMSE, and R² evaluation
- Residual analysis
- Model serialization with Joblib
- AI/ML red-team testing for invalid and out-of-distribution inputs
- Input validation as a mitigation for unsafe model extrapolation

## Features

The multiple-regression model uses:

| Feature | Description |
| --- | --- |
| `cvss_score` | CVSS severity score |
| `affected_systems` | Number of affected systems |
| `vuln_age_days` | Vulnerability age in days |
| `exploit_available` | Public exploit indicator (`0` or `1`) |
| `internet_facing` | Internet exposure indicator (`0` or `1`) |

The target is `remediation_days`.

## Model results

On a held-out test split, the five-feature model produced:

- **MAE:** 2.522 days
- **RMSE:** 3.005 days
- **R²:** 0.802

The learned coefficients closely recovered the hidden synthetic relationship used to generate the dataset:

| Parameter | Learned value |
| --- | ---: |
| Intercept | 35.998 |
| CVSS score | -1.527 |
| Affected systems | +0.0087 |
| Vulnerability age | +0.0192 |
| Exploit available | -4.181 |
| Internet facing | -2.957 |

## Red-team finding

The raw model accepts numeric inputs far outside the domain it was trained on. A deliberately malformed input produced a prediction on the order of:

```text
-2.957e+93 days
```

This is mathematically valid extrapolation but operationally meaningless. The finding illustrates an important ML-security lesson: the model does not understand CVSS ranges, binary fields, or business constraints unless the surrounding application enforces them.

`src/red_team.py` demonstrates both the vulnerable raw-model behavior and a validation layer that rejects malformed feature values before inference.

## Project structure

```text
VulnFix/
├── .gitignore
├── README.md
├── requirements.txt
├── models/
│   └── vulnfix_linear_regression.pkl
└── src/
    ├── generate.py
    ├── train.py
    ├── multiple_regression.py
    └── red_team.py
```

## Setup

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

First-principles simple regression:

```bash
python src/generate.py
```

Scikit-learn simple regression:

```bash
python src/train.py
```

Train and save the multiple-regression model:

```bash
python src/multiple_regression.py
```

Run the adversarial test and validation demo:

```bash
python src/red_team.py
```

## Security takeaway

Model robustness is a system property, not just a model property. Production ML applications should enforce feature types and ranges, reject malformed or out-of-distribution inputs where appropriate, and apply output sanity checks before predictions influence operational decisions.

## Disclaimer

The dataset in this project is synthetic and the model is educational. VulnFix is not intended to make real vulnerability-remediation decisions.
