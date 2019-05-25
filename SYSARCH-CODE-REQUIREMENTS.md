## System architecture & code requirements (Please read this before contributing)

CabinHAT is a small software, but it is a piece of software is split up into four parts
* Flask web-framework
* SQLite database
* Frontend with Bootstrap framework
* Python sensor history recorder

### Flask web-framework
All functions and services which concerns routing the webpages, serving JSON and pictures, are done through Flask. 
Currently, all Flask-related code resides in the [```app.py```](https://github.com/Espen84/CabinHAT/blob/master/cabinhat/app.py). All
code that is not Flask-related must reside in other files, for instance in ```utils.py```. For Flask contributions, it's important that you are familiar with
good Flask-practice and Pythonic code styles. Read more at http://flask.pocoo.org/ and https://docs.python-guide.org/writing/style/



### SQLite database
SQLite is included in Python and does not require any additional downloads and installation. All DDL (Data Definition Language) is found at
[```record.py```](https://github.com/Espen84/CabinHAT/blob/master/cabinhat/weatherrecorder/record.py). Any DDL addititions (new tables) 
is not required to be found in ```record.py``` unless it makes sense to place it there.

### Frontend
Our frontend is written with the CSS-framework Bootstrap. Any frontend contributions should conform to using Bootstrap with the same
color scheme, navbar and footer that is already present in CabinHAT. Check out Bootstrap's documentation [here](https://getbootstrap.com/docs/4.3/getting-started/introduction/)

Currently, all HTML, (and future) CSS and JavaScript files reside in the [```templates```-directory](https://github.com/Espen84/CabinHAT/tree/master/cabinhat/templates)

### Sensor history recorder
Lastly, we have [```weatherrecorder/record.py```](https://github.com/Espen84/CabinHAT/blob/master/cabinhat/weatherrecorder/record.py). This file is the
program which writes sensor data to the SQLite database. This subprogram is vanilla Python and only requires you to follow good Pythonic
practice in order to contribute.
