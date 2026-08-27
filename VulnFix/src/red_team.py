import numpy as np
import pandas as pd
import joblib

model = joblib.load(
    "models/vulnfix_linear_regression.pkl"
)

new_vulnerability = pd.DataFrame({
    "cvss_score": [-100000],
    "affected_systems": [99999999999999999999999],
    "vuln_age_days": [-0],
    "exploit_available": [0000000000000000000000000000/2],
    "internet_facing": [999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999] 
})

print(model.predict(new_vulnerability))