import plotly as py
import plotly.graph_objs as go

pyplt = py.offline.plot
labels = ['产品1', '产品2', '产品3', '产品4', '产品5']
values = [38.7, 15.33, 19.9, 8.6, 17.47]
trace = [go.Pie(labels=labels, values=values)]
layout = go.Layout(
    title='产品比例配比图',
)
fig = go.Figure(data=trace, layout=layout)
pyplt(fig, filename='tmp/1.html')
