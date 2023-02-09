import requests as r
from bs4 import BeautifulSoup

print("control point 0")

# Обработка стартовой страницы
url = "https://dubai.dubizzle.com/motors/used-cars/mercedes-benz/s-class/2023/1/17/mercedes-s550l-wald-body-kit-full-options--2-619---f08babea916440e8a9f886485a92c4ed/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

response = r.get(url=url, headers=headers).text
soup = BeautifulSoup(response, "lxml")

with open("First_page.html", "w") as file:
    file.write(str(soup))

print("control point 1")

with open("First_page.html", "r") as file:
    first_page = file.read()

for string in first_page:
    try:
        print("Yes")
        soup = BeautifulSoup(first_page, "lxml")
        datas = soup.find("div", class_="sc-cmkc2d-0 dhbOk").find("a").get("href")
        print(datas)
    except:
        pass
