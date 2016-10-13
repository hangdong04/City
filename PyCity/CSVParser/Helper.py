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
                            del speed[-1]
                            del time[-1]
                            del accuracy[-1]
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

            while
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
            data.append(data_list.copy())
            speed = []
            time = []
            accuracy = []
        return data

    def min(self, data):
        min_value = []
        for item in data:
            min_value.append(min(item['speed']))
        return min_value

    def max(self, data):
        max_value = []
        for item in data:
            max_value.append(max(item['speed']))
        return max_value

    def avg_speed(self, data):
        return_data = []
        for item in data:
            speed_avg = 0
            for idx, val in enumerate(item['speed']):
                if idx != 0:
                    speed_avg += (float(val) * (int(item['time'][idx]) - int(item['time'][idx - 1])))
            return_data.append(speed_avg / (int(item['time'][-1]) - int(item['time'][0])))
        return return_data