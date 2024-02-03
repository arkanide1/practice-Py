from bs4 import BeautifulSoup
import requests

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text,  "html.parser")


titlelines = soup.select('.titleline')
links = []

for titleline in titlelines:
    links.append(titleline.find('a')['href'])


votes = soup.select('.score')

for i in range(len(votes)):

    if int(votes[i].contents[0][:-7]) > 100:
        # as long as votes and links have same indexes so we can do this
        print(int(votes[i].contents[0][:-7]))
        print(links[i])
        print("")
