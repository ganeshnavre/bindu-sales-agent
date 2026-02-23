import pandas as pd
from typing import Dict, Any


class SalesInsightAgent:
    """
    Sales Insight Agent

    A structured data-processing agent that analyzes
    sales CSV data and generates business insights.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None

    def load_data(self) -> None:
        """Load CSV data into a DataFrame."""
        self.df = pd.read_csv(self.file_path)

    def total_revenue(self) -> float:
        """Calculate total revenue."""
        return float(self.df["revenue"].sum())

    def top_products(self, n: int = 5) -> Dict[str, float]:
        """Return top N products by revenue."""
        top = (
            self.df.groupby("product")["revenue"]
            .sum()
            .sort_values(ascending=False)
            .head(n)
        )
        return top.to_dict()

    def generate_summary(self) -> Dict[str, Any]:
        """Generate structured business insights."""
        self.load_data()

        summary = {
            "total_revenue": self.total_revenue(),
            "top_products": self.top_products(),
            "transaction_count": len(self.df),
        }

        return summary


if __name__ == "__main__":
    # Example usage
    agent = SalesInsightAgent("sales.csv")
    insights = agent.generate_summary()
    print("Sales Insights")
    print(insights)
