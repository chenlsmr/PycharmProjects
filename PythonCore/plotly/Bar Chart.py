#Bar Chart
#Mean house values by Bedrooms type and year
import plotly.graph_objs as go
import plotly.plotly as py
trace1 = go.Bar(
    x = df_groupby_datebr.index.values,
    y = df_groupby_datebr.ZHVI_1bedroom,
    name = "ZHVI_1bedroom",
    marker = dict(color = 'rgb(102,255,255)'),
    text = df_groupby_datebr['ZHVI_1bedroom'])
trace2 = go.Bar(
    x = df_groupby_datebr.index.values,
    y = df_groupby_datebr.ZHVI_2bedroom,
    name = "ZHVI_2bedroom",
    marker = dict(color = 'rgb(102,178,255)'),
    text = df_groupby_datebr['ZHVI_2bedroom'])
trace3 = go.Bar(
    x = df_groupby_datebr.index.values,
    y = df_groupby_datebr.ZHVI_3bedroom.values,
    name = "ZHVI_3bedroom",
    marker = dict(color = 'rgb(102,102,255)'),
    text = df_groupby_datebr['ZHVI_3bedroom'])
trace4 = go.Bar(
    x = df_groupby_datebr.index.values,
    y = df_groupby_datebr.ZHVI_4bedroom.values,
    name = "ZHVI_4bedroom",
    marker = dict(color = 'rgb(178, 102, 255)'),
    text = df_groupby_datebr['ZHVI_4bedroom'])
trace5 = go.Bar(
    x = df_groupby_datebr.index.values,
    y = df_groupby_datebr.ZHVI_5BedroomOrMore.values,
    name = "ZHVI_5BedroomOrMore",
    marker = dict(color = 'rgb(255, 102, 255)'),
    text = df_groupby_datebr['ZHVI_5BedroomOrMore'])
data = [trace1, trace2, trace3, trace4, trace5]
layout = go.Layout(barmode = "group", title="Bar Chart: Mean House Values by Bedrooms and Year",
                   xaxis= dict(title= 'Year',ticklen= 5,zeroline= False),
                   yaxis= dict(title= 'Mean House Values',ticklen= 5,zeroline= False))
fig = go.Figure(data = data, layout = layout)
url = py.plot(fig, validate=False)