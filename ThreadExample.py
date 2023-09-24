import threading
import requests
import time

class ThreadingDownloader(threading.Thread):
    json_dizi=[]
    def __init__(self,url):
        super().__init__()
        self.url=url

    def run(self):
        response =requests.get(self.url)
        self.json_dizi.append(response.json())
        #print(self.json_dizi)# datayı görmek istersen bunu da yazabilirsin ve aşağıdaki print(t) yorum yap daha güzel görülür
        return response.json()

def get_data_threading(urls):
    start_time = time.time()  # o esnadaki pc zamani
    #kaç tane url varsa o kadar url yapalı makat thread gücünü gösterelim
    thread_dizi=[]
    for url in urls:
        t=ThreadingDownloader(url) #kendi oluşturduğumuz sınıfa parametre olarak url yi verdik
        t.start() #yukarıda run fonkiyonu çalışır. t.start() deyince
        thread_dizi.append(t)

    for t in thread_dizi:
        t.join()
        print(t) #threadler nasıl gözükür ona bakalım.
    end_time = time.time()  # işlem bittiğindeki zamanımız

    elapsed_time = end_time - start_time

    print("Execution time : ", elapsed_time, "Seconds.")

urls=["https://postman-echo.com/delay/3"]*5
get_data_threading(urls)


# 10 ayrı istek attı paralel bir şekilde ve bunu Execution time :  3.7794153690338135 Seconds. saniyede oluşturduk
#5 threadi normalde senkronExample.py  16.701142072677612 Seconds. yaparken burada ise 3.77 saniyede hepsini yaptı
#çok fark olduğunu gördük ama her işimizde de thread kullanmamalıyız  thread sayısı artan işlemde ise 1000 tane gibi bu bizim
#işlemcimizi zorlar genel olarak birden fazla işlem için bu threadingi kullaniliriz ama internet için veri çekebilmemiz için bundan daha
#kullanılışlı olan bir yöntemi denyeceğiz
