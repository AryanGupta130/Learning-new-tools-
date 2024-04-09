import requests
import numpy as np
import os
from datetime import datetime, date
from helperfunctions import calculate_percentChange_24hours, plot_candlestick_chart, plot_candlestick_chart_12


symbol = input("Enter the Ticker Symbol Please: ")

##this is going to be the API key and information for the twelve data
twelve_api_key = os.environ.get('twelve_api_key')

url_12 = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval=15min&apikey=f8c1dda7c05943328c8b314d4f8ea656'
x = requests.get(url_12)
data_12 = x.json()

for entry in data_12['values']:
    entry['datetime'] = datetime.strptime(entry['datetime'], '%Y-%m-%d %H:%M:%S')

# Filter data for entries with today's date
today = date.today()
today_entries = [entry for entry in data_12['values'] if entry['datetime'].date() == today]

# Create numpy array with required information
data_array_12 = np.zeros((len(today_entries), 7), dtype=object)
for i, entry in enumerate(today_entries):
    formatted_datetime = entry['datetime'].strftime("%Y-%m-%d (%H:%M)")

    data_array_12[i, 0] = formatted_datetime  # Store date and time at index 0
    data_array_12[i, 1] = entry['open']
    data_array_12[i, 2] = entry['high']
    data_array_12[i, 3] = entry['low']
    data_array_12[i, 4] = entry['close']
    data_array_12[i, 5] = entry['volume']

print(data_array_12)






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



## now that we have this data in a numpy array, I want to be able to see the growth of the stock based on the last 24 hours, the last week, the last month, and the last year.

##calculate the growth of the stock in the last 24 hours

print(plot_candlestick_chart(data_array, symbol))
print(data_12)
print(plot_candlestick_chart_12(data_array_12, symbol))
