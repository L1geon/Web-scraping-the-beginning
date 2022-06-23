import requests
import bs4
from fake_headers import Headers

headers = Headers(os="mac", headers=True).generate()
KEYWORDS = ['дизайн', 'фото', 'web', 'python']
URL = "https://habr.com/ru/all/"
def main():
    response = requests.get(URL, headers=headers)
    data = response.text
    soup = bs4.BeautifulSoup(data, features="html.parser")
    articles = soup.findAll("article")
    result = {}
    for article in articles:
        news_id = article.attrs["id"]
        time_pub = article.find(class_="tm-article-snippet__datetime-published").text
        link = article.find(class_="tm-article-snippet__title-link").attrs["href"]
        a_name = article.find(class_="tm-article-snippet__title-link").find("span").text
        text = article.find(class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
        if text == None:
            text = article.find(class_="article-formatted-body article-formatted-body article-formatted-body_version-1")
        _text = text.text
        hub = article.find(class_="tm-article-snippet__hubs").text
        for word in KEYWORDS:
            r_name = a_name.find(word)
            r_hub = hub.find(word)
            r_text = _text.find(word)
            result_1 = []
            if r_name != -1 or r_hub != -1 or r_text != -1:
                result_1 = [time_pub, a_name, f"https://habr.com{link}"]
                if news_id in result.keys():
                    pass
                result[news_id] = result_1

    for value in result.values():
        print(f"{value[0]} - {value[1]} - {value[2]}")


if __name__ == "__main__":
    main()
