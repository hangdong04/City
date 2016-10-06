import csv
class Helper:

    def reader(self, str):
        each_pos = []
        data = []

        with open(str) as csvfile:
            reader = csv.DictReader(csvfile)
            ind = 1
            for row in reader:

                if int(row["num"]) > ind:
                    ind = int(row["num"])
                    data.append(each_pos)
                    each_pos = []
                    temp = {k: row[k] for k in
                            row.keys() & {'latitude', 'longitude', 'speed', 'bering', 'time', 'accuracy'}}
                    each_pos.append(temp)
                else:
                    temp = {k: row[k] for k in
                            row.keys() & {'latitude', 'longitude', 'speed', 'bering', 'time', 'accuracy'}}
                    each_pos.append(temp)
        return data

    def preprocess(self, obj_in):
        data = []
        data_list = dict()
        speed = []
        accuracy = []
        time = []
        temp_t = None
        temp_a = None
        temp_s = None
        for item in obj_in:
            found = 0
            for idx, val in enumerate(item):
                t = val['time']
                a = val['accuracy']
                s = val['speed']
                if float(s) == 0.0:
                    speed.append(s)
                    time.append(t)
                    accuracy.append(a)
                    if found == 1:
                        if idx != len(item) - 1:
                            del speed[len(speed) - 1]
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

            data_list['speed'] = speed
            data_list['time'] = time
            data_list['accuracy'] = accuracy
            data.append(data_list)
            speed = []
            time = []
            accuracy = []
        return data

