from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import numpy as np
import os

@api_view(['GET'])
def get_stock_data(request, symbol):
    api_key = os.environ.get('ALPHAVANTAGE_API_KEY')
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    data_array = prepare_data_array(data)
    return Response(data_array)

def prepare_data_array(data):
    dates = list(data['Time Series (Daily)'].keys())
    data_array = np.zeros((len(dates), 6), dtype=object)

    for i, date in enumerate(dates):
        date_data = data['Time Series (Daily)'][date]
        data_array[i, 0] = date
        data_array[i, 1] = float(date_data['1. open'])
        data_array[i, 2] = float(date_data['2. high'])
        data_array[i, 3] = float(date_data['3. low'])
        data_array[i, 4] = float(date_data['4. close'])
        data_array[i, 5] = float(date_data['5. volume'])

    return data_array.tolist()