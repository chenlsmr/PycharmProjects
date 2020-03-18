import geopandas
import pandas as pd
import geopandas as gp
import matplotlib.pyplot as plt

province_city = pd.read_csv("F:/rstudy/chinaprovincecity.csv", encoding = 'gb18030')
china_map=gp.GeoDataFrame.from_file("F:/rstudy/bou2_4p.shp", encoding = 'gb18030')
geopandas.geodataframe.GeoDataFrame
china_map.plot(figsize=(20,12))

china_map.plot(column="AREA",figsize=(20,12),cmap="Greens")
china_map=china_map.merge(province_city,left_on='NAME', right_on='province', how='left')

from shapely.geometry import Point
china_map["center"]=gp.GeoSeries([Point(x, y) for x, y in zip(china_map["jd"], china_map["wd"])])
china_map_ploygon=china_map[["AREA","NAME","geometry"]]
china_map_ploygon=china_map_ploygon
china_map_point=china_map[["AREA","NAME","center"]]
china_map_point=china_map_point.set_geometry('center')

#设置相同的投影
china_map_ploygon.crs={'init': 'epsg:3395'}
china_map_point.crs ={'init': 'epsg:3395'}
#地图可视化
base=china_map_ploygon.plot(column="AREA", edgecolor='black',figsize=(20,12),cmap="Greens")
china_map_point.plot(ax=base,marker='o',color='red',markersize=5)
plt.show()
