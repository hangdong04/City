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
avg_speed =Helper.avg_speed(data)
print(avg_speed)
# for car in Car:
#     print(car['speed'])
# for item in data:
#     speed_avg = 0
#     for idx, val in enumerate(item['speed']):
#         if idx != 0:
#             speed_avg += (float(val)*(int(item['time'][idx])-int(item['time'][idx-1])))
#     print(speed_avg/(int(item['time'][-1])-int(item['time'][0])))