from CSVParser.Helper import Helper
import json
# car_path = 'C:\\Users\Phatthanaphong\Desktop\City\PyCity\Data\Car.csv'
car_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Car.csv'
motor_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Motorcycle.csv'
bike_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Bicycle.csv'
run_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Run.csv'
walk_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Walk.csv'

Helper = Helper()
Car = Helper.reader(car_path)
data = Helper.preprocess(Car)
print(data[6]['time'][209:213])
temp = None
for idx,val in enumerate(data[6]['time']):
    if idx!=0:
        if temp>val:
            print("xxx")
            print(idx)
    temp = val

# avg_speed =Helper.avg_speed(data)
# min_speed = Helper.min(data)
# max_speed = Helper.max(data)
# print("max",max_speed)
# print("min",min_speed)
# print("avg_s",avg_speed)
