import time
from libs.openexchange import OpenExchangeClient

APP_ID='f1fe774e372c4262a40d41d0bd7c9d12'

client = OpenExchangeClient(APP_ID)

#ENDPOINT='https://openexchangerates.org/api/latest.json'

#response = requests.get(f'{ENDPOINT}?app_id={APP_ID}')
#exchange_rates = response.json()["rates"]

usd_amount = 1000
start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()

print(end-start)

start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()

print(end-start)

start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()

print(end-start)
print(f'USD {usd_amount} is GBP {gbp_amount:.2f}')