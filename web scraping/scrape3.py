from bs4 import BeautifulSoup
import requests
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text,  "html.parser")


titlelines = soup.select('.titleline')
links = []

for titleline in titlelines:
    links.append(titleline.find('a'))
votes = soup.select('.score')


def create_custom_hn(links, votes):
    news = []
    for i in range(len(votes)):
        if int(votes[i].contents[0][:-7]) >= 90:
            # as long as votes and links have same indexes so we can do this
            news.append({"title": links[i].getText(), "vote": int(
                votes[i].contents[0][:-7]), "link": links[i]['href']})

    return sort_stories_by_votes(news)


def sort_stories_by_votes(news):
    return sorted( news ,  key= lambda k:k["vote"], reverse=True)



pprint.pprint(create_custom_hn(links, votes))
