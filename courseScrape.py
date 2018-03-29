import urllib as url
import re

site = "http://personal.stevens.edu/~gliberat/registrar/17f/17f_u.html"
data = url.urlopen(site).readlines()

key = "BIO 484"
fullList = []
timeList = []
fullList.append(key)

found = False
for line in data:
    if key in line:
        found = True
        print line
    elif "<hr width" in line and found == True:
        found = False
        fullList.append(timeList)
        print fullList
        timeList = []
    elif "<hr width" in line and found == False:
        #Do nothing
        x = 1
    elif found == True:
        if re.search("[0-1][0-9]:[0-6][0-9]", line):
            time = line.split()
            print time
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
            #Start float conversion and add 12 hours for PM if needed
            startFloat = float(startHours)
            endFloat = float(endHours)
            if startAMPM == "PM":
                startFloat = startFloat + 12
            if endAMPM == "PM":
                endFloat = endFloat + 12
            #Add the minutes too
            startFloat = startFloat + float(startMins)/60
            endFloat = endFloat + float(endMins)/60
            print startFloat, endFloat
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
            

