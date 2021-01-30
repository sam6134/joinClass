#!/usr/bin/python3
import webbrowser
import datetime

from timeTable import timeTable, codeToCourse

def startClass(classCode):
    link = 'https://iitjammu.ipearl.ai/extras/course-v1:ITJA+'+str(classCode)+'+2021/join_zoom'
    webbrowser.open(link)

def getCurrentDay():
    return datetime.datetime.now().strftime('%A')

def convertStringToDate(s):
    x = datetime.datetime.now().strftime('%d,%m,%y')
    return(datetime.datetime.strptime(x+' '+s,'%d,%m,%y %H:%M'))

def timeInSlot(slots, time):
    for slot in slots:
        startTime = convertStringToDate(slot[0])
        endTime = convertStringToDate(slot[1])
        if(time>=startTime and time<=endTime):
            return True
    return False



today = getCurrentDay()
todaySchedule = timeTable.get(today, -1)
if(todaySchedule == -1):
    print("No Class Today")
else:
    flag = False
    for code in todaySchedule:
        currTime = datetime.datetime.now()
        slots = todaySchedule[code]
        if(timeInSlot(slots, currTime)):
            startClass(code)
            flag = True
            break
    if(not flag):
        print("No Class in Progress !!")