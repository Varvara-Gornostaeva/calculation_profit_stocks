import datetime
from collections import namedtuple

import numpy
import pandas
import pandas_datareader.data as web
from pandas_datareader.base import RemoteDataError

from calculate import profit_collum, revenue_collum


def earnings_stocks(stock_id, start_date, revenue):
    StockHandle = namedtuple('StockData', 'stock_id, data_start, revenue')
    revenue = float(revenue)
    end = datetime.date.today()
    try:
        start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        stock = web.DataReader(stock_id, 'yahoo', start, end)
    except RemoteDataError as e:
        stock = web.DataReader(stock_id, 'yahoo', start, end)
    # except (TypeError, ValueError) as e:
    #     return("""data does not match format '%Y-%m-%d'""")
    # except ValueError as e:
    #     raise e("""data does not match format '%Y-%m-%d'""")
    stock.fillna(method='ffill')
    close = stock.Close
    old_cost = close[0]
    profit = close.apply(profit_collum, args=(old_cost, revenue))
    new_revenue = profit.apply(revenue_collum, args=(revenue,))
    # month2_p = profit.groupby(pandas.Grouper(freq='M'))
    # month2_v = new_revenue.groupby(pandas.Grouper(freq='M'))
    month_revenue = new_revenue.resample('M').mean()
    month_profit = profit.resample('M').mean()
    # return month2_v, month2_p
    return month_revenue, month_profit

def total_earnings_profit(*args):
    return sum(list(args))


# appl = earnings_stocks_test('AAPL', '2016-12-24', 1200.0)
# googl = earnings_stocks_test('GOOG', '2001-01-01', 500.0)
# amzn = earnings_stocks_test('AMZN', '2012-01-01', 150.0)
# stocks_all = pd.DataFrame({"AAPL": stock1["Close"], "MSFT": stock2["Close"],"GOOG": stock3["Close"]})
# old_cost2 = stock2.Close[0]                                                                      │
# profit2 = exp.MSFT.apply(profit_collum, args=(old_cost, 150))
def total_earnings_revenue(*args):
    return sum(list(args))

# data = 'AAPL=2016-12-24=1200\r\nGOOG=2001-01-01=50\r\nAMZN=2012-01-01=150'
# d1= data.split('\r\n')
# parse = [item.split("=") for item in d1]
# data2 = [{"id": item[0], "data_start": item[1], "rev": item[2]} for item in parse]
# from collections import namedtuple
# StockData = namedtuple('StockData', 'stock_id, data_start, revenue')
# p = StockData('AAPL=2016-12-24=1200'.split("="))
# data2 = [StockData(item[0], item[1], item[2]) for item in parse]
# p, v = earnings_stocks(data2[0].stock_id, data2[0].data_start, data2[0].revenue)


# new_revenue = prof.apply(revenue_collum, args=(1200,))
# Get data about projects
# so we do cumsum over period of time so we can see the growth
# gp = df.groupby(['period', 'project']).agg({'minutes':'sum'})
# gp = gp.unstack(level=1)
# gp.groupby(pd.TimeGrouper(freq='M')).sum().cumsum().plot.area(alpha=0.75, linewidth=4., figsize=(20, 10))
# # over quarters
# gp.groupby(pd.TimeGrouper(freq='Q')).sum().cumsum().plot.area(alpha=0.75, linewidth=4., figsize=(20, 10))
# # over weeks
# gp.groupby(pd.TimeGrouper(freq='W')).sum().cumsum().plot.area(alpha=0.75, linewidth=4., figsize=(20, 10))


# month = stock.groupby(pandas.Grouper(freq='M')).sum()
# month = stock.groupby(pandas.TimeGrouper(freq='M')).agg(numpy.sum)

# data = 'AAPL=2016-12-24=1200\r\nGOOG=2001-01-01=50\r\nAMZN=2012-01-01=150'
# d1= data.split('\r\n')
# parse = [item.split("=") for item in d1]
# from collections import namedtuple
# StockData = namedtuple('StockData', 'stock_id, data_start, revenue')
# p = StockData('AAPL=2016-12-24=1200'.split("="))
# data2 = [StockData(item[0], item[1], item[2]) for item in parse]


def earnings_stocks(stock_id, start_date, revenue):
    # end_date = format(datetime.date.today(), '%Y-%m-%d')
    StockHandle = namedtuple('StockData', 'stock_id, data_start, revenue')
    revenue = float(revenue)
    end = datetime.date.today()
    try:
        start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        stock = web.DataReader(stock_id, 'yahoo', start, end)
    except RemoteDataError as e:
        stock = web.DataReader(stock_id, 'yahoo', start, end)
    # except (TypeError, ValueError) as e:
    #     return("""data does not match format '%Y-%m-%d'""")
    # except ValueError as e:
    #     raise e("""data does not match format '%Y-%m-%d'""")
    stock.fillna(method='ffill')
    # close = stock.loc[:, "Close"]
    close = stock.Close
    old_cost = float(close[0])
    print(type(old_cost))
    profit = close.apply(profit_collum, args=(old_cost, revenue))
    new_revenue = profit.apply(revenue_collum, args=(revenue,))
    month_revenue = new_revenue.resample('M').mean()
    month_profit = profit.resample('M').mean()
    # print(month_revenue, month_profit)
    return month_revenue, month_profit
    # return month_revenue.tolist(), month_profit.tolist()
# month = stock.groupby(pandas.Grouper(freq='M')).sum()
# month = stock.groupby(pandas.TimeGrouper(freq='M')).agg(numpy.sum)

def earnings_stocks_test(stock_id, start_date, revenue):
    # end_date = format(datetime.date.today(), '%Y-%m-%d')
    StockHandle = namedtuple('StockData', 'stock_id, data_start, revenue')
    revenue = float(revenue)
    end = datetime.date.today()
    try:
        start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        stock = web.DataReader(stock_id, 'yahoo', start, end)
    except RemoteDataError as e:
        stock = web.DataReader(stock_id, 'yahoo', start, end)
    # except (TypeError, ValueError) as e:
    #     return("""data does not match format '%Y-%m-%d'""")
    # except ValueError as e:
    #     raise e("""data does not match format '%Y-%m-%d'""")
    # print(month_revenue, month_profit)
    return stock
