import requests
from bs4 import BeautifulSoup as BS
import csv
def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    response = requests.get(url, headers=headers)
    return response.text

def get_soup(html):
    soup = BS(html , 'lxml')
    return soup
def get_last_page(soup):
    p = soup.find('ul',class_='pagination__list')
    page = p.find_all('li')[-2]
    print(page.text)
def get_data(soup):
    toys = soup.find_all('div',class_='hit__slide')
    for toy in toys:
        try:
            title = toy.find('h6',class_='hit__slide__title').text
        except:
            title = ''
        try:
            price = toy.find('span',class_='hit__slide__price').text
        except:
            price = ''
        try:
            image = toy.find('img').get('src')
            image = 'https://www.gadget.kg/'+ image
        except:
            image = ''
        data = {
    'title':title,
    'price':price,
    'image':image
}       

        write_to_csv(data)



def write_to_csv(data):
    with open('toys.csv','a') as file:
        fieldnames = ['title','price','image']
        writer = csv.DictWriter(file,delimiter=',',fieldnames = fieldnames)
        writer.writerow(data)

def main():
    BASE_URL = 'https://www.gadget.kg/catalog/gadzhety/gadzhety-dlya-mobilnyh/'
    count = 1
    while True:
        url = f'{BASE_URL}?page={count}'
        html = get_html(url)
        soup = get_soup(html)
        last_page = get_last_page(soup)
        print(f'Страницы {count} / Последняя страниц {last_page}')
        get_data(soup)
        if not is_next(soup) or count > int(last_page):
            break
        count += 1

main()

# html = get_html('https://www.gadget.kg/catalog/games/igry-igrushki-razvlecheniya')
# soup = get_soup(html)
# is_next(soup)