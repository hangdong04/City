from CSVParser.Helper import Helper
import json
car_path = 'C:\\Users\Phatthanaphong\Desktop\City\PyCity\Data\Car.csv'
# car_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Car.csv'
motor_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Motorcycle.csv'
bike_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Bicycle.csv'
run_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Run.csv'
walk_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Walk.csv'

Helper = Helper()
Car = Helper.reader(car_path)
data = Helper.preprocess(Car)
print(len(Car[2]))
# for car in data:
#     print(car['speed'])
#     break
    # speed_avg = 0
    # for idx, val in enumerate(car['speed']):
    #     if idx != 0:
    #         speed_avg += (float(val)*(int(car['time'][idx])-int(car['time'][idx-1])))
    # print(speed_avg/(int(car['time'][-1])-int(car['time'][0])))