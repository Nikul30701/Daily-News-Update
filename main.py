import requests

api_key = "271efe7cb2fd49f598bf4570037c7803"
url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-10-30&sortBy=publishedAt&apiKey={api_key}"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# access the article titles and descriptions
for article in content["articles"]:
    print(article["title"])