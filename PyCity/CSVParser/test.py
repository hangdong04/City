from CSVParser.Helper import Helper
import json
# car_path = 'C:\\Users\Phatthanaphong\Desktop\City\PyCity\Data\Car.csv'
car_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Car.csv'
motor_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Motorcycle.csv'
bike_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Bicycle.csv'
run_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Run.csv'
walk_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Walk.csv'

data = []
Helper = Helper()
Car = Helper.reader(car_path)
car_list =dict()
speed = []
accuracy = []
time = []
zero = []
inn = []
temp = None
temp_t = None
temp_a = None
temp_s = None
for car in Car:
    found = 0
    for idx, val in enumerate(car):
        t = val['time']
        a = val['accuracy']
        s = val['speed']
        if float(s) == 0.0:
            speed.append(s)
            time.append(t)
            accuracy.append(a)
            if found == 1:
                if idx != len(car)-1:
                    del speed[len(speed)-1]
                    del time[len(time) - 1]
                    del accuracy[len(accuracy) - 1]
            found = 1
        else:
            if found == 1:
                speed.append(temp_s)
                time.append(temp_t)
                accuracy.append(temp_a)
            found = 0
            speed.append(s)
            time.append(t)
            accuracy.append(a)
        temp_s = s
        temp_t = t
        temp_a = a

    for idx, val in enumerate(time):
        if idx != 0:
            if temp_t > val:
                del speed[idx]
                del time[idx]
                del accuracy[idx]
            else:
                temp_t = val
        else:
            temp_t = val
    for idx, val in enumerate(accuracy):
        if float(val) > 200:
            del speed[idx]
            del time[idx]
            del accuracy[idx]

    car_list['speed'] = speed
    car_list['time'] = time
    car_list['accuracy'] = accuracy
    data.append(car_list)
    speed = []
    time = []
    accuracy = []
print(data)
