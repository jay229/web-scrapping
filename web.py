import requests
from bs4 import BeautifulSoup
import json

# function fetch and save the data on given path
def fetchAndSave(url, path):
    data = requests.get(url)
    with open(path, "w+", encoding="utf-8") as f:
        f.write(data.text)

# url to fetch the news of mumbai
url = "https://timesofindia.indiatimes.com/city/mumbai"
fetchAndSave(url, "news.html")

# opening the html file in read mode
with open("news.html", "r", encoding="utf-8") as f:
    html_doc = f.read()

# creating BeautifulSoup object to parse the html file
soup = BeautifulSoup(html_doc, 'html.parser')

articles = []
article_data = {}

# iterating on anchor tag after finding and adding the required data in dictionary 
for link in soup.find_all("a"):
    spn = link.find("span")
    head = ""
    if(spn != None):
        article_data = {
            "headline": (spn.text),
            "link": link.get("href")
        }
    else:
        cap = link.find("figcaption")
        if cap != None:
            {
                "headline": (cap.text),
                "link": link.get("href")

            }
    articles.append(article_data)


# removing duplicates from the articles
updated_articles=[]
for article in articles:
    if bool(article) and article not in updated_articles:
        updated_articles.append(article)


# writing the updated_articles into json file
with open("news_articles.json", "w", encoding="utf-8") as json_file:
    json.dump( updated_articles, json_file, indent=4)


# Note: If I run this script, it will automatically creates the news.html and news_articles.json files.