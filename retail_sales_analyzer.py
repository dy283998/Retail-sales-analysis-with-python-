import pandas as pd
import matplotlib.pyplot as plt

class RetailSalesAnalyzer:
    def __init__(self):
        # Load CSV file into a pandas DataFrame
        self.data = pd.read_csv('retail_sales.csv')
        # Convert 'date' column from string to datetime format
        self.data['date'] = pd.to_datetime(self.data['date'])

    def data_clean(self):
        # Remove rows with any missing/null values
        self.data.dropna(inplace=True)

    def total_sales_per_product(self):
        # Group data by 'product' and sum the 'sales' for each product
        return self.data.groupby('product')['sales'].sum()

    def best_selling_product(self):
        # Sort total sales per product in descending order and get the top product
        total_sales = self.total_sales_per_product()
        return total_sales.sort_values(ascending=False).index[0]

    def average_daily_sales(self):
        # Calculate the average (mean) of sales column
        return self.data['sales'].mean()

    def plot_sales_trend(self):
        # Group sales by date and sum sales per day
        sales_trend = self.data.groupby('date')['sales'].sum()
        # Plot sales trend as a bar chart
        sales_trend.plot(kind='bar')
        plt.title('Sales Trend Over Time')
        plt.xlabel('Date')
        plt.ylabel('Total Sales')
        plt.tight_layout()
        plt.show()

# Example usage:
# if __name__ == "__main__":
#     analyzer = RetailSalesAnalyzer()
#     analyzer.data_clean()
#     print(analyzer.total_sales_per_product())
#     print("Best selling product:", analyzer.best_selling_product())
#     print("Average daily sales:", analyzer.average_daily_sales())
#     analyzer.plot_sales_trend()
