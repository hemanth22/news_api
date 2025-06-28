import os
from serpapi import GoogleSearch
import json

params = {
  "api_key": os.environ["SERPAPI"],
  "engine": "google_news",
  "hl": "en"
}

search = GoogleSearch(params)
results = search.get_dict()

source = results
#source = results.get("search_parameters", {})
#name = source.get("engine")

data1 = source.get("search_parameters", {})
data2 = data1.get("engine", {})


print(f"Search Parameters: {data1}")
print(f"Search Parameters: {data2}")

if data2 == "google_news":
    print("The search engine is Google News.")
    news_results = source.get("news_results", [{}])

news_results_data = source.get("news_results", [{}])

for idx, item in enumerate(news_results_data, start=1):
    print(f"\nNews Item {idx}:")

    # Extract from 'highlight' if available
    highlight = item.get("highlight", {})
    title = highlight.get("title", "")
    link = highlight.get("link", "")
    print(f"  Highlight Title: {title}")
    print(f"  Highlight Link : {link}")

    # Extract from 'stories' if available
    stories = item.get("stories", [])
    for j, story in enumerate(stories, start=1):
        story_title = story.get("title", "")
        story_link = story.get("link", "")
        print(f"    Story {j} Title: {story_title}")
        print(f"    Story {j} Link : {story_link}")
