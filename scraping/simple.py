import requests
from bs4 import BeautifulSoup
from functools import reduce

url_list = {
    '2015':'https://pycon.jp/2015/ja/sponsors/',
    '2016':'https://pycon.jp/2016/ja/sponsors/',
    '2017':'https://pycon.jp/2017/ja/sponsors/'
}

def scraping(url):
    res = requests.get(url)
    content = res.content
    soup = BeautifulSoup(content, 'html.parser')
    sponsors = soup.find_all('div', class_='sponsor-content')
    return { sponsor.h4.text for sponsor in sponsors}

def main():
    sponser_list = [ scraping(url) for url in url_list.values() ]

    print(reduce(lambda a, b: a&b, sponser_list))

if __name__ == '__main__':
    main()