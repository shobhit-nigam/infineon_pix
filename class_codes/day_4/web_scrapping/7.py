import requests
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20130209050253/http://oreilly.com/store/samplers.html"
res = requests.get(url)
print(res.status_code)

cont_obj = res.content
soup_obj = BeautifulSoup(cont_obj , 'html.parser')

samples = soup_obj.find_all("a", "item-title")

books = {}

for b in samples:
    title = b.string.strip()
    books[title] = b.attrs['href']

with open("books.txt", "w") as fa:
    for k in books:
        fa.write(k + "\n")
