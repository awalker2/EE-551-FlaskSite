transcriptList = [' ------------------------2015 Fall--------------------------\r\n',
                  'Class: CAL-105-H Grade: A-', 'Class: E-101-A Grade: P', 'Class: E-115-LF Grade: A',
                  'Class: E-120-K Grade: A', 'Class: E-121-C Grade: A', 'Class: MA-124-C Grade: A',
                  'Class: MA-461-CC Grade: A', 'Class: PEP-112-RF Grade: A',
                  ' -----------------------2016 Spring-------------------------\r\n',
                  'Class: CAL-103-A Grade: A-', 'Class: E-122-D Grade: A', 'Class: E-126-A Grade: A',
                  'Class: E-245-C Grade: A', 'Class: MA-221-F Grade: A', 'Class: MGT-103-R Grade: A',
                  ' ------------------------2016 Fall--------------------------\r\n',
                  'Class: CPE-360-A Grade: A', 'Class: CPE-390-A Grade: A', 'Class: E-231-D Grade: A',
                  'Class: E-234-RB Grade: A', 'Class: HHS-125-A Grade: A', 'Class: MA-134-A Grade: A-',
                  'Class: MA-462-A Grade: A', 'Class: PE-200-G7 Grade: P',
                  ' -----------------------2018 Spring-------------------------\r\n',
                  'Class: CPE-322-A Grade: ', 'Class: CPE-345-A Grade: ', 'Class: CPE-462-A Grade: ',
                  'Class: E-355-B Grade: ', 'Class: EE-551-A Grade: ', 'Class: EN-250-W1 Grade: ',
                  'Class: PE-200-G4 Grade: ']

classList = [[],
             ['General:MA 461', 'CH 115', 'CH 117', 'E 101', 'E 121', 'E 120', 'E 115', 'MA 121', 'CAL 103'],
             ['Science:CH 116', 'ScienceLab:CH 118', 'E 122', 'MA 123', 'PEP 111', 'CAL 105', 'MGT 103'],
             ['Humanity:HHS 125', 'General:MA 462', 'MA 221', 'MA 221R', 'PEP 112', 'PEP 112R', 'E 126', 'E 245', 'E 245L', 'E 231'],
             ['Humanity:HUM2', 'MA 134', 'E 232', 'E 232L', 'E 234', 'E 234R', 'CPE 360', 'CPE 390L', 'CPE 390'],
             ['Humanity:HUM3', 'Extra:EXTRA1', 'EE 471', 'E 344', 'E 321', 'E 243', 'E 243R', 'CPE 487'],
             ['Science:PEP 151', 'EE 345', 'E 355', 'CPE 322', 'CPE 462', 'IDE 400'],
             ['Technical:TECH1', 'Technical:TECH2', 'CPE 490', 'CPE 423', 'IDE 401'],
             ['Humanity:HUM4', 'Technical:TECH3', 'Technical:TECH4', 'CPE 424', 'IDE 402']
            ]
science1= " "
sci1=False
science2= " "
sci2=False

#Change the data structure for each course to [type, course, grade]
for semester in classList:
    counter = 0
    for clss in semester:
        tempList = ["Core", " ", " "]
        if ":" in clss:
            clssSplit = clss.split(":")
            tempList[0] = clssSplit[0]
            tempList[1] = " " + clssSplit[1].replace(" ", "-")
        else:
            tempList[1] = " " + clss.replace(" ", "-")
        semester[counter] = tempList
        counter = counter + 1

#Get the grade from transcript if available
for semester in classList:
    for clss in semester:
        for line in transcriptList:
            if clss[1] in line:
                gradeArray = line.split("Grade: ")
                if len(gradeArray) > 1:
                    clss[2] = gradeArray[1]

print classList

def writeTerm(term, firstTerm):
	if term%2==1:
		firstChar="F"	
	else:
		firstChar="S"
	currentTerm=firstTerm
	for x in xrange(0,term,+2):
		currentTerm=currentTerm+1
	return firstChar + str(currentTerm)
    
for semester in classList:
    for clss in semester:
        if clss[0] == "Science" and sci1 is False:
            science1=clss[1]
            science1Grade=clss[2]
            sci1=True
        elif clss[0] == "Science" and sci2 is False:
            science2=clss[1]
            science2Grade=clss[2]
            sci2=True

print science1
print science2
print science1Grade
print science2Grade




                
                

