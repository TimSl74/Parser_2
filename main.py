import requests as r
from bs4 import BeautifulSoup

print("control point 1")

# Обработка стартовой страницы
url = "https://dubai.dubizzle.com/motors/used-cars/"

response = r.get(url).text
soup = BeautifulSoup(response, "lxml")
# datas = soup.find_all("div", class_="td")

with open("First_page.json", "w") as file:
    file.write(str(soup))

for word in soup:
    print(word)
