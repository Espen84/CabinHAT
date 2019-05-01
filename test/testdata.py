import sqlite3

conn = sqlite3.connect('../db/cabinhat.db')

c = conn.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='weather'")
print(c.fetchone())

c.execute(""" CREATE TABLE weather (
                type text,
                value real,
                datetime text
) """)

conn.commit()
c.execute("INSERT INTO WEATHER VALUES ('Temp', 122, '2019-04-03')")
conn.commit()
c.execute("INSERT INTO WEATHER VALUES ('Humid', 60, '2019-04-03')")
conn.commit()
c.execute("INSERT INTO WEATHER VALUES ('Pressure', 40, '2019-04-03')")
conn.commit()

c.execute("INSERT INTO WEATHER VALUES ('Temp', 70, '2019-04-03')")
conn.commit()
c.execute("INSERT INTO WEATHER VALUES ('Humid', 33, '2019-04-03')")
conn.commit()
c.execute("INSERT INTO WEATHER VALUES ('Pressure', 55, '2019-04-03')")
conn.commit()

c.execute("INSERT INTO WEATHER VALUES ('Temp', 50, '2019-04-03')")
conn.commit()
c.execute("INSERT INTO WEATHER VALUES ('Humid', 43, '2019-04-03')")
conn.commit()
c.execute("INSERT INTO WEATHER VALUES ('Pressure', 35, '2019-04-03')")
conn.commit()


c.execute("INSERT INTO WEATHER VALUES ('Temp', 133, '2019-04-02')")
conn.commit()
c.execute("INSERT INTO WEATHER VALUES ('Temp', 1, '2019-04-01')")
conn.commit()
c.execute("INSERT INTO WEATHER VALUES ('Temp', 3, '2019-03-31')")
conn.commit()
c.execute("INSERT INTO WEATHER VALUES ('Temp', 5, '2019-03-30')")
conn.commit()
c.execute("INSERT INTO WEATHER VALUES ('Temp', 7, '2019-03-29')")
conn.commit()
c.execute("INSERT INTO WEATHER VALUES ('Temp', 9, '2019-03-28')")
conn.commit()
c.execute("INSERT INTO WEATHER VALUES ('Temp', 11, '2019-03-27')")
conn.commit()
c.execute("INSERT INTO WEATHER VALUES ('Temp', 13, '2019-03-26')")
conn.commit()
c.execute("INSERT INTO WEATHER VALUES ('Temp', 13, '2019-03-20')")
conn.commit()

c.execute("SELECT * FROM weather WHERE datetime BETWEEN (SELECT DATETIME('now','-7 day')) AND (SELECT DATETIME('now','-3 day'))")

print(c.fetchall())


conn.close()
