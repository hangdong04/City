import csv


Car = []
each_pos = []
with open('/home/phatthanapong/Desktop/City/PyCity/Data/Car.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    ind = 1
    for row in reader:

        if int(row["num"]) > ind:
            ind = int(row["num"])
            Car.append(each_pos)
            each_pos = []
            temp = {k: row[k] for k in row.keys() & {'latitude', 'longitude', 'speed', 'bering', 'time', 'accuracy'}}
            each_pos.append(temp)
        else:
            temp = {k: row[k] for k in row.keys() & {'latitude', 'longitude', 'speed', 'bering', 'time', 'accuracy'}}
            each_pos.append(temp)

    print(Car[0][0])




