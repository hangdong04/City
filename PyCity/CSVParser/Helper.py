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