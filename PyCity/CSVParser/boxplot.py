import csv
import numpy as np
import plotly.graph_objs as go
import plotly.plotly as py
import plotly
from CSVParser.Helper import Helper

plotly.offline.init_notebook_mode()
Helper = Helper()
# plotly.tools.set_credentials_file(username='aetdevinz', api_key='p5gx4csvk1')

car_path = 'C:\\Users\Phatthanaphong\Desktop\City\PyCity\Data\Car.csv'
motor_path = 'C:\\Users\Phatthanaphong\Desktop\City\PyCity\Data\Motorcycle.csv'
bike_path = 'C:\\Users\Phatthanaphong\Desktop\City\PyCity\Data\Bicycle.csv'
run_path = 'C:\\Users\Phatthanaphong\Desktop\City\PyCity\Data\Run.csv'
walk_path = 'C:\\Users\Phatthanaphong\Desktop\City\PyCity\Data\Walk.csv'

# car_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Car.csv'
# motor_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Motorcycle.csv'
# bike_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Bicycle.csv'
# run_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Run.csv'
# walk_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Walk.csv'
# path = 'C:\\Users\Phatthanaphong\Desktop\City\PyCity\Data\Car.csv'
data = []

Car = Helper.reader(car_path)
car_speed =[]
for car in Car:
    speed = [float(s['speed']) for s in car]
    car_speed.append(speed)


car_plot = go.Box(
    y=car_speed[4],
    name='Car'
)
data.append(car_plot)

Motor = Helper.reader(motor_path)
motor_speed =[]
for motor in Motor:
    speed = [float(s['speed']) for s in motor]
    motor_speed.append(speed)
motor_plot = go.Box(
    y=motor_speed[2],
    name='Motorcycle'
)
data.append(motor_plot)

Bike = Helper.reader(bike_path)
bike_speed =[]
for bike in Bike:
    speed = [float(s['speed']) for s in bike]
    bike_speed.append(speed)
bike_plot = go.Box(
    y=bike_speed[1],
    name='Bike'
)
data.append(bike_plot)

Run = Helper.reader(run_path)
run_speed =[]
for run in Run:
    speed = [float(s['speed']) for s in run]
    run_speed.append(speed)
    run_plot = go.Box(
    y=run_speed[1],
    name='Run'
)
data.append(run_plot)

Walk = Helper.reader(walk_path)
walk_speed =[]
for walk in Walk:
    speed = [float(s['speed']) for s in walk]
    walk_speed.append(speed)
walk_plot = go.Box(
    y=walk_speed[2],
    name='Walk'
)
data.append(walk_plot)

plotly.offline.plot(data, filename='scatter-plot')

