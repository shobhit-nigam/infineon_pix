import requests

url = "https://www.infineon.com/"
response = requests.get(url)
#print(response.content)
print(response.encoding)
