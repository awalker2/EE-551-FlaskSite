import itertools
import urllib as url
import re

def twevleToTwentyFour(hours, meridiem):
    if (meridiem == "PM" and (hours<11)):
        hours = hours + 12
    elif (meridiem == "AM" and (hours == 12)):
        hours = 0
    return hours
    
def courseScrape(key, site):
    data = url.urlopen(site).readlines()

    #Will have a full list in format: [course, lab or not, [time sublists]...]
    fullList = []
    timeList = []
    fullList.append(key)

    #The HTML has an extra space for every letter missing under 3
    if re.search("[A-Z][A-Z][ ]", key[:3]):
        key = key[:3] + " " + key[3:]
    elif re.search("[A-Z][ ]", key[:3]):
        key = key[:2] + "  " + key[2:]
    #print key
    
    #Non lab sections can either be xxx-123L# or xxx-123L, labs must be xxx-123L+letter for semester 3+ classes
    #Non recitation sections can either be xxx-123R# or xxx-123R, recitations must be xxx-123R+letter for semester 3+ classes
    if  key[-1:] == "L":
        key = key[:-1]
        key = key + "[L][A-Z]"
    elif key[-1:] == "R":
        key = key[:-1]
        key = key + "[R][A-Z]"
    else:
        key = "(?:(?=" + key + "(?!L)[A-Z])("+ key + "(?!R)[A-Z])" + "|" + key + "[L][1-9 ]+" + ")"
        
    found = False
    for line in data:
        #Need to make sure key was actually found and not a cross list
        if (re.search(key, line) and "Cross-Listed" not in line):
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
            #Need to not add any times for cancelled courses
            if ("CANCELLED" in line):
                found = False
            elif re.search("[0-1][0-9]:[0-6][0-9]", line):
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
    #print fullList
    return fullList

def checkOneForConflict(timeList):
    #print timeList
    #Sort the list
    timeList.sort(key=lambda x: x[0])
    #print timeList
    #See if there are any conflicts
    startTimePrev = -1
    endTimePrev = -1
    #https://stackoverflow.com/questions/325933/determine-whether-two-date-ranges-overlap
    for i in xrange(0, len(timeList)):
        if ((startTimePrev <= timeList[i][1]) and (endTimePrev >= timeList[i][1]))or(startTimePrev <= timeList[i][1]) and (timeList[i][0] <= endTimePrev):
            return "conflict"
        startTimePrev = timeList[i][0]
        endTimePrev = timeList[i][1]
    return "no conflict"

def checkAllForConflict(courseList, term):
    errorString = ""
    
    print "Checking term " + str(term) + " for conflicts..." 
    #Check whether it is a Spring of Fall term
    fallSite = "http://personal.stevens.edu/~gliberat/registrar/18f/18f_u.html"
    springSite = "http://personal.stevens.edu/~gliberat/registrar/18s/18s_u.html"
    if (term%2==0):
        site = springSite
    else:
        site = fallSite

    #Create a master list of all the courses with times    
    masterList = []
    for course in courseList:
        lst = courseScrape(course, site)
        print lst
        #A list with one element means the course does not exist in the term
        if len(lst) == 1:
            #print str(lst[0]) + " does not exist in the selected term"
            errorString = errorString + str(lst[0]) + " does not exist in the selected term\n"
        else:
            del lst[0]
            #Combine the start and end times into a list
            index = 0
            #print lst
            for subLst in lst:
                index = 0
                for i in xrange(0, len(subLst), 2):
                    tempLst = [subLst[index], subLst[index+1]]
                    subLst.append(tempLst)
                    index = index + 2
                for i in xrange(0, index):
                    del subLst[0]
            #print lst
            masterList.append(lst)
    if (errorString != ""):
        return errorString
    
    #Generate cartesian products for every course combination
    for combination in itertools.product(*masterList):
        timeList = []
        for lst in combination:
            timeList= timeList + lst    

        checkOneForConflict(timeList)
        if (checkOneForConflict(timeList) == "no conflict"):
            return "no conflict"
    return "conflict\n"

#print checkAllForConflict(["MA 221", "MA 221R", "PEP 112", "PEP 112R", "E 126", "E 245", "E 245L", "E 231", "CAL 105", "CPE 462","CPE 462"], 2)
#print checkAllForConflict(["CPE 4362","CPE33 462"], 2)




