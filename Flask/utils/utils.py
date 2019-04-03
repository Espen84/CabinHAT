import sqlite3

def get_week_history():
    history = []
    for i in range(7):
        history.append(get_day_history(i))
    return history

def get_day_history(days_ago):
    """
        Returns a dictionary with the average temp, humid
        and air pressure for the given day
        Parameter days_ago must be an integer between 0 and 6.
        Returns None if days_ago is illegal
    """
    if days_ago < 0 or days_ago > 6:
        return None
    conn = sqlite3.connect('db/cabinhat.db')
    c = conn.cursor()

    if days_ago == 0:
        c.execute(" SELECT * FROM weather WHERE datetime LIKE (SELECT DATE('now', '0 day')) ")
    else:
        start = '-' + str(days_ago) + ' day'
        days = {'start': start}
        c.execute("""   SELECT * FROM weather
                        WHERE datetime LIKE
                        (SELECT DATE('now', :start))
        """, days)
    temp_array = []
    humid_array = []
    pressure_array = []
    data = c.fetchall()

    for i in data:
        if i[0] == 'Temp':
            temp_array.append(i[1])
        elif i[0] == 'Humid':
            humid_array.append(i[1])
        elif i[0] == 'Pressure':
            pressure_array.append(i[1])
    conn.close()

    if len(temp_array) == 0:
        avg_temp = None
    else:
        avg_temp = round((sum(temp_array) / len(temp_array)), 2)

    if len(humid_array) == 0:
        avg_humid = None
    else:
        avg_humid = round((sum(humid_array) / len(humid_array)), 2)

    if len(pressure_array) == 0:
        avg_pressure = None
    else:
        avg_pressure = round((sum(pressure_array) / len(pressure_array)), 2)

    return {'temp': avg_temp, 'humid': avg_humid, 'pressure': avg_pressure}

get_week_history()
