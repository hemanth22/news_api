import requests
import os

# Replace with your actual GNews API key
#API_KEY = 'your_api_key_here'

API_KEY =  os.environ.get('GNEWS_IO_KEY')

# Base URL
BASE_URL = 'https://gnews.io/api/v4/search'

webhook_url = "https://fastapi-webhook-receiver.vercel.app/gnewswebhook"
#webhook_url = "http://localhost:8000/gnewswebhook"

# Keywords to search
keywords = ['socgen', 'dbs', 'stanchart']

# Loop through keywords and query the API
for keyword in keywords:
    params = {
        'q': keyword,
        'apikey': API_KEY,
        'lang': 'en',
        'max': 5  # Limit results per keyword
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()
#    print(data)

    print(f"\n🔍 Results for: {keyword.upper()}")
    for article in data.get('articles', []):
        payload = {
            "source": "GNews.io",
            "title": article.get('title', 'N/A'),
            "description": article.get('description', 'N/A'),
            "url": article.get('url', 'N/A'),
            "publishedTime": article.get('publishedAt', 'N/A'),
            "sourcename": article.get("source", {}).get("name", "N/A")
        }
#        print("JSON News:",payload)
        try:
           response = requests.post(webhook_url, json=payload)
           if response.status_code == 200:
               print(f"✅ Sent data for {payload['source']}")
           else:
               print(f"⚠️ Failed to send {payload['symbol']}: {response.status_code} - {response.text}")
        except requests.RequestException as e:
             print(f"❌ Error sending data for {payload['symbol']}: {e}")
#    print("=" * 80)

#    for article in data.get('articles', []):
#        print("Title:", article.get('title', 'N/A'))
#        print("Description:", article.get('description', 'N/A'))
#        print("URL:", article.get('url', 'N/A'))
#        print("Published At:", article.get('publishedAt', 'N/A'))
#        print("Source Name:", article.get('source', {}).get('name', 'N/A'))
#        print("-" * 80)


