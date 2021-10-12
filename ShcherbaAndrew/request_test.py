import requests

response = requests.get("https://news.yahoo.com/rss/")
print(response.status_code)
