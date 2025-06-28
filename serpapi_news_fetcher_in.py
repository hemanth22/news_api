import os
from serpapi import GoogleSearch
import json

params = {
  "api_key": os.environ["SERPAPI"],
  "engine": "google_news",
  "hl": "en",
  "gl": "in"
}

search = GoogleSearch(params)
results = search.get_dict()

# Write results to a JSON file
output_file = "news_results.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"Results saved to {output_file}")
