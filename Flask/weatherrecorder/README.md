## weatherrecorder

``` record.py ``` is the program which records all the weather data to the database.
This program needs to be running continuously in order to get a history of your weather data

## running

1. ``` git clone https://github.com/Espen84/CabinHAT ```
2. ``` cd CabinHAT/Flask/weatherrecorder ```
3. ``` python record.py ```

## Changing database recording time interval

Change the parameter of time.sleep() in ``` record.py ``` (line 44). The number is in seconds. Default is 1800 (30 minutes).
