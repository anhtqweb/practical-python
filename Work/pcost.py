# pcost.py
#
# Exercise 1.27
import sys
import report

def portfolio_cost(filename):
    '''Computes the total cost (shares * price) of a portfolio file'''
    total = 0
    portfolio = report.read_portfolio(filename)

    for stock in portfolio:
        total += stock.shares * stock.price
    return total

def main(argv):
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = 'Data/portfolio.csv'

    cost = portfolio_cost(filename)
    print('Total cost:', cost)

if __name__ == '__main__':
    main(sys.argv)