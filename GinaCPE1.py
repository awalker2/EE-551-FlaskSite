from pyPdf import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

"""
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
"""


def writeTerm(term, firstTerm):
	if term%2==1:
		firstChar="F"	
	else:
		firstChar="S"
	currentTerm=firstTerm
	for x in xrange(1,term,+2):
		currentTerm=currentTerm+1
	return firstChar + str(currentTerm)

def cpePage1(transcriptList, classList, email, fileName):
        firstTerm = 0
        try:
                firstTerm = int(transcriptList[0][27:29])
        except:
                firstTerm = 0  


        #print transcriptList

        for semester in classList:
                counter = 0
                for clss in semester:
                        if ((clss[-1:] == "L") or (clss[-1:] == "R")):
                                del semester[counter]
                        counter = counter+1
        #print classList

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

        ##print classList

                

        CH115_term=" "
        CH115_grade=" "
        CH117_term=" "
        CH117_grade=" "
        E101_term=" "
        E101_grade=" "
        E115_term=" "
        E115_grade=" "
        E120_term=" "
        E120_grade=" "
        E121_term=" "
        E121_grade=" "
        MA121_term=" "
        MA121_grade=" "
        MA122_term=" "
        MA122_grade=" "
        CAL103_term=" "
        CAL103_grade=" "
        E122_term=" "
        E122_grade=" "
        MA123_term=" "
        MA123_grade=" "
        MA124_term=" "
        MA124_grade=" "
        MGT103_term=" "
        MGT103_grade=" "
        PEP111_term=" "
        PEP111_grade=" "
        CAL105_term=" "
        CAL105_grade=" "
        E126_term=" "
        E126_grade=" "
        E231_term=" "
        E231_grade=" "
        E245_term=" "
        E245_grade=" "
        MA221_term=" "
        MA221_grade=" "
        PEP112_term=" "
        PEP112_grade=" "
        EE250_term=" "
        EE250_grade=" "
        EE359_term=" "
        EE359_grade=" "
        E232_term=" "
        E232_grade=" "
        E234_term=" "
        E234_grade=" "
        CPE390_term=" "
        CPE390_grade=" "
        EE471_term=" "
        EE471_grade=" "
        EE348_term=" "
        EE348_grade=" "
        E312_term=" "
        E312_grade=" "
        E243_term=" "
        E243_grade=" "
        E344_term=" "
        E344_grade=" "
        EE322_term=" "
        EE322_grade=" "
        EE345_term=" "
        EE345_grade=" "
        EE448_term=" "
        EE448_grade=" "
        E355_term=" "
        E355_grade=" "
        IDE400_term=" "
        IDE400_grade=" "
        EE423_term=" "
        EE423_grade=" "
        EE465_term=" "
        EE465_grade=" "
        IDE401_term=" "
        IDE401_grade=" "
        EE424_term=" "
        EE424_grade=" "
        IDE402_term=" "
        IDE402_grade=" "
        MA134_term=" "
        MA134_grade=" "
        CPE360_term=" "
        CPE360_grade=" "
        CPE487_term=" "
        CPE487_grade=" "
        CPE462_term=" "
        CPE462_grade=" "
        CPE345_term=" "
        CPE345_grade=" "
        CPE322_term=" "
        CPE322_grade=" "
        CPE423_term=" "
        CPE423_grade=" "
        CPE490_term=" "
        CPE490_grade=" "
        CPE424_term=" "
        CPE424_grade=" "
        General1=" "
        General1_grade=" "
        gen1=False
        General2=" "
        General2_grade=" "
        General3_grade=" "
        General3=" "
        gen2=False
        gen3=False
        Technical1=" "
        Technical1_grade=" "
        tech1=False
        Technical2=" "
        Technical2_grade=" "
        tech2=False
        Technical3=" "
        Technical3_grade=" "
        tech3=False
        Technical4=" "
        Technical4_grade=" "
        tech4=False
        Humanity1=" "
        Humanity1_grade=" "
        hum1=False
        Humanity2=" "
        Humanity2_grade=" "
        hum2=False
        Humanity3=" "
        Humanity3_grade=" "
        hum3=False
        Humanity4=" "
        Humanity4_grade=" "
        hum4=False
        Science1=" "
        Science1_grade=" "
        sci1=False
        Science2=" "
        Science2_grade=" "
        sci2=False
        ScienceLab1=" "
        ScienceLab1_grade=" "
        scil1=False
        Extra1=" "
        Extra1_grade=" "
        ext1=False
        Extra2=" "
        Extra2_grade=" "
        ext2=False
        Extra3=" "
        Extra3_grade=" "
        ext3=False
        Extra4=" "
        Extra4_grade=" "
        ext4=False
        General1_term=" "
        General2_term=" "
        General3_term=" "
        Technical1_term=" "
        Technical2_term=" "
        Technical3_term=" "
        Technical4_term=" "
        Humanity1_term=" "
        Humanity2_term=" "
        Humanity3_term=" "
        Humanity4_term=" "
        Science1_term=" "
        Science2_term=" "
        ScienceLab1_term=" "
        Extra1_term=" "
        Extra2_term=" "
        Extra3_term=" "
        Extra4_term=" "


        counter =0
        for semester in classList:
                  
                for clss in semester:
                        #print clss[1]
                        if " CAL-105" in clss[1]:
                                CAL105_grade =clss[2]
                                #print CAL105_grade
                                CAL105_term=writeTerm(counter,firstTerm)
                                #print CAL105_term
                        if " CH-117" in clss[1]:
                                CH117_grade =clss[2]
                                #print CH117_grade
                                CH117_term=writeTerm(counter,firstTerm)
                                #print CH117_term
                        if " CH-115" in clss[1]:
                                CH115_grade =clss[2]
                                #print CH115_grade
                                CH115_term=writeTerm(counter,firstTerm)
                                #print CH115_term
                        if " E-101" in clss[1]:
                                E101_grade =clss[2]
                                #print E101_grade
                                E101_term=writeTerm(counter,firstTerm)
                                #print E101_term
                        if " E-115" in clss[1]:
                                E115_grade =clss[2]
                                #print E115_grade
                                E115_term=writeTerm(counter,firstTerm)
                                #print E115_term
                        if " E-121" in clss[1]:
                                E121_grade =clss[2]
                                #print E121_grade
                                E121_term=writeTerm(counter,firstTerm)
                                #print E121_term
                        if " E-120" in clss[1]:
                                E120_grade =clss[2]
                                #print E120_grade
                                E120_term=writeTerm(counter,firstTerm)
                                #print E120_term
                        if " MA-121" in clss[1]:
                                MA121_grade =clss[2]
                                #print MA121_grade
                                MA121_term=writeTerm(counter,firstTerm)
                                #print MA121_term
                        if " MA-122" in clss[1]:
                                MA122_grade =clss[2]
                                #print MA122_grade
                                MA122_term=writeTerm(counter,firstTerm)
                                #print MA122_term
                        if " CAL-103" in clss[1]:
                                CAL103_grade =clss[2]
                                #print CAL103_grade
                                CAL103_term=writeTerm(counter,firstTerm)
                                #print CAL103_term	
                        if " E-122" in clss[1]:
                                E122_grade =clss[2]
                                #print E122_grade
                                E122_term=writeTerm(counter,firstTerm)
                                #print E121_term
                        if " MA-123" in clss[1]:
                                MA123_grade =clss[2]
                                #print MA123_grade
                                MA123_term=writeTerm(counter,firstTerm)
                                #print MA123_term
                        if " MA-124" in clss[1]:
                                MA124_grade =clss[2]
                                #print MA124_grade
                                MA124_term=writeTerm(counter,firstTerm)
                                #print MA124_term
                        if " MGT-103" in clss[1]:
                                MGT103_grade =clss[2]
                                #print MGT103_grade
                                MGT103_term=writeTerm(counter,firstTerm)
                                #print MGT103_term
                        if " PEP-111" in clss[1]:
                                PEP111_grade =clss[2]
                                #print PEP111_grade
                                PEP111_term=writeTerm(counter,firstTerm)
                                #print PEP111_term
                        if " E-126" in clss[1]:
                                E126_grade =clss[2]
                                #print E126_grade
                                E126_term=writeTerm(counter,firstTerm)
                                #print E126_term
                        if " E-231" in clss[1]:
                                E231_grade =clss[2]
                                #print E231_grade
                                E231_term=writeTerm(counter,firstTerm)
                                #print E231_term
                        if " E-245" in clss[1]:
                                E245_grade =clss[2]
                                #print E245_grade
                                E245_term=writeTerm(counter,firstTerm)
                                #print E245_term
                        if " MA-221" in clss[1]:
                                MA221_grade =clss[2]
                                #print MA221_grade
                                MA221_term=writeTerm(counter,firstTerm)
                                #print MA221_term
                        if " PEP-112" in clss[1]:
                                PEP112_grade =clss[2]
                                #print PEP112_grade
                                PEP112_term=writeTerm(counter,firstTerm)
                                #print PEP112_term
                        if " EE-250" in clss[1]:
                                EE250_grade =clss[2]
                                #print EE250_grade
                                EE250_term=writeTerm(counter,firstTerm)
                                #print EE250_term
                        if " EE-359" in clss[1]:
                                EE359_grade =clss[2]
                                #print EE359_grade
                                EE359_term=writeTerm(counter,firstTerm)
                                #print EE359_term
                        if " E-234" in clss[1]:
                                E234_grade =clss[2]
                                #print E234_grade
                                E234_term=writeTerm(counter,firstTerm)
                                #print E234_term
                        if " E-321" in clss[1]:
                                E321_grade =clss[2]
                                #print E231_grade
                                E321_term=writeTerm(counter,firstTerm)
                                #print E321_term
                        if " E-232" in clss[1]:
                                E232_grade =clss[2]
                                #print E232_grade
                                E232_term=writeTerm(counter,firstTerm)
                                #print E232_term
                        if " CPE-390" in clss[1]:
                                CPE390_grade =clss[2]
                                #print CPE390_grade
                                CPE390_term=writeTerm(counter,firstTerm)
                                #print CPE390_term
                        if " EE-471" in clss[1]:
                                EE471_grade =clss[2]
                                #print E126_grade
                                EE471_term=writeTerm(counter,firstTerm)
                                #print EE471_term
                        if " EE-348" in clss[1]:
                                EE348_grade =clss[2]
                                #print EE348_grade
                                EE348_term=writeTerm(counter,firstTerm)
                                #print EE348_term
                        if " E-355" in clss[1]:
                                EE355_grade =clss[2]
                                #print EE355_grade
                                E355_term=writeTerm(counter,firstTerm)
                                #print E355_term
                        if " IDE-400" in clss[1]:
                                IDE400_grade =clss[2]
                                #print IDE400_grade
                                IDE400_term=writeTerm(counter,firstTerm)
                                #print IDE400_term
                        if " EE-423" in clss[1]:
                                EE423_grade =clss[2]
                                #print EE423_grade
                                EE423_term=writeTerm(counter,firstTerm)
                                #print EE423_term
                        if " EE-465" in clss[1]:
                                EE465_grade =clss[2]
                                #print EE465_grade
                                EE465_term=writeTerm(counter,firstTerm)
                                #print EE465_term
                        if " IDE-401" in clss[1]:
                                IDE401_grade =clss[2]
                                #print IDE401_grade
                                IDE401_term=writeTerm(counter,firstTerm)
                                #print IDE401_term
                        if " EE-424" in clss[1]:
                                EE424_grade =clss[2]
                                #print EE424_grade
                                EE424_term=writeTerm(counter,firstTerm)
                                #print EE424_term
                        if " IDE-402" in clss[1]:
                                IDE402_grade =clss[2]
                                #print IDE402_grade
                                IDE402_term=writeTerm(counter,firstTerm)
                                #print IDE402_term
                        if " MA-134" in clss[1]:
                                MA134_grade =clss[2]
                                #print MA134_grade
                                MA134_term=writeTerm(counter,firstTerm)
                                #print MA134_term
                        if " CPE-360" in clss[1]:
                                CPE360_grade =clss[2]
                                #print CPE360_grade
                                CPE360_term=writeTerm(counter,firstTerm)
                                #print CPE360_term
                        if " CPE-487" in clss[1]:
                                CPE487_grade =clss[2]
                                #print CPE487_grade
                                CPE487_term=writeTerm(counter,firstTerm)
                                #print CPE487_term
                        if " CPE-462" in clss[1]:
                                CPE462_grade =clss[2]
                                #print CPE462_grade
                                CPE462_term=writeTerm(counter,firstTerm)
                                #print CPE462_term
                        if " CPE-345" in clss[1]:
                                CPE345_grade =clss[2]
                                #print CPE345_grade
                                CPE345_term=writeTerm(counter,firstTerm)
                                #print CPE345_term
                        if " CPE-322" in clss[1]:
                                CPE322_grade =clss[2]
                                #print CPE322_grade
                                CPE322_term=writeTerm(counter,firstTerm)
                                #print CPE322_term
                        if " CPE-423" in clss[1]:
                                CPE423_grade =clss[2]
                                #print CPE423_grade
                                CPE423_term=writeTerm(counter,firstTerm)
                                #print CPE423_term
                        if " CPE-490" in clss[1]:
                                CPE490_grade =clss[2]
                                #print CPE490_grade
                                CPE490_term=writeTerm(counter,firstTerm)
                                #print CPE490_term
                        if " CPE-424" in clss[1]:
                                CPE424_grade =clss[2]
                                #print CPE424_grade
                                CPE424_term=writeTerm(counter,firstTerm)
                                #print CPE424_term

                        if clss[0] == "Humanity" and hum1 is False:
                                Humanity1 = clss[1]
                                Humanity1_grade = clss[2]
                                Humanity1_term=writeTerm(counter,firstTerm)
                                hum1=True
                        elif clss[0] == "Humanity" and hum2 is False:
                                Humanity2 = clss[1]
                                Humanity2_grade = clss[2]
                                Humanity2_term=writeTerm(counter,firstTerm)
                                hum2=True
                        elif clss[0] == "Humanity" and hum3 is False:
                                Humanity3 = clss[1]
                                Humanity3_grade = clss[2]
                                Humanity3_term=writeTerm(counter,firstTerm)
                                hum3=True
                        elif clss[0] == "Humanity" and hum4 is False:
                                Humanity4 = clss[1]
                                Humanity4_grade = clss[2]
                                Humanity4_term=writeTerm(counter,firstTerm)
                                hum4=True

                        if clss[0] == "Technical" and tech1 == True:
                                Technical1 =clss[1]
                                Technical1_grade = clss[2]
                                Technical1_term=writeTerm(counter,firstTerm)
                                tech1=False
                        elif clss[0] == "Technical" and tech2 == True:
                                Technical2 =clss[1]
                                Technical2_grade = clss[2]
                                Technical2_term=writeTerm(counter,firstTerm)
                                tech2 == False
                        elif clss[0] == "Technical" and tech3 == True:
                                Technical3 =clss[1]
                                Technical3_grade = clss[2]
                                Technical3_term=writeTerm(counter,firstTerm)
                                tech3 == False
                        elif clss[0] == "Technical" and tech4 == True:
                                Technical4 =clss[1]
                                Technical4_grade = clss[2]
                                Technical4_term=writeTerm(counter,firstTerm)
                                tech4 == False

                        if clss[0] == "General" and gen1 == True:
                                General1 = clss[1]
                                General1_grade = clss[2]
                                General1_term=writeTerm(counter,firstTerm)
                                gen1 == False
                        elif clss[0] == "General" and gen2 == True:
                                General2 = clss[1]
                                General2_grade = clss[2]
                                General2_term=writeTerm(counter,firstTerm)
                                gen2 == False
                        elif clss[0] == "General" and gen3 == True:
                                General3 = clss[1]
                                General3_grade = clss[2]
                                General3_term=writeTerm(counter,firstTerm)
                                gen3 == False

                        if clss[0] == "Science" and sci1 is False:
                                Science1 = clss[1]
                                Science1_grade = clss[2]
                                Science1_term=writeTerm(counter,firstTerm)
                                sci1 = True	
                        elif clss[0] == "Science" and sci2 is False:
                                Science2 = clss[1]
                                Science2_grade = clss[2]
                                Science2_term=writeTerm(counter,firstTerm)
                                sci2 = True

                        if clss[0] == "ScienceLab" and scil1 is False:
                                ScienceLab1 = clss[1]
                                ScienceLab1_grade = clss[2]
                                ScienceLab1_term=writeTerm(counter,firstTerm)
                                scil1 = True	


                        if clss[0] == "Extra" and ext1 == False:
                                Extra1 = clss[1]
                                Extra1_grade = clss[2]
                                Extra1_term=writeTerm(counter,firstTerm)
                                ext1 = True
                        elif clss[0] == "Extra" and ext2 == False:
                                Extra2 = clss[1]
                                Extra2_grade = clss[2]
                                Extra2_term=writeTerm(counter,firstTerm)
                                ext2 = True

                        elif clss[0] == "Extra" and ext3 == False:
                                Extra3 = clss[1]
                                Extra3_grade = clss[2]
                                Extra3_term=writeTerm(counter,firstTerm)
                                ext3=True
                        elif clss[0] == "Extra" and ext4 == False:
                                Extra4 = clss[1]
                                Extra4_grade = clss[2]
                                Extra4_term=writeTerm(counter,firstTerm)
                                ext4=True
                counter =counter+1


        packet = StringIO.StringIO()
        # taking in inputs
##        name="Gina Schnecker"
##        ID="10300000"
##        classyear="2018"
##        mailbox="18-16"
##        email= "gschneck@stevens.edu"
##        spring1= "S17"
##        term3_hum="first elective"
##        term4_hum="second elective"
##        scienceelective="science"
##        sciencelab="laboratory"
##        grade1="A"
        #term1="S17"

        can = canvas.Canvas(packet, pagesize=letter)


        #personal info
        #can.drawString(70,505, name)
        #can.drawString(255,505, ID)
        #can.drawString(385,505, classyear)
        #can.drawString(460,505, mailbox)
        can.drawString(525,505, email)

        #term1 terms
        can.drawString(40,390, CH115_term)
        can.drawString(40,376, CH117_term)
        can.drawString(40,362, E101_term) 
        can.drawString(40,348, E115_term)
        can.drawString(40,334, E120_term)
        can.drawString(40,320, E121_term)
        can.drawString(40,308, MA121_term)
        can.drawString(40,296, MA122_term)
        can.drawString(40,284, CAL103_term)

        #term1 grades
        can.drawString(295,390, CH115_grade)
        can.drawString(295,376, CH117_grade)
        can.drawString(295,362, E101_grade) 
        can.drawString(295,348, E115_grade)
        can.drawString(295,334, E120_grade)
        can.drawString(295,320, E121_grade)
        can.drawString(295,308, MA121_grade)
        can.drawString(295,296, MA122_grade)
        can.drawString(295,284, CAL103_grade)

        #term2 terms
        can.drawString(40,230, Science1_term)
        can.drawString(40,218, ScienceLab1_term)
        can.drawString(40,204, E122_term) 
        can.drawString(40,190, MA123_term)
        can.drawString(40,176, MA124_term)
        can.drawString(40,162, MGT103_term)
        can.drawString(40,146, PEP111_term)
        can.drawString(40,132, CAL105_term)

        #term2 grades
        can.drawString(295,230, Science1_grade)
        can.drawString(295,218, ScienceLab1_grade)
        can.drawString(295,204, E122_grade) 
        can.drawString(295,190, MA123_grade)
        can.drawString(295,176, MA124_grade)
        can.drawString(295,162, MGT103_grade)
        can.drawString(295,146, PEP111_grade)
        can.drawString(295,132, CAL105_grade)

        #term3 terms
        can.drawString(360,390, E126_term)
        can.drawString(360,376, E231_term)
        can.drawString(360,362, E245_term) 
        can.drawString(360,348, MA221_term)
        can.drawString(360,334, PEP112_term)
        can.drawString(360,320, Humanity1_term)

        #term3 grades
        can.drawString(625,390, E126_grade)
        can.drawString(625,376, E231_grade)
        can.drawString(625,362, E245_grade) 
        can.drawString(625,348, MA221_grade)
        can.drawString(625,334, PEP112_grade)
        can.drawString(625,320, Humanity1_grade)

        #term4 term
        can.drawString(360,230, CPE360_term)
        can.drawString(360,218, CPE390_term)
        can.drawString(360,204, E232_term) 
        can.drawString(360,190, E234_term)
        can.drawString(360,176, MA134_term)
        can.drawString(360,162, Humanity2_term)

        #term4 grades
        can.drawString(625,230, CPE360_grade)
        can.drawString(625,218, CPE390_grade)
        can.drawString(625,204, E232_grade) 
        can.drawString(625,190, E234_grade)
        can.drawString(625,176, MA134_grade)
        can.drawString(625,162, Humanity2_grade)

        #humanities
        can.drawString(450,320, Humanity1)
        can.drawString(450,162, Humanity2)

        #science elective/lab
        can.drawString(150,230, Science1)
        can.drawString(185,218, ScienceLab1)

        can.save()

        #move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfFileReader(packet)
        # read your existing PDF
        existing_pdf = PdfFileReader(file("Computer_Engineering_2017.pdf", "rb"))
        output = PdfFileWriter()
        # add the "watermark" (which is the new pdf) on the existing page		
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)
        # finally, write "output" to a real file
        outputStream = file("CPE/newpdf"+fileName+".pdf", "wb")
        output.write(outputStream)
        outputStream.close()

        

#cpePage1(transcriptList, classList, "", "")
