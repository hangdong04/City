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
zero = []
inn = []
temp = None
for car in Car:
    found = 0
    for idx, val in enumerate(car):
        print(len(car))
        s = val['speed']
        inn.append(idx)
        if float(s) == 0.0:
            speed.append(s)
            if found == 1:
                if idx != len(car)-1:
                    del speed[len(speed)-1]
            found = 1
        else:
            if found == 1:
                speed.append(temp)
            found = 0
            speed.append(s)
        temp = s


    print(speed)
    print(inn)
    break

    # speed = [float(s['bering']) for s in car]
    # car_speed.append(speed)