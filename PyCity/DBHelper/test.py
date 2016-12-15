import sqlite3

db_path = 'C:\\Users\phatt\Desktop\City\PyCity\GpsData\Car'
conn = sqlite3.connect(db_path)

c = conn.cursor()
c.execute('SELECT max(num) FROM location')

print(c.fetchone()[0])