import requests
import threading
import time


def get_sync_data(urls):
    start_time=time.time()  #o esnadaki pc zamani
    json_dizi=[]
    for url in urls:
        json_dizi.append(requests.get(url).json())
    end_time=time.time() #işlem bittiğindeki zamanımız
    elapsed_time=end_time-start_time
    print("Execution time : ", elapsed_time, "Seconds.")
    return json_dizi

# http://postman-echo.com/delay/3  bu sitedeki link 3 saniye geçince sitedeyi açar
urls=["https://postman-echo.com/delay/3"]*5
get_sync_data(urls)

#Execution time :  18.701142072677612 Seconds.  internetin hızına göre pc hızına göre bazen değişkenlik gösterebilir