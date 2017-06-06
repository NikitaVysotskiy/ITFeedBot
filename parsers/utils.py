import json


USER_AGENT = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0"}
DOU_BASE_URL = "https://dou.ua/"
AIN_BASE_URL = "https://ain.ua/"


class PostCard:
    def __init__(self, title, link, views, info=None, date=None):
        self.title = title
        self.link = link
        self.date = date
        self.views = views
        self.info = info

    def __str__(self):
        return "PostCard(\ntitle: {0} \nlink: {1}".format(self.title,
                                                          self.link)

    def toJSON(self):
        return json.dumps(self.__dict__)




