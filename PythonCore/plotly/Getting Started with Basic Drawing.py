import numpy as np
import pandas as pd
import plotly.plotly as py
import plotly
import plotly.graph_objs as gp

rand_x = np.random.randn(1000)
rand_y = np.random.randn(1000)
#plotly.tools.set_credentials_file(username='user_name', api_key='KC2kwJWZXjfSJ65bhCvc')
#plotly也会有比较坑的地方，比如你要注册账户生成apikey,使用前必须写。
plotly.tools.set_credentials_file(username='chenlsmr', api_key='drXlI0IxjLOl3YFBdfT2')
# 生成一个trace，要求有x,y,绘图模式
trace = gp.Scatter(
    x=rand_x,
    y=rand_y,
    mode='markers'
)
data = [trace]
ts = py.plot(data, filename='basic-scatter')