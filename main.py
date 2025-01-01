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

with tgb.Page() as page:
    # Page header 
    tgb.text("# S&P 500 Stock Value Exploation", mode="md", class_name="text-center")

    # Date range selelctor (for future use)
    tgb.date_range("{dates}", label_start="Start Date", labe_end="End Date")

    # Country and company selectors 
    with tgb.layout(columns="1 3"):
        # Country selector 
        tgb.selector(
            label="Country",
            value="{country}",
            lov=[("USA", "USA"), ("Canada", "Canada"), ("UK", "UK")]
        )

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
