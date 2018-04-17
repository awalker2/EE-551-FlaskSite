import urllib as url
import re

def twevleToTwentyFour(hours, meridiem):
    if (meridiem is "PM" and (hours<11)):
        hours = hours + 12
    elif (meridiem is "AM" and (hours is 12)):
        hours = 0
    return hours
    
def courseScrape(key, lab, site):
    data = url.urlopen(site).readlines()

    #Will have a full list in format: [course, lab or not, [time sublists]...]
    fullList = []
    timeList = []
    fullList.append(key)
    fullList.append("Lab: " + str(lab))

    #Non lab sections can either be xxx-123L# or xxx-123L, labs must be xxx-123L+letter
    if lab is False:
        key = "(?:" + key + "(?!L)[A-Z]" + "|" + key + "[L][1-9 ]+" + ")"
    else:
        key = key + "[L][A-Z]"

    found = False
    for line in data:
        if re.search(key, line):
            found = True
            #print line
        elif "<hr width" in line and found == True:
            found = False
            fullList.append(timeList)
            #print fullList
            timeList = []
        elif "<hr width" in line and found == False:
            #Do nothing
            x = 1
        elif found == True:
            if re.search("[0-1][0-9]:[0-6][0-9]", line):
                time = line.split()
                #print time
                #Get raw start and end time strings
                startTime = time[1]
                endTime = time[2]
                #Get the AM/PM part
                startAMPM = startTime[-2:]
                endAMPM = endTime[-2:]
                #Remove the AM/PM part
                startTime = startTime[:-2]
                endTime = endTime[:-2]
                #Get the hours
                startHours = startTime[:2]
                endHours = endTime[:2]
                #Get the minutes
                startMins = startTime[-2:]
                endMins = endTime[-2:]
                #Start float conversion and convert from 12 to 24 hours
                startFloat = float(startHours)
                endFloat = float(endHours)
                startFloat = twevleToTwentyFour(startFloat, startAMPM)
                endFloat = twevleToTwentyFour(endFloat, endAMPM)
                #Add the minutes too
                startFloat = startFloat + float(startMins)/60
                endFloat = endFloat + float(endMins)/60
                #print startFloat, endFloat
                #Add in 24 hours for each day, also must work if course is offered same time multiple days
                for char in list(time[0]):
                    if char == 'M':
                        timeList.append(startFloat)
                        timeList.append(endFloat)
                    elif char == 'T':
                        timeList.append(startFloat+24)
                        timeList.append(endFloat+24)
                    elif char == 'W':
                        timeList.append(startFloat+48)
                        timeList.append(endFloat+48)
                    elif char == 'R':
                        timeList.append(startFloat+72)
                        timeList.append(endFloat+72)
                    elif char == 'F':
                        timeList.append(startFloat+96)
                        timeList.append(endFloat+96)
                    elif char == 'S':
                        timeList.append(startFloat+120)
                        timeList.append(endFloat+120)
                    elif char == 'U':
                        timeList.append(startFloat+144)
                        timeList.append(endFloat+144)
    print fullList
    return fullList
