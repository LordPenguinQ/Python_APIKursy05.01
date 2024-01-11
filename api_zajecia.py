import requests

waluta = 'eur'
kurs = 1.24
# http://api.nbp.pl/api/exchangerates/rates/{table}/code}/{date}/
print(f" {waluta}, {kurs}")
# dane = {"table":"C","currency":"dolar amerykański","code":"USD","rates":[{"no":"064/C/NBP/2016","effectiveDate":"2016-04-04","bid":3.6929,"ask":3.7675}]}
code = 'usd'
x='2023-01-05'

dane = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{code}/{x}/')
ile = dane.json()
print(ile)
print(type(ile))
print(ile["rates"][0]["mid"])
#
for i in range(2022,2023):
    for j in range(12,17):
        x = str(i)+'-'+'12'+'-'+str(j)
        print(x)
        # x = '2023-01-05'
        dane = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{code}/{x}/')
        ile = dane.json()
        print(ile["rates"][0]["mid"])
#
