import requests
# NOT working

def convert_dbp_to_usd(amount):
    response = requests.get('https://api.exchangerates-api.com/v4/latest/GBP')
    exchange_rates = response.json()['rates']
    usd_rate = exchange_rates['USD']
    usd_amount = amount * usd_rate

    return usd_amount


pounds = int(input())
us_dollars = convert_dbp_to_usd(pounds)
print(us_dollars)