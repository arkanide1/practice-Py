from bs4 import BeautifulSoup
import requests
import pprint


def create_custom_hn(links, votes):
    tmp_news = []
    for i in range(len(votes)):
        if int(votes[i].contents[0][:-7]) >= 100:
            # as long as votes and links have same indexes so we can do this
            tmp_news.append({"title": links[i].getText(), "vote": int(
                votes[i].contents[0][:-7]), "link": links[i]['href']})
    return tmp_news


def sort_stories_by_votes(news_list):
    return sorted(news_list,  key=lambda k: k["vote"], reverse=True)


def pages(number_of_pages):
    news = []
    for i in range(1, number_of_pages+1):
        res = requests.get(f"https://news.ycombinator.com/news?p={i}")
        soup = BeautifulSoup(res.text,  "html.parser")

        titlelines = soup.select('.titleline')
        links = []
        for titleline in titlelines:
            links.append(titleline.find('a'))
        votes = soup.select('.score')

        news += create_custom_hn(links, votes)
    return sort_stories_by_votes(news)


num = int(input("enter the number of pages you want to check:"))
pprint.pprint(pages(num))
