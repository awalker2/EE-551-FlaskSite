import helperFunctions as helper
import itertools

def checkOneForConflict(timeList):
    timeListofLists = []
    index = 0
    for i in xrange(0, len(timeList), 2):
        timeListSub = []
        timeListSub.append(timeList[index])
        timeListSub.append(timeList[index+1])
        timeListofLists.append(timeListSub)
        index = index + 2
    #print timeListofLists
    for i in itertools.combinations(timeListofLists, r = 2):
        print i
        #https://stackoverflow.com/questions/325933/determine-whether-two-date-ranges-overlap
        if ((i[0][0] <= i[1][1]) and (i[0][1] >= i[1][1]))or(i[0][0] <= i[1][1]) and (i[1][0] <= i[0][1]):
            print "conflict"
            return "conflict"
    print "no conflict"
    return "no conflict"

def checkAllForConflict(courseList, term):
    #Check whether it is a Spring of Fall term
    fallSite = "http://personal.stevens.edu/~gliberat/registrar/17f/17f_u.html"
    springSite = "http://personal.stevens.edu/~gliberat/registrar/17s/17s_u.html"
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
            print str(lst[0]) + " does not exist in the selected term"
            return str(lst[0]) + " does not exist in the selected term"
        del lst[0]
        masterList.append(lst)

    #Generate cartesian products for every course combination
    for combination in itertools.product(*masterList):
        timeList = []
        for lst in combination:
            timeList = timeList + lst
        print timeList
        if (checkOneForConflict(timeList) == "no conflict"):
            return "no conflict"

checkAllForConflict(["E 232", "EE 471", "CPE 390"], 2)




