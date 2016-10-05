from CSVParser.Helper import Helper
car_path = 'C:\\Users\Phatthanaphong\Desktop\City\PyCity\Data\Car.csv'
# car_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Car.csv'
motor_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Motorcycle.csv'
bike_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Bicycle.csv'
run_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Run.csv'
walk_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Walk.csv'

data = []
Helper = Helper()
Car = Helper.reader(car_path)
car_speed =[]
speed = []
accuracy = []
time = []
zero = []
inn = []
temp = None
temp_t = None
for car in Car:
    found = 0
    for idx, val in enumerate(car):
        t = val['time']
        a = val['accuracy']
        s = val['speed']
        time.append(t)
        accuracy.append(a)
        if idx != 0:
            if temp_t > t:
                del time[len(time)-1]
        temp_t = val['time']

        if float(val['accuracy']) > 200:
            del accuracy[len(accuracy)-1]
        if float(s) == 0.0:
            speed.append(s)
            if found == 1:
                if idx != len(car)-1:
                    del speed[len(speed)-1]
                    del time[len(time) - 1]
                    del accuracy[len(accuracy) - 1]
            found = 1
        else:
            if found == 1:
                speed.append(temp)
            found = 0
            speed.append(s)
        temp = s

    print(len(accuracy))
    print(len(time))
    print(len(speed))
    break