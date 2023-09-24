

import requests
def get_crpyto_data():
    response = requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
    if response.status_code==200:
        return response.json()

user_input=input("bir kripto adını giriniz :")
crypto_response=get_crpyto_data()

for crypto in crypto_response:

    if crypto["currency"]==user_input:


        print(crypto["price"])

        break

# internetten veri çekip kullanıcıya sonucu gösterdiğimix bir uygulama oldu bu