from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data" / "sample_sales_data.csv", parse_dates=["date"])
print("Shape:", df.shape)
print("Missing values:\n", df.isna().sum())
df = df.drop_duplicates().dropna(subset=["order_id", "date", "category", "quantity", "unit_price"])
df = df[(df.quantity > 0) & (df.unit_price >= 0)].copy()
df["sales"] = df.quantity * df.unit_price
summary = df.groupby("category", as_index=False).sales.sum().sort_values("sales", ascending=False)
print(summary)
out = ROOT / "outputs"
out.mkdir(exist_ok=True)
df.to_csv(out / "cleaned_sales_data.csv", index=False)
summary.to_csv(out / "sales_by_category.csv", index=False)
