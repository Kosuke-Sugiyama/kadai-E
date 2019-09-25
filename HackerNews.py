import requests
import time


def main():
    for i in range(10):
        time.sleep(1)  # ここで1秒止まる

    search_URL = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    r = requests.get(search_URL)
    news_list = r.json()[0:5]
    # news_list = [21064942, 21067487, 21064911, 21062180, 21066385]

    for news_id in news_list:
        news_dict = {}
        article_URL = f"https://hacker-news.firebaseio.com/v0/item/{news_id}.json?print=pretty"
        request = requests.get(article_URL)
        news_dict['title'] = request.json()["title"]
        news_dict['url'] = request.json()["url"]
        print(news_dict)


if __name__ == '__main__':
    main()
