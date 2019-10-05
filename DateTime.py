import datetime as dt
import time as t

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

def currentDate():
    dateNow = dt.datetime.now()
    dateNow.month

    response = "Today is {} {} {}, {}".format(dateNow.strftime("%A"), monthName[dateNow.month], int(dateNow.strftime("%d")), dateNow.year)

    return response