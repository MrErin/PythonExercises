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
    for purchase in purchases:
        if purchase[0] in stockDict:
            print(
                f'On {purchase[2]} I purchased {purchase[1]} shares of {stockDict[purchase[0]]} ({purchase[0]}) at ${purchase[3]} a share; a total value of ${purchase[1] * purchase[3]}.'
            )


purchase_history()


# Create a second purchase summary that which accumulates total investment by ticker symbol. In the above sample data, there are two blocks of GE. These can easily be combined by creating a dict where the key is the ticker and the value is the list of blocks purchased. The program makes one pass through the data to create the dict. A pass through the dict can then create a report showing each ticker symbol and all blocks of stock.

def cost_basis():
    investments = dict([(key, 0) for key in stockDict.keys()])
    for purchase in purchases:
        if purchase[0] in investments.keys():
            investments[purchase[0]] += purchase[1] * purchase[3]

    print(investments)


cost_basis()


def investment_lists():
    investments = dict([(key, []) for key in stockDict.keys()])
    for purchase in purchases:
        if purchase[0] in investments.keys():
            investments[purchase[0]] += purchase

    print(investments)


investment_lists()
