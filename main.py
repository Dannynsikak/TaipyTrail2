import taipy as tp
import taipy.gui.builder as tgb
from taipy import Config
import pandas as pd
import datetime

#Sample data
company_data = pd.DataFrame({
    "Symbol": ["AAPL", "GOOGL", "MSFT", "SHOP", "TD", "BMO", "HSBC", "BARC"],
    "Shortname": [
        "Apple", "Google", "Microsoft", "Shopify", "Toronto-Dominion", 
        "Bank of Montreal", "HSBC", "Barclays"
    ],
    "Country": ["USA", "USA", "USA", "Canada", "Canada", "Canada", "UK", "UK"]
})
# Initial states
country = "USA" # Default selected country
company = "AAPL" # Default selected company

# Filter company names based on the selected country
company_names = company_data[["Symbol","Shortname"]][
    company_data["Country"] == country
].sort_values("Shortname").values.tolist()

# placeholder prediction values
lin_pred, knn_pred, rnn_pred = 150, 152, 149

dates = [
    datetime.date(2024, 1, 1),
    datetime.date(2024, 12, 31)
]

if __name__ == "__main__":
    # Run the orchestrator

    # Initialize scenario

    # Run the GUI
    gui = tp.Gui(page)
    gui.run(title="S&P 500 Stock Explorer")
