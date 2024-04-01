from datetime import datetime, timedelta

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
