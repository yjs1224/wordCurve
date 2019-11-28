# wordCurve

This repository is the backend of [WordCurvePage](https://github.com/wangke1996/WordCurvePage)

You can view the page [here](https://wangke1996.github.io/WordCurvePage)

This README file is for developers

## Set Up
* Python >= 3.6
- Install packages in [requirements.tst](requirements.txt)
* Modify [config.py](backend/lib/config.py) to set file path
- Run

        python run.py --port=xxx --debug
    to check if any error occurred. "xxx" is a server port you can use, such as 5000. (__Make sure this port is opened in your firewall rules__)

## Frontend Interaction
* Config backend server url(```https://your.server.ip.address:your port```) in your [frontend module](https://github.com/wangke1996/WordCurvePage#backend-interaction). 
- See the [document of flask](http://flask.palletsprojects.com/en/1.1.x/) for more details.

## Developing codes
* This backend is based on [Flask](https://www.palletsprojects.com/p/flask/), you can use any other web server frameworks as well, such as [Django](https://www.djangoproject.com/), even just the http package in python.
- Examples I provided is a simple interface without database manager. If you are dealing with large amount of data, manage database by yourself. 
* If you are using flask like my codes, set ```"--debug"``` in developing. Then you don't need to restart the program when changes are made.
