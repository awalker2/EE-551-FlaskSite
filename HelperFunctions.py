def addDictToCourseList(number, key, classes, dictionary, append=""):
    for x in range (1, number+1):
        try:
            term = int(dictionary[key+str(x)+"Term"])
            course = str(dictionary[key+str(x)])
            if (course):
                classes[int(term)].append(key[4:]+":"+course+append)
        except:
            print "Error appending with key: " + key+str(x) + "/Term"

def addListToCourseList(classList, classes):
    for x in range (0, len(classList), 2):
        try:
            course =  classList[x]
            term = classList[x+1]
            classes[term].append(course)
        except:
            print "Error appending course: " + classList[x] + " with term: " + classList[x+1]

def standardizeInput(dictionary):
    for value in dictionary:
        dictionary[value] = dictionary[value].upper()
        dictionary[value] = dictionary[value].replace("-"," ")
