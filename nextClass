#!/usr/bin/python3
import datetime

from timeTable import timeTable, codeToCourse


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

def findNext(schedule, time):
    nextCode = []
    for code in schedule:
        slots = schedule[code]
        for slot in slots:
            startTime = convertStringToDate(slot[0])
            if(time<=startTime):
                diff = (startTime - time).total_seconds()
                nextCode.append([code, slot[0], diff ])
    if(nextCode == []):
        return nextCode
    nextCode.sort(key= lambda x: x[2])
    return nextCode

def setOffset(s):
    h,m = s.split(':')
    m = str(int(m)+10)
    if(m == "60"):
        h = str(int(h) + 1)
        m = "00"
    return h+':'+m

today = datetime.datetime.now().strftime('%A')
todaySchedule = timeTable.get(today, -1)
if(todaySchedule == -1):
    print("No More Class Today")
else:
    ongoing = False
    for code in todaySchedule:
        currTime = datetime.datetime.now()
        slots = todaySchedule[code]
        if(timeInSlot(slots, currTime)):
            print(codeToCourse[code],'class is currently in Progress !!')
            break
    if(not ongoing):  
        nextClasses = findNext(todaySchedule,currTime)
        if(nextClasses == []):
            print("No more Classes for Today !!")
        else:
            print("The Upcoming Classes are - ")
            for (code,startTime,diff) in nextClasses:
                startTime = setOffset(startTime)
                print(codeToCourse[code],"at",startTime)
