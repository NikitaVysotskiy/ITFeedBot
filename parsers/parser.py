from bs4 import BeautifulSoup
import requests
import json

base_url = "https://dou.ua/"


class PostCard:
    def __init__(self, title, link, date, views, info):
        self.title = title
        self.link = link
        self.date = date
        self.views = views
        self.info = info

    def __str__(self):
        return "PostCard(\ntitle: {0} \nlink: {1} \ndate: {2})".format(self.title,
                                                                       self.link,
                                                                       self.date)

    def toJSON(self):
        return json.dumps(self.__dict__)


def parse_postcards():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0"}
    res = requests.get(base_url + "/lenta/", headers=headers)
    bs = BeautifulSoup(res.text, "html.parser")
    # cards = bs.select(".b-postcard")
    headers = bs.select(".b-postcard .title a")
    titles = [title.text.strip() for title in headers]
    links = [header["href"] for header in headers]
    dates = [date.text[:-7] for date in bs.select(".b-info time.date")]
    views_num = [views.text for views in bs.select(".b-info span.pageviews")]
    infos = [info.text for info in bs.select(".b-typo")]
    post_cards = [PostCard(title, link, date, views, info) for (title, link, date, views, info)
                  in zip(titles, links, dates, views_num, infos)]

    return post_cards


# if __name__ == '__main__':
#     cards = parse_postcards()
#     for card in cards:
#         print(card)

