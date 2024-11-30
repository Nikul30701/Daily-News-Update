import requests
from emailing import send_email

api_key = "271efe7cb2fd49f598bf4570037c7803"
url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-10-30&sortBy=publishedAt&apiKey=271efe7cb2fd49f598bf4570037c7803&language=en"

# Make request
response = requests.get(url)

# Get a dictionary with data
content = response.json()

# Access the article titles and descriptions
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" \
        + article["description"] \
        + "\n" + article["url"]+ 2*"\n"

body = body.encode("utf-8")

# Send email
send_email(message=body)
