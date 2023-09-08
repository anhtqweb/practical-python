# report.py
#
# Exercise 2.4
import fileparse
import stock
import tableformat

def read_portfolio(filename):
    with open(filename) as f:
        listStock = fileparse.parse_csv(f, select=['name', 'shares', 'price'], types=[str, int, float])
        listStock = [stock.Stock(s['name'], s['shares'], s['price']) for s in listStock]

    return listStock

def read_prices(filename):
    with open(filename) as f:
        pricelist = fileparse.parse_csv(f, types=[str, float], has_headers=False)
    return dict(pricelist)

def make_report(portfolio, prices):
    report = []
    for holding in portfolio:
        name = holding.name
        shares = holding.shares
        price = prices[name]
        change = price - holding.price
        row = (name, shares, price, change)
        report.append(row)

    return report

def print_report(report, formatter):
    headers = ('Name', 'Shares', 'Price', 'Change')
    formatter.headings(headers)
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

def portfolio_report(porfolio_file, prices_file, fmt='txt'):
    prices = read_prices(prices_file)   
    portfolio = read_portfolio(porfolio_file)

    formatter = tableformat.create_formatter(fmt)

    report = make_report(portfolio, prices)
    print_report(report, formatter)

def main(argv):
    portfolio_report(argv[1], argv[2], argv[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)