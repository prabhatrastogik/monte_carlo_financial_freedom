# Monte Carlo Simulation applied to a portfolio return vs expenses with variations of returns, inflation and taxation applied

## Structure of Calculation

- Portfolio Starts with a fixed investment I(0) that is assumed to be invested in index-equivalent funds and Monthly Expenses E(0) as inputs
- Invstement amount, expenses and returns across months is calculated as:

Monthly Return:
R(m) = I(m-1)*[Simulated monthly return of an index, implemented using monthly distribution of Nifty returns]

Investment Update Function:
I(m) = I(m-1) + R(m) - E(m) // Expenses are modelled using E(m) function

Expenses:
E(m) = E(m-1) * (1 + sumulated monthly inflation)


Plotting of monte carlo simulation has following analysis:

- I(m) over months
- Real value of I(m) over months 
    Real Value = Inflation Adjusted current value

- E(m) over months
- Real Value of E(m) over months

Month Range included = 50 years = 600 months
