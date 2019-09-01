import requests
from bs4 import BeautifulSoup

url_list = {
    '2015':'https://pycon.jp/2015/ja/sponsors/',
    '2016':'https://pycon.jp/2016/ja/sponsors/',
    '2017':'https://pycon.jp/2017/ja/sponsors/'
}

def scraping(url, year):
    res = requests.get(url)
    content = res.content
    soup = BeautifulSoup(content, 'html.parser')
    sponsors = soup.find_all('div', class_='sponsor-content')
    sponser_list = set()
    for sponsor in sponsors:
        name = sponsor.h4.text
        sponser_list.add(name)
    return sponser_list

def main():
    sponser_set = {}
    for year in url_list:
        print(year)

        sponser_set[year] = scraping(url_list[year], year)

    print(sponser_set['2015'] & sponser_set['2016'] & sponser_set['2017'])


if __name__ == '__main__':
    main()