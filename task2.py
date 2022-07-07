import requests
import lxml.html


animals_file = open("Категории животных.txt", "w+")
url = 'http://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
resp = requests.get(url)
dict_animals_amount = {}


def add_data(resp):
    doc = lxml.html.document_fromstring(resp.text)
    links = doc.xpath('//*[@id="mw-pages"]/div/div/div/ul/li[a]/a')
    with open("Категории животных.txt", "a", encoding="utf-8") as f:
        for link in links:
            name = link.get('title')
            first_let = name[0]
            if 1040 <= ord(first_let) <= 1071:
                f.write(name + '\n')


def some_funk(resp):
    doc = lxml.html.document_fromstring(resp.text)
    links = doc.xpath('//*[@id="mw-pages"]/a[2]')
    for a in links:
        name = a.get('href')
        if a.text == 'Следующая страница':
            url = 'https://ru.wikipedia.org/' + name
            resp = requests.get(url)
            add_data(resp)
            some_funk(resp)


add_data(resp)
some_funk(resp)

with open("Категории животных.txt", encoding="utf8") as file:
    for line in file.readlines():
        if line[0] not in dict_animals_amount:
            dict_animals_amount[line[0]] = 1
        else:
            dict_animals_amount[line[0]] += 1


for name in sorted(dict_animals_amount):
    print(f'{name}: {dict_animals_amount[name]}')
