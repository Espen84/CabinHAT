# CabinHAT
Open Source Project using Raspberry Pi's with sense HAT modules to read temperature, and other relevant data to check and perform maintenance on cabin.

## Content

1. [Technologies](https://github.com/Espen84/CabinHAT#technologies)
2. [Intent](https://github.com/Espen84/CabinHAT#intent)
3. [License](https://github.com/Espen84/CabinHAT#license)
4. [Installation](https://github.com/Espen84/CabinHAT#installation)
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

The purpose of this project is to provide an open source solution for monitoring the status of a cabin, or whatever the user desires to monitor.  CabinHAT is a product that uses [Raspberry Pi](https://www.raspberrypi.org/),
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
[GNU General Public License v3.0](https://github.com/Espen84/CabinHAT/blob/master/LICENSE)

### Third party licenses:

+ [Python 2.2 and above](https://docs.python.org/3/license.html) use a GPL compatible license.  

+ [SQLite](https://www.sqlite.org/copyright.html) use a Creative Commons (CC) license.

+ [Raspberry Pi’s schematics](https://www.raspberrypi.org/app/uploads/2012/04/Raspberry-Pi-Schematics-R1.0.pdf) and 
  [Gerbers (visualization of the circuits)](https://www.raspberrypi.org/blog/final-pcb-artwork/) are freely available.

+ [ARM CPUs](https://www.raspberrypi.org/documentation/faqs/) used in Raspberry Pi, are not Open Source. 

 
## Running
This software is meant to be run on a RaspberryPi with a SenseHAT module and a PiCam module. Make sure you've got the latest
software updates for those modules

1. ```git clone https://github.com/Espen84/CabinHAT ```

2. ```cd CabinHAT/weatherrecorder ```

3. ``` python record.py``` This starts the program which records history of the weatherdata

4. ``` cd ../ ```

5. ``` python app.py ```

## Contribute

Want to contribute to the project? 
See [CONTRIBUTE.md](https://github.com/Espen84/CabinHAT/blob/master/CONTRIBUTE.md).

## Developers 

+ Aarsheim. Gorm-Erik

+ Alvsaker. Vegard

+ Fosse. Ingve

+ Holen. Marius

+ Oftedal. Espen Sivertsen

## Acknowledgements 

## Final Notes 

For more, please visit the [Wiki](https://github.com/Espen84/CabinHAT/wiki)
