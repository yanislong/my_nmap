#!/usr/bin/python

import requests
import config

def getToken():
    url = config.aurl + "/oauth/client/token"
    print url
    header = {}
    data = {}
#    data['appKey'] = "6c0e996c77884798935ef8d52df138de"
#    data['appSecret'] = "dbd6efe436fc40879ee1c242de68d6a8"
#    data['appKey'] = "c816b067600447b6bbc1a59448fbca20"
#    data['appSecret'] = "0463c28cc8e348548b5dff592fbaa851"
#    data['appKey'] = "d8a2ca8b66e84cb5937e7276e573c7b8"
#    data['appSecret'] = "3fe6a45e9f7e4573b33c26564978d49e"
    data['appKey'] = "067bcef3f5a347e1ad4972d1081261a9"
    data['appSecret'] = "ea1724eccafc41689f9c785bb0960acf"
#    data['appKey'] = "ab882e62f2c44fdba5ba985a0f95757f"
#    data['appSecret'] = "5780352d8dfd4442ae9e5eb6f480bc88"
    r = requests.post(url, data=data)
    print r.content
#    print r.json()['result']['access_token']
#    return r.json()['result']['access_token']

if __name__ == "__main__":
    getToken()
