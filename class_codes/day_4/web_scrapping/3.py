import requests

url = "https://www.infineon.com/"
response = requests.get(url)
#print(response.content)
#print(response.headers)

for k, v in response.headers.items():
    print(k, "-->", v)
    print()
