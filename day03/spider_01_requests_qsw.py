import requests
from lxml import etree

class Classifyname(dict):
    pass

class BookItem(dict):
    pass

class ChapterItem(dict):
    pass

def download(url, callback=None):
    resp = requests.request('GET', url)
    resp.encoding = 'gbk'
    if resp.status_code == 200:
        if callback:
            callback(resp.text)
        else:
            parse(resp.text)
    else:
        parse('%s 下载失败' % url)


def parse(html):
    root = etree.HTML(html)
    nav_list = root.xpath('//ul[@class="channel-nav-list"]/li')
    item = Classifyname()
    for nav in nav_list:
        item['name'] = nav.xpath('./a/text()')[0]
        item['books_url'] = nav.xpath('./a/@href')[0]
        itemipelin(item)

        download(item['books_url'], parse_book)

def parse_book(html):
    root = etree.HTML(html)
    seeWell_list = root.xpath('//ul[starts-with(@class, "seeWell")]/li')

    item = BookItem()
    for seeWell_li in seeWell_list:
        item['book_name'] = seeWell_li.xpath('./a/img/@alt')[0]
        item['book_url'] = seeWell_li.xpath('./a/@href')[0]

        itemipelin(item)
        download(item.get('book_url'), parse_deatli)

def parse_deatli(html):
    root = etree.HTML(html)
    chapter_url = root.xpath('.//div[@class="b-oper"]/a/@href')[0]

    download(chapter_url, parse_chapter)

def parse_chapter(html):
    root = etree.HTML(html)
    charpter_list = root.xpath('//div[@class="clearfix dirconone"]/li')
    item = ChapterItem()
    for charpters in charpter_list:
         item['title'] = charpters.xpath('./a/@title')[0]
         item['charpter'] = charpters.xpath('./a/@href')[0]
         # itemipelin(item)



def itemipelin(item):

    if isinstance(item, Classifyname):

        print('--保存分类信息--')
        print(item)

    elif isinstance(item, BookItem):

        print('--保存书信息--')
        print(item)
    else:

        print('--保存章节信息--')
        print(item)

if __name__ == '__main__':
    download('http://www.quanshuwang.com/')