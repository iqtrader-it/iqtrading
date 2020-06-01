import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    r.encoding = 'utf8'
    return r.text


def csv_read(data):
    with open("data.csv", 'a') as file:
        writer = csv.writer(file)
        writer.writerow((data['time'], data['head'], data['link']))


def get_link_head(html):
    soup = BeautifulSoup(html, 'html.parser')
    heads = soup.find('tbody').find_all('tr')
    parser_list = []
    for i in heads:
        if i.find('span', rel="localdatetime") == None:
            time = i.find('div').string
        else:
            time = i.find('span', rel="localdatetime").string
        head = i.find('a').string
        link = 'https://www.finanz.ru' + i.find('a').get('href')

        data = {'time': time,
                'head': (head, link)
                }
        parser_list.append(data)
    return parser_list

        # print(data['time'], data['head'], data['link'])

        # csv_read(data)


# start = get_link_head(get_html('https://www.finanz.ru/novosti'))

def get_link_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find('div', class_='content').find('div', class_='news_text').find_all('p')
    parser_content = ''
    for i in content:
        try:
            block = i.find('p').text
            parser_content += block
        except:
            continue
    return parser_content
