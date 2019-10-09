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

def currentTime():
    # datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # currHour = dt.datetime.now().hour
    # currMin = dt.datetime.now().minute
    currTime = dt.datetime.now().strftime('%H:%M')
    convTime = dt.datetime.strptime(currTime, '%H:%M')
    resTime = convTime.strftime("%I:%M %p")
    response = "The time is now {}".format(resTime)

    return response

    # currTime.strftime("%I:%M %p")
    # if currHour > 11:
    #     response = "The time now is {}:{}pm"

'''
d = dt.datetime.strptime("10:30", "%H:%M")
>>> d.strftime("%I:%M %p")
'10:30 AM'
>>> d = datetime.strptime("22:30", "%H:%M")
>>> d.strftime("%I:%M %p")
'10:30 PM'

'''