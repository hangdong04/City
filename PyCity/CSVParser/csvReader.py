import csv
import numpy as np
import plotly.graph_objs as go
import plotly.plotly as py
import plotly

plotly.offline.init_notebook_mode()
# plotly.offline.plot()
# plotly.offline.iplot()
# plotly.tools.set_credentials_file(username='aetdevinz', api_key='p5gx4csvk1')

Car = []
each_pos = []
with open('/home/phatthanapong/Desktop/City/PyCity/Data/Car.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    ind = 1
    for row in reader:

        if int(row["num"]) > ind:
            ind = int(row["num"])
            Car.append(each_pos)
            each_pos = []
            temp = {k: row[k] for k in row.keys() & {'latitude', 'longitude', 'speed', 'bering', 'time', 'accuracy'}}
            each_pos.append(temp)
        else:
            temp = {k: row[k] for k in row.keys() & {'latitude', 'longitude', 'speed', 'bering', 'time', 'accuracy'}}
            each_pos.append(temp)
list_speed =[]
for car in Car:
    speed = [float(s['speed']) for s in car]
    list_speed.append(speed)
ind = 1
data = []
for each_speed in list_speed:
    ind += 1
    trip = go.Scatter(
        y=each_speed,
        mode='markers',
        marker=dict(
            size='8',
            color='rgba(100+ind, 0, 0, .8)',
            colorscale='Viridis'
        )
    )
    data.append(trip)


# list_speed = [float(d['speed']) for d in Car[0]]
#
# list_range = list(range(1, 100))
# trace1 = go.Scatter(
#     y = list_speed,
#     mode='markers',
#     marker=dict(
#         size='8',
#         color='rgba(100, 0, 0, .8)',
#         colorscale='Viridis'
#     )
# )
# data = [trace1]

# py.iplot(data, filename='scatter-plot')
plotly.offline.plot(data, filename='scatter-plot')




# trace1 = go.Scatter(
#     y = np.random.randn(500),
#     mode='markers',
#     marker=dict(
#         size='16',
#         color = np.random.randn(500), #set color equal to a variable
#         colorscale='Viridis',
#         showscale=True
#     )
# )
# data = [trace1]
# plotly.offline.plot(data, filename='scatter-plot-with-colorscale')
# py.iplot(data, filename='scatter-plot-with-colorscale')


# plotly.offline.plot({
#     "data": [go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
#     "layout": go.Layout(title="hello world")
# })
