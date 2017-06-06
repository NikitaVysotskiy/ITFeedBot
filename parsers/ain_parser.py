import parsers.utils as utils
from bs4 import BeautifulSoup
import requests


def parse_postcards():
    res = requests.get(utils.AIN_BASE_URL, headers=utils.USER_AGENT)
    bs = BeautifulSoup(res.text, "html.parser")
    # cards = bs.select(".b-postcard")
    # headers = bs.select(".b-postcard .title a")
    titles = [title.text.strip() for title in bs.select(".item-title")]
    links = [a["href"] for a in bs.select(".item-link")]
    # dates = [date.text[:-7] for date in bs.select(".b-info time.date")]

    views_num = [views.text for views in bs.select(".more-post-info span.views")]
    # infos = [info.text for info in bs.select(".b-typo")]
    post_cards = [utils.PostCard(title, link, views) for (title, link, views)
                  in zip(titles, links, views_num)]

    return post_cards


if __name__ == '__main__':
    cards = parse_postcards()
    print(cards)
    for card in cards:
        print(card)



