"""Generates sales_data.csv: a small, illustrative sales log for a fictional
coffee shop chain, used only as the domain the DataDesk agent reasons over
(not for statistical modeling). Deterministic (fixed seed) so the dataset
is reproducible.
"""
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)

products = {
    "Espresso": ("Beverage", 3.25),
    "Latte": ("Beverage", 4.50),
    "Cold Brew": ("Beverage", 4.00),
    "Croissant": ("Bakery", 3.75),
    "Muffin": ("Bakery", 3.25),
    "Bagel": ("Bakery", 2.95),
}
regions = ["Downtown", "Uptown", "Suburban"]

dates = pd.date_range("2025-01-01", "2025-06-30", freq="D")

rows = []
for date in dates:
    n_orders = rng.integers(15, 30)
    for _ in range(n_orders):
        product = rng.choice(list(products.keys()))
        category, unit_price = products[product]
        quantity = int(rng.integers(1, 4))
        region = rng.choice(regions)
        total_sales = round(quantity * unit_price, 2)
        rows.append({
            "date": date.strftime("%Y-%m-%d"),
            "month": date.strftime("%B"),
            "product": product,
            "category": category,
            "region": region,
            "quantity": quantity,
            "unit_price": unit_price,
            "total_sales": total_sales,
        })

df = pd.DataFrame(rows)
df.to_csv("sales_data.csv", index=False)
print(f"Wrote {len(df)} rows to sales_data.csv")
