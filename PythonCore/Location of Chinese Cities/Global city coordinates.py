import datetime,time,json,requests

data = requests.get('https://geo.datav.aliyun.com/areas/bound/100000_full.json')
data=data.json()
provinces=[]
adcodes=[]
for item in data['features']:
    # print(item)
    if item['properties']['name']:
        province_item = {
            "name":item['properties']['name'],
            "adcode":item['properties']['adcode'],
            "geo":item['properties']['center']
        }
        # print(province_item)
        provinces.append(province_item)


for item in provinces:
    item['city']=[]
    data = requests.get('https://geo.datav.aliyun.com/areas/bound/%s_full.json'%item['adcode'])
    data = data.json()
    for city in data['features']:
        if city['properties']['name']:
            city_item = {
                "name": city['properties']['name'],
                "adcode": city['properties']['adcode'],
                "geo": city['properties']['center']
            }
            # print(city_item)
            item['city'].append(city_item)


for province in provinces:
    for city in province['city']:
        city['district']=[]
        data = requests.get('https://geo.datav.aliyun.com/areas/bound/%s_full.json'%city['adcode'])
        if data.status_code==200:
            data = data.json()
            if data:
                for district in data['features']:
                    if district['properties']['name']:
                        district_item={
                            "name": district['properties']['name'],
                            "adcode": district['properties']['adcode'],
                            "geo": district['properties']['center']
                        }
                        # print(district_item)
                        city['district'].append(district_item)

all_address={}
for province in provinces:
    all_address[province['name']]=province['geo']
    for city in province['city']:
        all_address[city['name']]=city['geo']
        for district in city['district']:
            all_address[district['name']]=district['geo']

print(all_address)
