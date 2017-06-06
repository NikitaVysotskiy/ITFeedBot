import requests
from bs4 import BeautifulSoup
import parsers.utils as utils


def parse_postcards():

    res = requests.get(utils.DOU_BASE_URL + "/lenta/", headers=utils.USER_AGENT)
    bs = BeautifulSoup(res.text, "html.parser")
    # cards = bs.select(".b-postcard")
    headers = bs.select(".b-postcard .title a")
    titles = [title.text.strip() for title in headers]
    links = [header["href"] for header in headers]
    dates = [date.text[:-7] for date in bs.select(".b-info time.date")]
    views_num = [views.text for views in bs.select(".b-info span.pageviews")]
    infos = [info.text for info in bs.select(".b-typo")]
    post_cards = [utils.PostCard(title, link, views, info, date) for (title, link, views, info, date)
                  in zip(titles, links, views_num, infos, dates)]

    return post_cards


if __name__ == '__main__':
    cards = parse_postcards()
    for card in cards:
        print(card)

