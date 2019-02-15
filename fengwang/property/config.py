#-*-coding=utf-8 -*-

import json

import getToken

#[服务器地址]

#url = "http://open-get.hivescm.com"
url = "http://open-gateway.beescm.cn:10030"
#url = "http://pre-open-gateway.newbeescm.com"
#url = "http://open-gateway.newbeescm.com"

#开发环境  open-gateway.hivescm.com
#测试环境  open-gateway.beescm.cn
#预发环境  pre-open-gateway.newbeescm.com
#线上环境  open-gateway.newbeescm.com

#[HEADER参数]

api_v = ("v1.0", "memberFind")

#[BODY参数]

with open("requestBody.data","r") as f:
    ff = f.read()
ff = json.loads(ff)

#测试
akey = "067bcef3f5a347e1ad4972d1081261a9"
asecret = "ea1724eccafc41689f9c785bb0960acf"

#[获取accessToken的应用]

aToken = getToken.login()
