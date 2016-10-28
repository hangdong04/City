from CSVParser.Helper import Helper
import plotly.graph_objs as go
import plotly
plotly.offline.init_notebook_mode()

# car_path = 'C:\\Users\Phatthanaphong\Desktop\City\PyCity\Data\Car.csv'
# motor_path = 'C:\\Users\Phatthanaphong\Desktop\City\PyCity\Data\Motorcycle.csv'

car_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Car.csv'
motor_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Motorcycle.csv'
Helper = Helper()

Car = Helper.reader(car_path)
car = Helper.preprocess(Car)
Motor = Helper.reader(motor_path)
motor = Helper.preprocess(Motor)
# print(car[0].get('speed'))

new_time = Helper.time_rescale(car[0].get('time'))
# print(new_time)

trace0 = go.Scatter(
    y = car[0].get('speed'),
    x = new_time,
    mode = 'lines',
    name = 'lines'
)

trace1 = go.Scatter(
    y = motor[7].get('speed'),
    x = Helper.time_rescale(motor[7].get('time')),
    mode = 'lines',
    name = 'lines'
)

data = [trace0]
layout = dict(title = 'Speed of Car',
              xaxis = dict(title = 'Time (second)'),
              yaxis = dict(title = 'Speed (km/hr)'),
              )
fig = dict(data = data, layout = layout)
plotly.offline.plot(fig, filename='car-speed')

data1 = [trace1]
layout1 = dict(title = 'Speed of Motorcycle',
              xaxis = dict(title = 'Time (second)'),
              yaxis = dict(title = 'Speed (km/hr)'),
              )
fig1 = dict(data = data1, layout = layout1)
plotly.offline.plot(fig1, filename='motor-speed')

trace2 = go.Scatter(
    y = car[0].get('bearing'),
    x = Helper.time_rescale(car[0].get('time')),
    mode = 'lines',
    name = 'lines'
)
data2 = [trace2]
layout2 = dict(title = 'Head Change of Car',
              xaxis = dict(title = 'Time (second)'),
              yaxis = dict(title = 'Head Change Angle (degrees)'),
              )
fig2 = dict(data = data2, layout = layout2)
plotly.offline.plot(fig2, filename='car-hcr')
trace3 = go.Scatter(
    y = motor[7].get('bearing'),
    x = Helper.time_rescale(motor[7].get('time')),
    mode = 'lines',
    name = 'lines'
)
data3 = [trace3]
layout3 = dict(title = 'Head Change of Motorcycle',
              xaxis = dict(title = 'Time (second)'),
              yaxis = dict(title = 'Head Change Angle (degrees)'),
              )
fig3 = dict(data = data2, layout = layout2)
plotly.offline.plot(fig3, filename='motor-hcr')
# avg_speed_car = Helper.avg_speed(car)
# avg_speed_car_nZ = Helper.avg_speed_nozero(car)
# min_speed_car = Helper.min(car)
# max_speed_car = Helper.max(car)

