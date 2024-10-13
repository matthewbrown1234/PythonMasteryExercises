import csv

def get_portfolio(file_path):
    portfolio = []
    with open(file_path) as csvfile:
        rows = csv.reader(csvfile, delimiter= ' ')
        for row in rows:
            portfolio_row = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(portfolio_row)
    return portfolio

def calculate_portfolio_cost(portfolio):
    total_cost = 0.0
    for row in portfolio:
        total_cost = total_cost + row['shares'] * row['price']
    return total_cost



def main():
    portfolio = get_portfolio('./Data/portfolio.dat')
    portfolio_cost = calculate_portfolio_cost(portfolio)
    print('Total cost:', portfolio_cost)


if __name__ == '__main__':
    main()

