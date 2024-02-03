from bs4 import BeautifulSoup
# allows us to use HTML and grab data to scrape
import requests
# allows us to download this data

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text,  "html.parser")
# print(soup.body.contents)
# print(soup.find('div'))
# print(soup.find_all('div'))
# print(soup.title)
# print(soup.find(id="score_39241113"))

scores = soup.select('.score')

for score in scores :
    if int(score.contents[0][:-7]) > 100:
        print(score.contents[0][:-7])
