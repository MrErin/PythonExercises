stockDict = {
    'GM': 'General Motors',
    'CAT': 'Caterpillar',
    'EK': 'Eastman Kodak'
}
purchases = [
    ('GM', 100, '10-sep-2001', 48),
    ('CAT', 100, '1-apr-1999', 24),
    ('GM', 200, '1-jul-1998', 56)
]

# Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock and uses the stockDict to look up the full company name. This is the basic relational database join algorithm between two tables.


def purchase_history():
    print('PURCHASE HISTORY:')
    for purchase in purchases:
        print(
            f'On {purchase[2]} I purchased {purchase[1]} shares of {stockDict[purchase[0]]} ({purchase[0]}) at ${purchase[3]} a share; a total value of ${purchase[1] * purchase[3]}.'
        )


purchase_history()


# Create a second purchase summary that which accumulates total investment by ticker symbol. In the above sample data, there are two blocks of GE. These can easily be combined by creating a dict where the key is the ticker and the value is the list of blocks purchased. The program makes one pass through the data to create the dict. A pass through the dict can then create a report showing each ticker symbol and all blocks of stock.

def cost_basis():
    print('COST BASIS:')
    investments = dict((key, 0) for key in stockDict.keys())
    print(investments)
    for purchase in purchases:
        investments[purchase[0]] += purchase[1] * purchase[3]

    print(investments)


cost_basis()


def investment_lists():
    print('INVESTMENT LIST:')
    investments = dict((key, []) for key in stockDict.keys())
    for purchase in purchases:
        investments[purchase[0]] += purchase

    print(investments)


investment_lists()


# Steve's code

portfolio = dict()
for purchase in purchases:
    ticker = purchase[0]

    full_company_name = stockDict[ticker]
    number_of_shares = purchase[1]
    purchase_price = purchase[3]
    full_purchase_price = number_of_shares * purchase_price

    minimal_purchase = (purchase[1], purchase[2], purchase[3])

    try:
        # Append the purchase to the ticker list
        portfolio[ticker].append(purchase)
    except KeyError:
        portfolio[ticker] = list()  # If the key doesn't exist yet, create it
        portfolio[ticker].append(purchase)

    print("I purchased {} stock for ${}".format(
        full_company_name, full_purchase_price))

print(portfolio)


for ticker, purchases in portfolio.items():
    print("------ {} ------".format(ticker))
    total_portfolio_stock_value = 0
    for purchase in purchases:
        total_portfolio_stock_value += purchase[1] * purchase[3]
        print("    {}".format(purchase))
    print("Total value of stock in portfolio: ${}\n\n".format(
        total_portfolio_stock_value))
