'''
DateTime.py
Author: Michael Chang
Desc: Output current time and date of today

Future implementations: 
    * adding feature of holidays
    * Birthday
'''

import time as t
import datetime as dt

monthName = {
    1:"January",
    2:"Febuary",
    3:"March",
    4:"April",
    5:"May",
    6:"June",
    7:"July",
    8:"Augest",
    9:"Septeber",
    10:"October",
    11:"November",
    12:"December"
}

# Desc: Output current date (Day, Month, Date, Year)
def currentDate():
    dateNow = dt.datetime.now()

    response = "Today is {} {} {}, {}".format(dateNow.strftime("%A"), monthName[dateNow.month], int(dateNow.strftime("%d")), dateNow.year)

    return response

# Desc: Output current time
def currentTime():
    currTime = dt.datetime.now().strftime('%H:%M')          # Get the current time
    convTime = dt.datetime.strptime(currTime, '%H:%M')      # Convert to str type
    resTime = convTime.strftime("%I:%M %p")                 # Convert time from 24 hr to 12 hr
    response = "The time is now {}".format(resTime)         # Output the response

    return response



