def scrapeTranscript(openfile):
    newlist=[]
    grades=['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','D-','F+','F','F-','P','IP']
    bbool=False
    termnumber=1
    for line in openfile:
        line1 = str.split(line)
        if "----------" in line and ('20' in line or '19' in line):
            #print "\n"+line
            newlist.append(line)
            if termnumber<=3:
                stermnumber="I"*termnumber
            elif termnumber==4:
                stermnumber="IV"
            elif termnumber<9:
                stermnumber="V"+"I"*(termnumber-5)
            elif termnumber==9:
                stermnumber="IX"
            else:
                stermnumber="X"+"I"*(termnumber-10)
            #print "TERM "+str(stermnumber)+ "\n"
            #newlist.append("TERM "+str(stermnumber))
            termnumber+=1
        if bbool:
            try:
                q=line1[-3]
                if q in grades:
                    sprev=prevline.split(" ")
                    sprev2=sprev[1]
                    if "-" in sprev2:
                        #print prevline+q
                        newlist.append(prevline+q)
                else:
                    sprev=prevline.split(" ")
                    sprev2=sprev[1]
                    if "-" in sprev2:
                        #print prevline
                        newlist.append(prevline)
   
            except:
                try:
                    q=line1[-2]
                    if q in grades:
                        sprev=prevline.split(" ")
                        sprev2=sprev[1]
                        if "-" in sprev2:
                            #print prevline+q
                            newlist.append(prevline+q)
                    else:
                        #print prevline
                        newlist.append(prevline)
                except:
                    try:
                        q=line1[-1]
                        if q in grades:
                            sprev=prevline.split(" ")
                            sprev2=sprev[1]
                            if "-" in sprev2:
                                #print prevline+q
                                newlist.append(prevline+q)
                        else:
                            sprev=prevline.split(" ")
                            sprev2=sprev[1]
                            if "-" in sprev2:
                                #print prevline
                                newlist.append(prevline)
                    except:
                        sprev=prevline.split(" ")
                        sprev2=sprev[1]
                        if "-" in sprev2:
                            #print prevline
                            newlist.append(prevline)
            bbool=False
        if "TM" in line1 or "TG" in line1 or "SYS" in line1 or "SSW" in line1 or "SOC" in line1 or "SM" in line1 or "SES" in line1 or "REG" in line1 or "QF" in line1 or "PME" in line1 or "PIN" in line1 or "OE" in line1 or "NIS" in line1 or "NE" in line1 or "NANO" in line1 or "MT" in line1 or "MIS" in line1 or "ME" in line1 or "LFR" in line1 or "ISE" in line1 or "IPD" in line1 or "HST" in line1 or "HSS" in line1 or "FIN" in line1 or "FE" in line1 or "ES" in line1 or "EN" in line1 or "EMT" in line1 or "EM" in line1 or "ELC" in line1 or "CM" in line1 or "CHE" in line1 or "CE" in line1 or "BT" in line1 or "BME" in line1 or "BIO" in line1 or "BIA" in line1 or "CS" in line1 or "CAL" in line1 or "CH" in line1 or "E" in line1 or "MA" in line1 or "MGT" in line1 or "PEP" in line1 or "EE" in line1 or "CPE" in line1 or "HSS" in line1 or "PRV" in line1 or "TG" in line1 or "BT" in line1 or "IDE" in line1 or "HMU" in line1 or "HAR" in line1 or "HHS" in line1 or "LSP" in line1 or "HLI" in line1 or "HMU" in line1 or "HPL" in line1 or "COMM" in line1 or "HST" in line1 or "HTH" in line1 or "D" in line1:
            line2 = ("Class: " + line1[0] + line1[1] + " " + "Grade: " + line1[-3])
            if line1[-3] not in grades:
                if line1[-2] in grades:
                    line2 = ("Class: " + line1[0] + line1[1] + " " + "Grade: " + line1[-2])
                    #print line2
                    newlist.append(line2)
                else:
                    bbool=True
                    prevline=("Class: " + line1[0] + line1[1] + " " + "Grade: ")
            else:
                #print line2
                newlist.append(line2)
        if "PE" in line1:
            if line1[-2] in grades:
                line2 = ("Class: " + line1[0] + line1[1] + " " + "Grade: " + line1[-2])
                #print line2
                newlist.append(line2)
            else:
                line2 = ("Class: " + line1[0] + line1[1] + " " + "Grade: ")
                #print line2
                newlist.append(line2)
        
    newlist.append("Number of terms taken: " + str(termnumber))

    return newlist

#with open("UnofficialTranscript.txt") as openfile:
    #print scrapeTranscript(openfile)
