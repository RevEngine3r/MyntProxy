import time

import requests

import PeerMgr as Pm

email = 'hoaxbyte@yandex.ru'
global_api_key = 'd874fa0fbd2ab2dd6be0bf0827a4986c2fb2b'

zone_id = 'ce2b590b7c4fe1d9d880cd9c65ab0c86'
domain_name = 'mynt.uniqsoft.ir'
domain_ids = ['73faa100ae0f8be4615d8892c4a3a0a8',
              '439546f032e803c4b9af2fefb153bc7b',
              'ea2801b64be6114447598c1a0b651c2a',
              '6c13930420a115872a85847da507a5c9',
              'c3f3d06fdaf4ead1552675a9b1cbd9fe']

url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"


def update_mynt_records(ips):
    for __id, __ip in zip(domain_ids, ips):
        __url = f'{url}/{__id}'
        data = f'{{"type":"A","name":"{domain_name}","content":"{__ip}","proxied":false,"ttl":120}}'

        r = requests.put(__url, headers={
            'X-Auth-Email': email,
            'X-Auth-Key': global_api_key,
            'Content-Type': 'application/json'
        }, data=data)
        time.sleep(.5)


def update_mynt():
    Pm.ping_sort()
    update_mynt_records(Pm.get_best_5())


"""def mynt_updater():
    while True:
        Pm.ping_sort()

        time.sleep(3 * 60)


def start_mynt_updater_thread():
    threading.Thread(target=mynt_updater).start()"""
