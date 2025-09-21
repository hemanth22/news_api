import requests
import os

# Replace 'YOUR_API_KEY' with your actual News API key
api_key =  os.environ.get('NEWSAPI_ORG_KEY')

# Specify the base URL for the News API 
base_url = 'https://newsapi.org/v2/'

# Define the endpoint for the "everything" API
endpoint = 'everything'

# Define list of countries
queries = ['USD', 'SGD', 'INR']

# Define webhook url
webhook_url = "http://localhost:8000/newsapiwebhook"

for query in queries:
    print("News Country: ",f"{query}","\n")
    parameters = {
        'q': query,
        'apiKey': api_key,
    }

# Specify the parameters for your request (e.g., query, sources, date, etc.)
#parameters = {
#    'q': 'SGD',  # Replace with your desired query
#    'apiKey': api_key,
#}

# Make the API request
    response = requests.get(f"{base_url}{endpoint}", params=parameters)

# Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
    # Parse the JSON response
        data = response.json()
        for article in data.get('articles', []):
            payload = {
                "source": "NewsAPI.org",
                "title": article.get('title', 'N/A'),
                "description": article.get('description', 'N/A'),
                "url": article.get('url', 'N/A'),
                "publishedTime": article.get('publishedAt', 'N/A'),
                "sourcename": article.get("source", {}).get("name", "N/A"),
                "author": article.get('author', 'N/A')
            }
#            print("JSON News:",payload)
            try:
               #print(payload)
               response = requests.post(webhook_url, json=payload)
               if response.status_code == 200:
                   print(f"✅ Sent data for {payload['source']}")
               else:
                  print(f"⚠️ Failed to send {payload['symbol']}: {response.status_code} - {response.text}")
            except requests.RequestException as e:
                print(f"❌ Error sending data for {payload['symbol']}: {e}")

    if response.status_code != 200:
        print("Failed to establish connection with NewsAPI.org")
