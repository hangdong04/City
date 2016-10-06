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
print(len(data))

