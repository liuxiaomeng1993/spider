from  urllib.request import urlopen, Request
from request import get
import json

BASE_URL = 'http://114.116.238.223'

def query_index(index_name):
    url = BASE_URL + '/' + index_name
    resp = get(url)
    if resp.code == 200:
        return resp.read().decode('utf-8')
    else:
        return 400

def add_index(index_name):
    url = BASE_URL + '/' + index_name
    params = {
        "settings": {
            "number_of_shards": 5,
            "number_of_replicas": 1
        }
    }

    # PUT
    resp = urlopen(Request(url,
                           json.dumps(params).encode('utf-8'),
                           headers={
                               'Content-Type': 'application/json'
                           }, method='PUT'))
    if resp.code == 200:
        return resp.read().decode('utf-8')
    else:
        return 400

def add_info(index_name, type_name,  document, id=None):
    url = BASE_URL + '/' + index_name + "/" + type_name + "/"
    if id:
        url += str(id)

    resp = urlopen(Request(url,
                            json.dumps( document).encode('utf-8'),
                            {
                                'Content-Type': 'application/json'
                            }))
    print(resp.read().decode('utf-8'))

if __name__ == '__main__':


        add_info('mado', 'm',  document={
            'name': '小王',
            'age':19
        })



