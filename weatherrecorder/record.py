from sense_hat import SenseHat
import sqlite3
import os
import time
import datetime

#if os.path.isfile('./cabinhat.db')
conn = sqlite3.connect('../cabinhat.db')
sense = SenseHat()

c = conn.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='weather'")

if c.fetchone() == None:
    c.execute(""" CREATE TABLE weather (
                    type text,
                    value real,
                    datetime text
            )""")
    conn.commit()
c.execute("SELECT * FROM weather")
print(c.fetchall())
conn.close()


def get_dict(weath_type, sense_data):
    return {'type': weath_type, 'value': sense_data}

while True:
    temp = sense.get_temperature()
    humid = sense.get_humidity()
    pressure = sense.get_pressure()
    
    conn = sqlite3.connect('../db/cabinhat.db')
    c = conn.cursor()
    c.execute("INSERT INTO weather VALUES (:type, :value, DateTime('now'))", get_dict('Temp', temp))
    c.execute("INSERT INTO weather VALUES (:type, :value, DateTime('now'))", get_dict('Humid', humid))
    c.execute("INSERT INTO weather VALUES (:type, :value, DateTime('now'))", get_dict('Pressure', pressure))
    conn.commit()
    conn.close()
    print(datetime.datetime.now())
    print('Weather data recorded. Sleeping 30 minutes')
    time.sleep(1800) #Change the parameter of time.sleep() to change interval time (seconds) for recordings. 
    
