import time
import json
from collections import dict_keys

import requests
from datetime import datetime
import pandas as pd
import numpy as np
def catch_data():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    reponse = requests.get(url=url).json()
    #返回数据字典
    data = json.loads(reponse['data'])
    return data
data = catch_data()
data.keys()
dict_keys(['chinaTotal', 'chinaAdd', 'lastUpdateTime', 'areaTree', 'chinaDayList', 'chinaDayAddList'])
lastUpdateTime = data['lastUpdateTime']
# 数据明细，数据结构比较复杂，一步一步打印出来看，先明白数据结构
areaTree = data['areaTree']
# 国内数据
china_data = areaTree[0]['children']
china_list = []
for a in range(len(china_data)):
    province = china_data[a]['name']
    province_list = china_data[a]['children']
    for b in range(len(province_list)):
        city = province_list[b]['name']
        total = province_list[b]['total']
        today = province_list[b]['today']
        china_dict = {}
        china_dict['province'] = province
        china_dict['city'] = city
        china_dict['total'] = total
        china_dict['today'] = today
        china_list.append(china_dict)

china_data = pd.DataFrame(china_list)
china_data.head()

# 定义数据处理函数
def confirm(x):
    confirm = eval(str(x))['confirm']
    return confirm
def suspect(x):
    suspect = eval(str(x))['suspect']
    return suspect
def dead(x):
    dead = eval(str(x))['dead']
    return dead
def heal(x):
    heal =  eval(str(x))['heal']
    return heal
# 函数映射
china_data['confirm'] = china_data['total'].map(confirm)
china_data['suspect'] = china_data['total'].map(suspect)
china_data['dead'] = china_data['total'].map(dead)
china_data['heal'] = china_data['total'].map(heal)
china_data['addconfirm'] = china_data['today'].map(confirm)
china_data['addsuspect'] = china_data['today'].map(suspect)
china_data['adddead'] = china_data['today'].map(dead)
china_data['addheal'] = china_data['today'].map(heal)
china_data = china_data[["province","city","confirm","suspect","dead","heal","addconfirm","addsuspect","adddead","addheal"]]
china_data.head()

global_data = pd.DataFrame(data['areaTree'])
global_data['confirm'] = global_data['total'].map(confirm)
global_data['suspect'] = global_data['total'].map(suspect)
global_data['dead'] = global_data['total'].map(dead)
global_data['heal'] = global_data['total'].map(heal)
global_data['addconfirm'] = global_data['today'].map(confirm)
global_data['addsuspect'] = global_data['today'].map(suspect)
global_data['adddead'] = global_data['today'].map(dead)
global_data['addheal'] = global_data['today'].map(heal)
world_name = pd.read_excel("世界各国中英文对照.xlsx")
global_data = pd.merge(global_data,world_name,left_on ="name",right_on = "中文",how="inner")
global_data = global_data[["name","英文","confirm","suspect","dead","heal","addconfirm","addsuspect","adddead","addheal"]]
global_data.head()

chinaDayList = pd.DataFrame(data['chinaDayList'])
chinaDayList = chinaDayList[['date','confirm','suspect','dead','heal']]
chinaDayList.head()

chinaDayAddList = pd.DataFrame(data['chinaDayAddList'])
chinaDayAddList = chinaDayAddList[['date','confirm','suspect','dead','heal']]
chinaDayAddList.head()
