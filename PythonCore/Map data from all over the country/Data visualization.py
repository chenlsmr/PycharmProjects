from pyecharts.charts import * #导入所有图表
from pyecharts import options as opts
#导入pyecharts的主题（如果不使用可以跳过）
from pyecharts.globals import ThemeType
total_pie = Pie(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS,width = '500px',height ='350px'))  #设置主题，和画布大小
total_pie.add("",[list(z) for z in zip(chinaTotal.keys(), chinaTotal.values())],
            center=["50%", "50%"], #图的位置
            radius=[50, 80])   #内外径大小
total_pie.set_global_opts(
            title_opts=opts.TitleOpts(title="全国总量",subtitle=("截止"+lastUpdateTime)))
total_pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{c}"))  #标签格式
total_pie.render_notebook()
totaladd_pie = Pie(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS,width = '500px',height ='350px'))  #设置主题，和画布大小
totaladd_pie.add("",[list(z) for z in zip(chinaAdd.keys(), chinaAdd.values())],
            center=["50%", "50%"],
            radius=[50, 80])
totaladd_pie.set_global_opts(
            title_opts=opts.TitleOpts(title="昨日新增"))
totaladd_pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{c}"))  #标签格式
totaladd_pie.render_notebook()
#<div id = "e7f89ced2eee4f72aabf78c05ab56dc1" style = "width:500px; height:350px;" ></div>
world_map = Map(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS))
world_map.add("",[list(z) for z in zip(list(global_data["英文"]), list(global_data["confirm"]))], "world",is_map_symbol_show=False)
world_map.set_global_opts(title_opts=opts.TitleOpts(title="2019_nCoV-世界疫情地图"),
                          visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                          pieces = [
                        {"min": 101 , "label": '>100'}, #不指定 max，表示 max 为无限大
                        {"min": 10, "max": 100, "label": '10-100'},
                        {"min": 0, "max": 9, "label": '0-9' }]))
world_map.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
world_map.render_notebook()

#数据处理
area_data = china_data.groupby("province")["confirm"].sum().reset_index()
area_data.columns = ["province","confirm"]

area_map = Map(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS))
area_map.add("",[list(z) for z in zip(list(area_data["province"]), list(area_data["confirm"]))], "china",is_map_symbol_show=False)
area_map.set_global_opts(title_opts=opts.TitleOpts(title="2019_nCoV中国疫情地图"),visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                pieces = [
                        {"min": 1001 , "label": '>1000',"color": "#893448"}, #不指定 max，表示 max 为无限大
                        {"min": 500, "max": 1000, "label": '500-1000',"color": "#ff585e"},
                        {"min": 101, "max": 499, "label": '101-499',"color": "#fb8146"},
                        {"min": 10, "max": 100, "label": '10-100',"color": "#ffb248"},
                        {"min": 0, "max": 9, "label": '0-9',"color" : "#fff2d1" }]))
area_map.render_notebook()
#<div id = "4afca4394dc74d64aa320c7831ca4bd1" style = "width:900px; height:500px;"></div>

line1 = Line(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS))
line1.add_xaxis(list(chinaDayList["date"]))
line1.add_yaxis("治愈",list(chinaDayList["heal"]),is_smooth=True)
line1.add_yaxis("死亡", list(chinaDayList["dead"]),is_smooth=True)
line1.set_global_opts(title_opts=opts.TitleOpts(title="Line1-治愈与死亡趋势"))
line1.render_notebook()
line2 = Line(init_opts=opts.InitOpts(theme=ThemeType.SHINE))
line2.add_xaxis(list(chinaDayList["date"]))
line2.add_yaxis("确诊",list(chinaDayList["confirm"]))
line2.add_yaxis("疑似", list(chinaDayList["suspect"]))
line2.set_global_opts(title_opts=opts.TitleOpts(title="Line2-确诊与疑似趋势"))
line2.render_notebook()
#<div id = "70d5c115f4344fffa84cf3aec7357c6a"style = "width:900px; height:500px;"></div>
bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS,width = '900px',height ='400px'))
bar .add_xaxis(list(chinaDayAddList["date"]))
bar .add_yaxis("确诊", list(chinaDayAddList["confirm"]))
bar .add_yaxis("疑似", list(chinaDayAddList["suspect"]))
bar .add_yaxis("死亡", list(chinaDayAddList["dead"]))
bar .add_yaxis("治愈", list(chinaDayAddList["heal"]))
bar .set_global_opts(title_opts=opts.TitleOpts(title="每日新增数据趋势"))
bar.render_notebook()
#<div id = "f361d22988f248c3a8dccd9da4c05962" style="width:900px; height:400px;"></div>

