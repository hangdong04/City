from CSVParser.Helper import Helper
import plotly.graph_objs as go
import plotly
plotly.offline.init_notebook_mode()

car_path = 'C:\\Users\Phatthanaphong\Desktop\City\PyCity\Data\Car.csv'
motor_path = 'C:\\Users\Phatthanaphong\Desktop\City\PyCity\Data\Motorcycle.csv'
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
data1 = [trace1]
# plotly.offline.plot(data, filename='car-speed')
# plotly.offline.plot(data1, filename='motor-speed')
# avg_speed_car = Helper.avg_speed(car)
# avg_speed_car_nZ = Helper.avg_speed_nozero(car)
# min_speed_car = Helper.min(car)
# max_speed_car = Helper.max(car)

