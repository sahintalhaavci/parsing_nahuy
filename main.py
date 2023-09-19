# import requests
# from bs4 import BeautifulSoup as BS
# import csv

# def get_html(url):
#     response = requests.get(url)
#     return response.text

# def get_soup(html):
#     soup = BS(html , 'lxml')
#     return soup

# def get_data(soup):
#     catalog = soup.find('div',class_ = 'row')
#     products = catalog.find_all('div',class_='product-list')
#     for product in products:
#         info = product.find('div', class_='product-thumb')
#         try:
#             title = info.find('div',class_='caption').find('div',class_='name').text.strip()
#         except:
#             title = ''
#         try:
#             price = info.find('div',class_='caption').find('div',class_='price').text.strip()
#         except:
#             price = ''
#         try:
#             image = info.find('div',class_='image').find('a').find('img').get('data-src')
#         except:
#             image = ''
#         try:
#             desc = info.find('div',class_='caption').find('div',class_='description-small').text.strip()
#         except:
#             desc = ''
        
#         data = {

#             'title':title,
#             'price':price,
#             'image':image
#         }
#         print(data)

# html = get_html('https://softech.kg/braslety-i-chasy')
# soup = get_soup(html)
# get_data(soup)

