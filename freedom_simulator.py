from random import choice
from collections import defaultdict

import pandas as pd

nifty_returns = (
    pd.read_csv("nifty_monthly_returns.csv")[ "Annual"].values
).flatten()

inflation_yearly = pd.read_csv("india-inflation.csv")["InflationRate"].values


def monthly_update(last_investment, last_expense):
    month_inflation = choice(inflation_yearly) / 12
    month_returns = choice(nifty_returns) / 12

    return_on_investment = last_investment * month_returns / 100
    expense = last_expense * (1 + month_inflation / 100)
    investment = last_investment + return_on_investment - expense

    return investment, expense, month_inflation


def simulate_for_expense_percent(expense_percent):
    investment = 1
    expense = investment * expense_percent

    output_dict = defaultdict(list)
    for month in range(600):
        investment, expense, month_inflation = monthly_update(investment, expense)
        if investment < 0:
            investment = 0
        output_dict["month"].append(month)
        output_dict["investment"].append(investment)
        output_dict["expense"].append(expense)
        output_dict["month_inflation"].append(month_inflation)

    simulated_data = pd.DataFrame.from_dict(output_dict)
    simulated_data["deflation_index"] = (
        simulated_data["month_inflation"] / 100 + 1
    ).cumprod()

    simulated_data["real_investment"] = (
        simulated_data["investment"] / simulated_data["deflation_index"]
    )

    simulated_data["real_expense"] = (
        simulated_data["expense"] / simulated_data["deflation_index"]
    )

    return simulated_data

# print(simulate_for_expense_percent(0.005))
