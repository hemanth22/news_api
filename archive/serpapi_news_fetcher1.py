import os
import json
from serpapi import GoogleSearch

bank_names = ["Societe Generale", "DBS", "Standard Chartered"]

for bank in bank_names:
    params = {
        "api_key": os.environ["SERPAPI"],
        "engine": "google_news",
        "q": bank,
        "hl": "en",
        "gl": "in"
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    # Create a clean filename based on the bank name
    safe_name = bank.lower().replace(" ", "_")
    output_file = f"news_results1_{safe_name}.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"Results for {bank} saved to {output_file}")