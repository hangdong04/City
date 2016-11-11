from CSVParser.Helper import Helper
import json

from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
# Wndows path
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
min_speed_car = Helper.min(car)
max_speed_car = Helper.max(car)
car_data = Helper.feature_list(max_speed_car,min_speed_car,avg_speed_car,'car')

Motor = Helper.reader(motor_path)
motor = Helper.preprocess(Motor)
std_speed_m = Helper.std(motor)

trace0 = go.Scatter(
    y = std_speed,
    mode = 'markers',
    name = 'car',
    line=dict(
        color=('rgb(205, 12, 24)'),
        width=6)
)

trace1 = go.Scatter(
    y = std_speed_m,
    mode = 'markers',
    name = 'motorcycle',
    line = dict(
        color=('rgb(22, 96, 167)'),
        width=6)
)

data = [trace0, trace1]
layout = dict(title = 'Speed standard deviation',
              xaxis = dict(title = 'Trip'),
              yaxis = dict(title = 'STD Speed (km/hr)'),
              )
fig = dict(data = data, layout = layout)
plotly.offline.plot(fig, filename='std-speed')