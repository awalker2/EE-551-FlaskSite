import helperFunctions as helper
import itertools

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
        lst = helper.courseScrape(course, site)
        print lst
        #A list with one element means the course does not exist in the term
        if len(lst) == 1:
            #print str(lst[0]) + " does not exist in the selected term"
            return str(lst[0]) + " does not exist in the selected term"
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
            
    #Generate cartesian products for every course combination
    for combination in itertools.product(*masterList):
        timeList = []
        for lst in combination:
            timeList= timeList + lst    

        checkOneForConflict(timeList)
        if (checkOneForConflict(timeList) == "no conflict"):
            return "no conflict"
    return "conflict"

#print checkAllForConflict(["MA 221", "CAL 103","MA 221R", "PEP 112", "PEP 112R", "E 126", "E 245", "E 245L", "E 231", "CAL 105", "CPE 462","CPE 462"], 2)





