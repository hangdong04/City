import sqlite3
label_bic = 'Bicycle'
label_car = 'Car'
label_walk = 'Walk'
label_run = 'Running'
label_motor = 'Motorcycle'

db_car = 'C:\\Users\phatt\Desktop\City\PyCity\GpsData\Car'
conn_car = sqlite3.connect(db_car)
car = conn_car.cursor()
car.execute('SELECT max(num) FROM location')
last_car = car.fetchone()[0]

db_bic = 'C:\\Users\phatt\Desktop\City\PyCity\GpsData\Bicycle'
conn_bic = sqlite3.connect(db_bic)
bic = conn_bic.cursor()
bic.execute('SELECT max(num) FROM location')
last_bic = bic.fetchone()[0]

db_motor = 'C:\\Users\phatt\Desktop\City\PyCity\GpsData\Motorcycle'
conn_motor = sqlite3.connect(db_motor)
motor = conn_motor.cursor()
motor.execute('SELECT max(num) FROM location')
last_motor = motor.fetchone()[0]

db_run = 'C:\\Users\phatt\Desktop\City\PyCity\GpsData\Run'
conn_run = sqlite3.connect(db_run)
run = conn_run.cursor()
run.execute('SELECT max(num) FROM location')
last_run = run.fetchone()[0]

db_walk = 'C:\\Users\phatt\Desktop\City\PyCity\GpsData\Walk'
conn_walk = sqlite3.connect(db_walk)
walk = conn_walk.cursor()
walk.execute('SELECT max(num) FROM location')
last_walk = walk.fetchone()[0]

print(last_bic,last_car,last_motor,last_run,last_walk)

## Edit NUM of new database
db_edit = 'C:\\Users\phatt\Desktop\City\PyCity\GpsData\Benz\GpsLog 170959.db'
conn = sqlite3.connect(db_edit)
c = conn.cursor()
c.execute('SELECT label FROM location group by label')
tag_list = c.fetchall()
c.execute('SELECT num,label FROM location group by num')
num_list = c.fetchall()
print(num_list)
for item in num_list:
    print(item[0],item[1])
    if item[1] == label_car:
        last_car += 1
        t = (last_car, item[0])
        c.execute('UPDATE location SET num = ? WHERE num = ?', t)
    elif item[1] == label_bic:
        last_bic += 1
        t = (last_bic, item[0])
        c.execute('UPDATE location SET num = ? WHERE num = ?', t)
    elif item[1] == label_motor:
        last_motor += 1
        t = (last_motor, item[0])
        c.execute('UPDATE location SET num = ? WHERE num = ?', t)
    elif item[1] == label_walk:
        last_walk += 1
        t = (last_walk, item[0])
        c.execute('UPDATE location SET num = ? WHERE num = ?', t)
    elif item[1] == label_run:
        last_run += 1
        t = (last_run, item[0])
        c.execute('UPDATE location SET num = ? WHERE num = ?', t)
conn.commit()
for tag in tag_list:
    if tag[0] == label_car:
        c.execute('SELECT * FROM location WHERE label = "Car"')
        data = c.fetchall()
        if len(data) != 0:
            car.executemany('INSERT INTO location VALUES (?,?,?,?,?,?,?,?)', data)
            conn_car.commit()
    elif tag[0] == label_run:
        c.execute('SELECT * FROM location WHERE label = "Running"')
        data = c.fetchall()
        if len(data) != 0:
            run.executemany('INSERT INTO location VALUES (?,?,?,?,?,?,?,?)', data)
            conn_run.commit()
    elif tag[0] == label_walk:
        c.execute('SELECT * FROM location WHERE label = "Walk"')
        data = c.fetchall()
        if len(data) != 0:
            walk.executemany('INSERT INTO location VALUES (?,?,?,?,?,?,?,?)', data)
            conn_walk.commit()
    elif tag[0] == label_bic:
        c.execute('SELECT * FROM location WHERE label = "Bicycle"')
        data = c.fetchall()
        if len(data) != 0:
            bic.executemany('INSERT INTO location VALUES (?,?,?,?,?,?,?,?)', data)
            conn_bic.commit()
    elif tag[0] == label_motor:
        c.execute('SELECT * FROM location WHERE label = "Motorcycle"')
        data = c.fetchall()
        if len(data) != 0:
            motor.executemany('INSERT INTO location VALUES (?,?,?,?,?,?,?,?)', data)
            conn_motor.commit()
conn.close()












