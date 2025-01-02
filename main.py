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
            lov=[("USA", "USA"), ("Canada", "Canada"), ("UK", "UK")],
            dropdown=True,
            value_by_id=True
        )
        # Company selector
        tgb.selector(
            label="Company",
            value="{company}",
            lov="{company_names}",
            dropdown=True,
            value_by_id=True
        )

    # Predictions display
    with tgb.layout(columns="1 1 1"):
        tgb.text("Linear Prediction: {lin_pred}", class_name="metric-box")
        tgb.text("KNN Prediction: {knn_pred}", class_name="metric-box")
        tgb.text("RNN Prediction: {rnn_pred}", class_name="metric-box")

def filter_company_names(country):
    """
    Filter company names based on the selected country
    """
    return company_data[["Symbol", "Shortname"]][
        company_data["Country"] == country
    ].sort_values("Shortname").values.tolist()

# Data Nodes for country and company names 
country_cfg = Config.configure_data_node(id="country", default_data=country)
company_names_cfg = Config.configure_data_node(id="company_names", default_data=company_names)

filter_companies_task_cfg = Config.configure_task(
    id="filter_companies_task",
    function=filter_company_names,
    input=country_cfg,
    output=company_names_cfg
)

scenario_cfg = Config.configure_scenario(
    id="country_company_scenario",
    task_configs=[filter_companies_task_cfg]
)

def on_change(state, name, value):
    if name == "country":
        print(f"{name} was modified to {value}")
        # Update the country data node in the scenario
        state.scenario.country.write(value)
        # Submit the scenario to execute the task
        state.scenario.submit(wait=True)
        # Read the updated company names and update the state
        state.company_names = state.scenario.company_names.read()
    if name == "country":
        print(f"{name} was modified to {value}")

dates = [
    datetime.date(2024, 1, 1),
    datetime.date(2024, 12, 31)
]

if __name__ == "__main__":
    # Run the orchestrator
    tp.Orchestrator().run()
    # Initialize scenario
    scenario = tp.create_scenario(scenario_cfg)
    # Write the default country to the scenario
    scenario.country.write(country)
    # Run the GUI
    gui = tp.Gui(page)
    gui.run(title="S&P 500 Stock Explorer")
