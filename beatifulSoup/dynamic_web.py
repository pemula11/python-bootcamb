from bs4 import BeautifulSoup
import lxml, requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = (response.text)

soup = BeautifulSoup(yc_web_page, "html.parser")
article = (soup.find_all(name="tr", class_="athing submission")) #anchor a link class athing
article_vote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print((article_vote))
article_text = []

for i, title in enumerate(article):
    (article_text.append(f"title : {title.text} - vote {i}"))

print(article_text)
print("--------------")
highest_vote = max(article_vote)
idx = article_vote.index(highest_vote)

print(f"highest vote is {article[idx].getText()} with vote: {highest_vote}")