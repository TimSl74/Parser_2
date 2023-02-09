import requests as r
from bs4 import BeautifulSoup
import time

print("control point 0")

# Обработка стартовой страницы
url = "https://dubai.dubizzle.com/motors/used-cars/?page=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}

response = r.get(url=url, headers=headers).text
soup = BeautifulSoup(response, "lxml")

with open("start_page.json", "w") as file:
    file.write(str(soup))

print("control point 1")

with open("start_page.json", "r") as file:
    first_page = file.read()

# print(first_page)
try:
    #soup_1 = BeautifulSoup(first_page, "lxml")
    datas_1 = soup.find_all("div", class_="sc-cmkc2d-0 dhbOk")
    with open("first_search.json", "w") as file:
        file.write(str(datas_1))
except:
    pass

with open("first_search.json", "r") as file:
    first_search = file.read()
auto_url = []
soup_2 = BeautifulSoup(first_search, "lxml")
# В first_search всё сохраняется одной строкой, из-за этого не работает перебор for soups in soup_2
for soups in soup_2:
    datas_2 = soups.find("a", class_="sc-cmkc2d-1 sc-cmkc2d-2 Npagx jlrPcY").get("href")
    auto_url.append(datas_2)
    time.sleep(3)
    print("+1")
with open("auto_url.json", "w") as file:
    file.write(str(auto_url))

print("control point 2")
