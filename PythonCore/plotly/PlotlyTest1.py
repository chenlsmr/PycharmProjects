import plotly
import plotly.plotly as pl
import plotly.graph_objs as go
import pandas as pd

plotly.tools.set_credentials_file(username='chenlsmr', api_key='CVEfEhEd443jzMUGH8fB')
df = pd.read_csv('jine2019.csv')
y = df['dt'][:-1]
x1 = df['uus'][:-1]
x2 = df['ddl'][:-1]
x3 = df['jine'][:-1]

trace1 = go.Scatter(
    x=y,
    y=x1,
    mode='lines+markers',
    name='用户数'
)
trace2 = go.Scatter(
    x=y,
    y=x2,
    mode='lines',
    name='订单量'
)
trace3 = go.Scatter(
    x=y,
    y=x3,
    mode='markers',
    name='金额',
    xaxis='x',
    yaxis='y2'  # 标注一个y轴
)
data = [trace1, trace2, trace3]
layout = go.Layout(
    yaxis2=dict(anchor='x', overlaying='y', side='right')  # 设置y轴格式
)
fig = go.Figure(data=data, layout=layout)
pl.plot(fig, filename='figure1')