# CabinHAT
Open Source Project using Raspberry Pi's with sense HAT modules to read temperature, and other relevant data to check and perform maintenance on cabin.

![alt text][Pi picture]

[Pi picture]: https://github.com/Espen84/CabinHAT/blob/master/pic/nodeRED/Pi%20bilde2.jpg "Pi picture"

![alt text][CabinHAT dashboard]

[CabinHAT dashboard]: https://github.com/Espen84/CabinHAT/blob/master/pic/nodeRED/dashboard.png "Dashboard"

## Content

1. [Technologies](https://github.com/Espen84/CabinHAT#technologies)
2. [Intent](https://github.com/Espen84/CabinHAT#intent)
3. [License](https://github.com/Espen84/CabinHAT#license)
4. [Installing and running](https://github.com/Espen84/CabinHAT#installing-and-running)
5. [Contribute](https://github.com/Espen84/CabinHAT#contribute)
6. [Developers](https://github.com/Espen84/CabinHAT#developers)
7. [Acknowledgements](https://github.com/Espen84/CabinHAT#acknowledgements)

[]()

 
## Technologies
+ [Rasberry Pi 3 or 3+](https://www.raspberrypi.org/products/)
+ [Sense HAT module](https://www.raspberrypi.org/products/sense-hat/)
+ [Camera compatible w/ Raspberry Pi (module or USB webcam)](https://www.raspberrypi.org/products/camera-module-v2/)
+ [Python 3.5 or higher](https://www.python.org/downloads/)
+ [SQLite](https://www.sqlite.org/index.html)
 
## Intention

The purpose of this project is to provide an open source solution for monitoring the status of your cabin, or whatever the user desires to monitor.  CabinHAT is a product that uses [Raspberry Pi](https://www.raspberrypi.org/),
[Sense HAT](https://www.raspberrypi.org/products/sense-hat/),
[Flask](http://flask.pocoo.org/) and 
[SQLite](https://www.sqlite.org/index.html), to deliver data such as:
+ [Temperature](https://en.wikipedia.org/wiki/Temperature)
+ [Humidity](https://en.wikipedia.org/wiki/Humidity)
+ [Air pressure](https://en.wikipedia.org/wiki/Atmospheric_pressure)
+ Real time pictures  

This to help the user determine if there is something wrong at the location where the SenseHAT is deployed, and if maintenance needs to be performed. 

## License

### Our license 
[BSD 3-Clause License](https://github.com/Espen84/CabinHAT/blob/master/LICENSE.md)

MER OM LICENSE HER, HVORFOR DENNE? ER DEN KOMPATIBEL MED DE ANDRE?

### Third party licenses:

+ [Python 2.2 and above](https://docs.python.org/3/license.html) use a GPL compatible license.  

+ [SQLite](https://www.sqlite.org/copyright.html) use a Creative Commons (CC) license.

+ [Raspberry Pi’s schematics](https://www.raspberrypi.org/app/uploads/2012/04/Raspberry-Pi-Schematics-R1.0.pdf) and 
  [Gerbers (visualization of the circuits)](https://www.raspberrypi.org/blog/final-pcb-artwork/) are freely available.

+ [ARM CPUs](https://www.raspberrypi.org/documentation/faqs/) used in Raspberry Pi, are not Open Source. 

 
## Installing and running
This software is meant to be run on a RaspberryPi with a [Sense HAT module](https://www.raspberrypi.org/documentation/hardware/sense-hat/) and a [Picamera module](https://picamera.readthedocs.io/en/release-1.13/install.html). Make sure you've got the latest
software updates for those modules.

1. ```git clone https://github.com/Espen84/CabinHAT ```

2. ```cd CabinHAT``` and run ```pip3 install -e .``` This will install Flask and package the python files, making imports more trivial

3. ```cd weatherrecorder ``` and run ``` python3 record.py``` This starts the program which records history of the weatherdata

4. Open a new terminal window and cd to root of the repository

5. ``` python3 app.py ``` This starts the webserver

6. Go to ``` 0.0.0.0:5000 ``` in a browser to see the dashboard

**DISCLAIMER:** Port forwarding is done at your own risk. It is not recommended using Flask's webserver.

### Running on other than RASBIAN/Raspberry Pi
Following steps 1-6 is tested on Windows 10 and Mac OS (in addition to on Raspberry PI). The program will import dummy emulators, reporting random sensor data.


## Contribute

Want to contribute to the project? 
See [CONTRIBUTE.md](https://github.com/Espen84/CabinHAT/blob/master/CONTRIBUTE.md).

## Developers 

+ Aarsheim. Gorm-Erik [@gormaar](https://github.com/gormaar)

+ Alvsaker. Vegard [@vegardalvsaker](https://github.com/vegardalvsaker)

+ Fosse. Ingve [@ingvefosse](https://github.com/ingvefosse)

+ Holen. Marius [@mariusholen](https://github.com/mariusholen)

+ Oftedal. Espen Sivertsen [@Espen84](https://github.com/Espen84)

## Acknowledgements 

## Final Notes 

For more, please visit the [Wiki](https://github.com/Espen84/CabinHAT/wiki)
