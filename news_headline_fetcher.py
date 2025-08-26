import requests

API_KEY = "your_api_key_here" 
url = "https://newsapi.org/v2/top-headlines"

category = input("Enter category (technology/sports/health/science): ").lower()

# API request
params = {
    "country": "us",
    "category": category,
    "apiKey": API_KEY,
    "pageSize": 5   
}

response = requests.get(url, params=params).json()

# headlines print
if response["status"] == "ok" and response["articles"]:
    print(f"\nTop 5 {category} headlines:\n")
    for i, article in enumerate(response["articles"], 1):
        print(f"{i}. {article['title']}")
else:
    print("No headlines found or invalid category!")