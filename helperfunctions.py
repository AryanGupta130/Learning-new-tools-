from datetime import datetime, timedelta
import plotly.graph_objs as go


## these functions will show the different percent changes over a period of time
def calculate_percentChange_24hours(data_array, symbol):
    percent_change = (data_array[0][4] - data_array[1][4]) / data_array[1][4] * 100
    Ticker = symbol.upper()
    return f'Percent Change in last 24 hours for {Ticker} is {percent_change}'

def calculate_percentChange_lastweek(data_array, symbol):
    return None

def calculate_percentChange_lastmonth(data_array, symbol):
    return None


def calculate_percentChange_last3months(data_array, symbol):
    return None


def calculate_percentChange_last6months(data_array, symbol):
    return None


def calculate_percentChange_last9months(data_array, symbol):
    return None


def calculate_percentChange_lastYear(data_array, symbol):
    return None


## this function will be used for plotting purposes
def plot_candlestick_chart(data_array, symbol):
    # Extracting data for the candlestick chart
    dates = data_array[:, 0]
    opens = data_array[:, 1]
    highs = data_array[:, 2]
    lows = data_array[:, 3]
    closes = data_array[:, 4]

    # Create Candlestick chart
    fig = go.Figure(data=[go.Candlestick(x=dates,
                    open=opens,
                    high=highs,
                    low=lows,
                    close=closes)])

    # Update chart layout
    fig.update_layout(title=f'Candlestick Chart for {symbol}',
                      xaxis_title='Date',
                      yaxis_title='Price')

    # Show the chart
    fig.show()

