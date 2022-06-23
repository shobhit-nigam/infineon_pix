import requests

url = "https://www.infineon.com/cms/en/careers/"
url = "https://www.linkedin.com/company/infineon-technologies/jobs"
response = requests.get(url)
print(response)
