import requests
import os

NEWSS_API_KEY = os.environ.get('NEWS_API_KEY')

url = 'https://gnews.io/api/v4/top-headlines?token='+NEWSS_API_KEY

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
