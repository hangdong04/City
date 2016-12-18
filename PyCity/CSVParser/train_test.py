from CSVParser.Helper import Helper
import json

from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
# Wndows path

car_path = 'C:\\Users\Phatt\Desktop\City\PyCity\Data\Car.csv'
motor_path = 'C:\\Users\Phatt\Desktop\City\PyCity\Data\Motorcycle.csv'
bike_path = 'C:\\Users\Phatt\Desktop\City\PyCity\Data\Bicycle.csv'
run_path = 'C:\\Users\Phatt\Desktop\City\PyCity\Data\Run.csv'
walk_path = 'C:\\Users\Phatt\Desktop\City\PyCity\Data\Walk.csv'
# Linux path
# car_path = '/home/aaa/Desktop/City/PyCity/Data/Car.csv'
# motor_path = '/home/aaa/Desktop/City/PyCity/Data/Motorcycle.csv'
# bike_path = '/home/aaa/Desktop/City/PyCity/Data/Bicycle.csv'
# run_path = '/home/aaa/Desktop/City/PyCity/Data/Run.csv'
# walk_path = '/home/aaa/Desktop/City/PyCity/Data/Walk.csv'
Helper = Helper()

Car = Helper.reader(car_path)
car = Helper.preprocess(Car)
avg_speed_car = Helper.avg_speed(car)
std_speed_car = Helper.std(car)
avg_speed_car_nozero = Helper.avg_speed_nozero(car)
max_speed_car = Helper.max(car)

car_data = Helper.feature_list(max_speed_car,std_speed_car,avg_speed_car,avg_speed_car_nozero,'car')


Motor = Helper.reader(motor_path)
motor = Helper.preprocess(Motor)
avg_speed_motor = Helper.avg_speed(motor)
avg_speed_motor_nz = Helper.avg_speed_nozero(motor)
std_speed_car = Helper.std(motor)
max_speed_motor = Helper.max(motor)
motor_data = Helper.feature_list(max_speed_motor,std_speed_car,avg_speed_motor,avg_speed_motor_nz,'motor')
motor_data.data = 2*motor_data.data
motor_data.target = 2*motor_data.target


Bike = Helper.reader(bike_path)
bike = Helper.preprocess(Bike)
avg_speed_bike = Helper.avg_speed(bike)
avg_speed_bike_nz = Helper.avg_speed_nozero(bike)
max_speed_bike = Helper.max(bike)
std_speed_bike = Helper.std(bike)
bike_data = Helper.feature_list(max_speed_bike,std_speed_bike,avg_speed_bike,avg_speed_bike_nz,'bike')
bike_data.data = 34*bike_data.data
bike_data.target = 34*bike_data.target


Run = Helper.reader(run_path)
run = Helper.preprocess(Run)
avg_speed_run = Helper.avg_speed(run)
avg_speed_run_nz = Helper.avg_speed_nozero(run)
max_speed_run = Helper.max(run)
std_speed_run = Helper.std(run)
run_data = Helper.feature_list(max_speed_run,std_speed_run,avg_speed_run,avg_speed_run_nz,'run')
run_data.data = 50*run_data.data
run_data.target = 50*run_data.target


Walk = Helper.reader(walk_path)
walk = Helper.preprocess(Walk)
avg_speed_walk = Helper.avg_speed(walk)
avg_speed_walk_nz = Helper.avg_speed_nozero(walk)
std_speed_walk = Helper.std(walk)
max_speed_walk = Helper.max(walk)
walk_data = Helper.feature_list(max_speed_walk,std_speed_walk,avg_speed_walk, avg_speed_walk_nz,'walk')
walk_data.data = 5*walk_data.data
walk_data.target = 5*walk_data.target

print(walk_data.data[:4])
print(walk_data.data[3:4])

train_data = car_data.data[:80] + motor_data.data[:80] + walk_data.data[:80] + bike_data.data[:80] + run_data.data[:80]
train_target = car_data.target[:80] + motor_data.target[:80] + walk_data.target[:80] + bike_data.target[:80] + run_data.data[:80]
print(len(train_data))
print(len(train_target))
test_data = car_data.data[80:100] + motor_data.data[80:100] + walk_data.data[80:100] + bike_data.data[80:100] + run_data.data[80:100]


print(len(test_data))

dt = tree.DecisionTreeClassifier()
dt = dt.fit(train_data, train_target)
print(dt.predict(test_data))
#
# rbf = RandomForestClassifier(n_estimators=10)
# rbf = rbf.fit(train_data, train_target)
# print(rbf.predict(test_data))
#
# gnb = GaussianNB()
# gnb = gnb.fit(train_data, train_target)
#
# print(gnb.predict(test_data))
#
# nclf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1)
# nclf.fit(train_data,train_target)
# print(nclf.predict(test_data))