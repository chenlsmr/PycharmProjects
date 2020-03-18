##在线使用
import plotly.plotly as py
from plotly import tools
from plotly.graph_objs import *
plotly.tools.set_credentials_file(username='chenlsmr', api_key='wpRt7sIBRnQ8g1rqPt0b')
trace0 = Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17],
    mode='markers'
)
trace1 = Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = Data([trace0, trace1])

py.iplot(data)