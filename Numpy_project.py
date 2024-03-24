import requests
import numpy as np
import os

api_key = os.environ.get('ALPHAVANTAGE_API_KEY') ## this will retreive the API key from the OS

symbol = input("Enter the Ticker Symbol Please: ")
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

print(data_array)










