from CSVParser.Helper import Helper
car_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Car.csv'
car_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Car.csv'
motor_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Motorcycle.csv'
bike_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Bicycle.csv'
run_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Run.csv'
walk_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Walk.csv'

data = []
Helper = Helper()
Car = Helper.reader(car_path)
car_speed =[]
speed = []
zero = 0
for car in Car:
    for idx, val in enumerate(car):
        temp = val['speed']
        if float(temp) == 0.0:
            zero += 1
        else:
            zero = 0

        if zero > 0:
            del speed[-1]
        else:
            speed.append(temp)
    print(speed)
    break

    # speed = [float(s['bering']) for s in car]
    # car_speed.append(speed)