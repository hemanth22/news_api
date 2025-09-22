import requests
import os

# Replace with your actual API key from NewsData.io

API_KEY =  os.environ.get('NEWSDATA_IO_KEY')

# Base URL
BASE_URL = 'https://newsdata.io/api/1/news'

# Keywords to search
keywords = ['socGen', 'DBS', 'StanChart', 'INR', 'Ship']

# Loop through keywords and query the API
for keyword in keywords:
    params = {
        'apikey': API_KEY,
        'q': keyword,
        'language': 'en'
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    print(f"\n🔍 Results for: {keyword}")
    print("Printing Data", data)
    

#    for article in data.get('results', []):
#        print("Title:", article.get('title', 'N/A'))
#        print("Description:", article.get('description', 'N/A'))
#        print("URL:", article.get('link', 'N/A'))
#        print("Published At:", article.get('pubDate', 'N/A'))
#        print("Source Name:", article.get('source_id', 'N/A'))
#        print("-" * 80)
