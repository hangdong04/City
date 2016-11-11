from CSVParser.Helper import Helper
import plotly.graph_objs as go
import plotly
plotly.offline.init_notebook_mode()
# car_path = 'C:\\Users\Phatthanaphong\Desktop\City\PyCity\Data\Car.csv'
# motor_path = 'C:\\Users\Phatthanaphong\Desktop\City\PyCity\Data\Motorcycle.csv'
# bike_path = 'C:\\Users\Phatthanaphong\Desktop\City\PyCity\Data\Bicycle.csv'
# run_path = 'C:\\Users\Phatthanaphong\Desktop\City\PyCity\Data\Run.csv'
# walk_path = 'C:\\Users\Phatthanaphong\Desktop\City\PyCity\Data\Walk.csv'
# Linux path
car_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Car.csv'
motor_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Motorcycle.csv'
bike_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Bicycle.csv'
run_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Run.csv'
walk_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Walk.csv'

Helper = Helper()

Car = Helper.reader(car_path)
car = Helper.preprocess(Car)
avg_speed_car = Helper.avg_speed(car)
avg_speed_car_nz = Helper.avg_speed_nozero(car)
max_speed_car = Helper.max(car)

Motor = Helper.reader(motor_path)
motor = Helper.preprocess(Motor)
avg_speed_motor = Helper.avg_speed(motor)
avg_speed_motor_nz = Helper.avg_speed_nozero(motor)
max_speed_motor = Helper.max(motor)

# CAR
trace = go.Scatter(
    y = avg_speed_car_nz,
    name = 'remove stop point',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4)
)

trace1 = go.Scatter(
    y = avg_speed_car,
    name = 'all point',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4)
)
data = [trace, trace1]
layout = dict(title = 'Average Speed of Car',
              xaxis = dict(title = 'Trip'),
              yaxis = dict(title = 'Average Speed (km/hr)'),
              )
fig = dict(data = data, layout = layout)
plotly.offline.plot(fig, filename='car-avg-speed')

#Motor
trace2 = go.Scatter(
    y = avg_speed_motor_nz,
    name = 'remove stop point',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4)
)

trace3 = go.Scatter(
    y = avg_speed_motor,
    name = 'all point',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4)
)
data1 = [trace2, trace3]
layout1 = dict(title = 'Average Speed of Motorcycle',
              xaxis = dict(title = 'Trip'),
              yaxis = dict(title = 'Average Speed (km/hr)'),
              )
fig1 = dict(data = data1, layout = layout1)
plotly.offline.plot(fig1, filename='motor-avg-speed')

