import requests
import numpy as np
import os
from helper import calculate_percentChange_24hours, plot_candlestick_chart


#may need to change
symbol = input("Enter the Ticker Symbol Please: ")


##this is going to be the API key and information for the twelve data
twelve_api_key = os.environ.get('twelve_api_key')

url_12 = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval=1min&apikey=f8c1dda7c05943328c8b314d4f8ea656'
x = requests.get(url_12)
data_12 = x.json()


##this is the API key for alpha vantage
api_key = os.environ.get('ALPHAVANTAGE_API_KEY') ## this will retreive the API key from the OS


url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'
r = requests.get(url)
data = r.json()


dates = list(data['Time Series (Daily)'].keys()) ## this will extract the amt of dates in the data dictionary pulled in from API
num_dates = len(dates)
num_features = len(data['Time Series (Daily)'][dates[0]])  # Number of features for each date


# Create an empty numpy array to hold the data
data_array = np.zeros((len(dates), 6), dtype=object)

# Fill the numpy array with the data
for i, date in enumerate(dates):

    date_data = data['Time Series (Daily)'][date]
    data_array[i, 0] = date
    data_array[i, 1] = float(date_data['1. open'])
    data_array[i, 2] = float(date_data['2. high'])
    data_array[i, 3] = float(date_data['3. low'])
    data_array[i, 4] = float(date_data['4. close'])
    data_array[i, 5] = float(date_data['5. volume'])


def get_realtime_data(symbol, api_key):
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()

    if 'Global Quote' in data:
        return data['Global Quote']
    else:
        return None

## now that we have this data in a numpy array, I want to be able to see the growth of the stock based on the last 24 hours, the last week, the last month, and the last year.

##calculate the growth of the stock in the last 24 hours

print(data_array)
print(calculate_percentChange_24hours(data_array, symbol))
print(plot_candlestick_chart(data_array, symbol))
print(data_12)