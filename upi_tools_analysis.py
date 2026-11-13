from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

DATA_PATH = Path("data/processed/upi_transactions_risk_scored.csv")

def load_data(path=DATA_PATH):
    if Path(path).exists():
        return pd.read_csv(path)
    return pd.DataFrame({
        "transaction_id":["TX001","TX002","TX003","TX004","TX005","TX006"],
        "amount_inr":[250,1200,5000,150,8200,600],
        "transaction_type":["P2P","P2M","P2M","Recharge","Bill Payment","P2P"],
        "transaction_status":["SUCCESS","SUCCESS","FAILED","SUCCESS","SUCCESS","FAILED"],
        "device_type":["Android","iOS","Web","Android","Web","iOS"],
        "fraud_flag":[0,0,1,0,1,0]
    })

if __name__ == "__main__":
    df=load_data()
    print("Shape:",df.shape)
    print("\nMissing values:\n",df.isna().sum())
    print("\nDuplicates:",df.duplicated().sum())
    print("\nSummary by transaction type:\n",
          df.groupby("transaction_type")["amount_inr"].agg(["count","mean","median"]))
    print("\nFlagged rate (%):",round(df["fraud_flag"].mean()*100,3))
    sns.countplot(data=df,x="transaction_type")
    plt.title("Transaction Count by Type")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.show()
