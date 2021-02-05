import requests
import config
import argparse
import sys


def latest_news(feed):
    url = f'http://newsapi.org/v2/everything?q={feed}&apiKey={config.API_KEY}'
    response = requests.get(url)
    if response.json()["status"] == 'ok':
        return response.json()["articles"]


def plot_newsfeed(news):
    for element in news:
        article_title = str(element["title"])
        print(article_title)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('feed', type=str, help="pass the feed that you wanna read news from")
    args = parser.parse_args(sys.argv[1:])
    plot_newsfeed(latest_news(args.feed))
