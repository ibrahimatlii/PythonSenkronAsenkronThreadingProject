import threading
import time
import requests
import asyncio
import aiohttp

async def get_data_asyncio_but_as_wrapper(urls):
    start_time=time.time()
    json_dizi=[]

    async with aiohttp.ClientSession() as session: #async io'da session oluşturmadan istek atılmıyor
        for url in urls:
            async with session.get(url) as resp: #istek atıldı
                json_dizi.append(await resp.json())
    end_time=time.time()
    elapsed_time=end_time-start_time
    print("Execution time : ", elapsed_time, "Seconds.")
    return json_dizi

#yukardaki istediğimiz sonucu hızlı alamamıştık şimdi uygun bir şekilde yeni bir fonksiyonla yazacağız


async def get_data(session,url,json_dizi):
    async with session.get(url) as resp:
        json_dizi.append(await resp.json())


async def get_data_async_concurrently(urls):
    start_time = time.time()
    json_dizi=[]

    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(asyncio.ensure_future(get_data(session,url,json_dizi)))
        await asyncio.gather(*tasks)

    end_time = time.time()
    elapsed_time=end_time-start_time
    print("Execution time : ", elapsed_time, "Seconds.")
    return json_dizi

urls=["https://postman-echo.com/delay/3"]*5
#asyncio.run(get_data_asyncio_but_as_wrapper(urls))

#yukardaıki metot için Execution time :  16.324233770370483 Seconds. saniyede ceavp verdi bu şekilde senkrondan sadece iki saniye kadar  daha hızlı
#bu bizim için istediğimiz gibi olmadı thread bile ortlama 4 saniyede yaptı. e hani threadden daaha hızlı cevap verirdi çünkü ona göre
#uygun bir şekilde yazmadık şimdi yazalım

asyncio.run(get_data_async_concurrently(urls))
#burada dikakt ederseniz  Execution time :  3.6397106647491455 Seconds. saniyede sürdü asenkron bir şekilde programın cevabını aldık
