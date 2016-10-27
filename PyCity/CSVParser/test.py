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
avg_speed_motor = Helper.avg_speed(motor)
min_speed_motor = Helper.min(motor)
max_speed_motor = Helper.max(motor)
motor_data = Helper.feature_list(max_speed_motor,min_speed_motor,avg_speed_motor,'motor')

Bike = Helper.reader(bike_path)
bike = Helper.preprocess(Bike)
avg_speed_bike = Helper.avg_speed(bike)
min_speed_bike = Helper.min(bike)
max_speed_bike = Helper.max(bike)
bike_data = Helper.feature_list(max_speed_bike,min_speed_bike,avg_speed_bike,'bike')

Run = Helper.reader(run_path)
run = Helper.preprocess(Run)
avg_speed_run = Helper.avg_speed(run)
min_speed_run = Helper.min(run)
max_speed_run = Helper.max(run)
run_data = Helper.feature_list(max_speed_run,min_speed_run,avg_speed_run,'run')

Walk = Helper.reader(walk_path)
walk = Helper.preprocess(Walk)
avg_speed_walk = Helper.avg_speed(walk)
min_speed_walk = Helper.min(walk)
max_speed_walk = Helper.max(walk)
walk_data = Helper.feature_list(max_speed_walk,min_speed_walk,avg_speed_walk,'walk')

train_data = car_data.data[10:] + motor_data.data[10:]
train_target = car_data.target[10:] + motor_data.target[10:]

test_data = car_data.data[:10] + motor_data.data[:10]

# dt = tree.DecisionTreeClassifier()
# dt = dt.fit(train_data,train_target)
# print(dt.predict(test_data))

rbf = RandomForestClassifier(n_estimators=10)
rbf = rbf.fit(train_data, train_target)
print(rbf.predict(test_data))
# gnb = GaussianNB()
# gnb = gnb.fit(train_data, train_target)

# print(gnb.predict(test_data))