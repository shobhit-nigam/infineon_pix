import nltk
import pprint
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.infineon.com/"
html_obj = urlopen(url).read()
soup_obj = BeautifulSoup(html_obj, 'html.parser')

lista = soup_obj.find_all("a")
print("\n", lista)
