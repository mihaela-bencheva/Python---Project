import requests
from bs4 import BeautifulSoup

scrape_url = "https://dama.bg/horoscope/"

def enterDataType():
    type_of_data = input("Enter what type of data you'd like to see (only valid html tag's name is excepted): ")
    return type_of_data

def scrapeDataFromUrlByConcreteDataType(scrape_url):
    dataType = enterDataType()

    if dataType == '':
        dataType = enterDataType()

    req = requests.get(scrape_url)
    req.encoding = 'utf-8'

    if req.status_code == "404":
        return 'The page is not found.'

    soup = BeautifulSoup(req.text, 'html.parser')
    scraped_data = soup.find_all(dataType)

    if not scraped_data:
        scraped_data = soup.find_all('a')

    link_dict = {}

    index = 0
    for data in scraped_data:
        if dataType == 'a':
            link_dict[index] = {'href': data.attrs.get('href', ''),
                                'text': data.get_text()}
        elif dataType == 'img':
            link_dict[index] = {'src': data.attrs.get('src', ''),
                                'alt':data.attrs.get('alt', ''),
                                'text': data.get_text()}
        else:
            link_dict[index] = {'text': data.get_text()}

        index = index + 1

    return link_dict


if __name__ == '__main__':
    scraped_datas = scrapeDataFromUrlByConcreteDataType(scrape_url)

    print(scraped_datas)

