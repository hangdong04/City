import csv
from CSVParser.Model import Model
import numpy
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
        bearing = []
        temp_t = None
        temp_a = None
        temp_s = None
        temp_b = None
        for item in obj_in:
            found = 0
            for idx, val in enumerate(item):
                t = float(val['time'])
                a = float(val['accuracy'])
                s = float(val['speed'])
                b = float(val['bering'])
                if float(s) == 0.0:
                    speed.append(s)
                    time.append(t)
                    accuracy.append(a)
                    bearing.append(b)
                    if found == 1:
                        if idx != len(item) - 1:
                            del speed[-1]
                            del time[-1]
                            del accuracy[-1]
                            del bearing[-1]
                    found = 1
                else:
                    if found == 1:
                        speed.append(temp_s)
                        time.append(temp_t)
                        accuracy.append(temp_a)
                        bearing.append(temp_b)
                    found = 0
                    speed.append(s)
                    time.append(t)
                    accuracy.append(a)
                    bearing.append(temp_b)
                temp_s = s
                temp_t = t
                temp_a = a
                temp_b = b
            ordered = True
            while ordered:
                ordered = False
                for idx, val in enumerate(time):
                    if idx != 0:
                        if temp_t > val:
                            ordered = True
                            del speed[idx]
                            del time[idx]
                            del accuracy[idx]
                            del bearing[idx]
                        else:
                            temp_t = val
                    else:
                        temp_t = val
            for idx, val in enumerate(accuracy):
                if float(val) > 200:
                    del speed[idx]
                    del time[idx]
                    del accuracy[idx]
                    del bearing[idx]
            data_list['speed'] = speed
            data_list['time'] = time
            data_list['accuracy'] = accuracy
            data_list['bearing'] = bearing
            data.append(data_list.copy())
            speed = []
            time = []
            accuracy = []
            bearing = []
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

    def std(self, data):
        std_value = []
        for item in data:
            std = numpy.std(item['speed'])
            std_value.append(std)
        return std_value

    def avg_speed(self, data):
        return_data = []
        for item in data:
            speed_avg = 0
            for idx, val in enumerate(item['speed']):
                if idx != 0:
                    speed_avg += (float(val) * (int(item['time'][idx]) - int(item['time'][idx - 1])))
            return_data.append(speed_avg / (int(item['time'][-1]) - int(item['time'][0])))
        return return_data

    def avg_speed_nozero(self, data):
        return_data = []
        for item in data:
            speed_avg = 0
            time = 0
            prevSpeed = 0
            for idx, val in enumerate(item['speed']):
                if not(prevSpeed == 0 and val == 0):
                    if idx != 0:
                        dt = (item['time'][idx] - item['time'][idx - 1])
                        speed_avg += (float(val) * dt)
                        time += dt
                prevSpeed = val
            if time == 0:
                time = 1
            return_data.append(speed_avg / time)
        return return_data

    def feature_list(self, max, std, avg, avg_nz, target):
        data = []
        label = []
        for idx in range(len(max)):
            item = []
            item.append(max[idx])
            item.append(std[idx])
            item.append(avg[idx])
            item.append(avg_nz[idx])
            label.append(target)
            data.append(item)
        model = Model(data, label)
        return model

    def time_rescale(self,time):
        res_time = []
        init_time = 0
        for idx, val in enumerate(time):
            if idx != 0:
                res_time.append((val-init_time)/1000)
            else:
                init_time = val
                res_time.append(0)
        return res_time