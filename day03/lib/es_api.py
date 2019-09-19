import json

import requests

BASE_URL = 'http://114.116.238.223'


def add_index(index_name):
    url = BASE_URL + '/' + index_name
    params = {
        "settings": {
            "number_of_shards": 5,
            "number_of_replicas": 1
        }
    }

    # PUT
    resp = requests.put(url,
                           json.dumps(params).encode('utf-8'),
                           headers={
                               'Content-Type': 'application/json'
                           })
    return True

def remove_index(index_name):
    resp = requests.delete(f'{BASE_URL}/{index_name}')
    ret = resp.json()
    return ret['acknowledged']





if __name__ == '__main__':
    print(add_index('books'))
    # print(remove_index('books'))



