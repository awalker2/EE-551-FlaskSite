import smtplib
import datetime
from email.mime.nonmultipart import MIMENonMultipart
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEImage import MIMEImage
import base64
import itertools
import walkerScrape as scrape
fallSite = "http://personal.stevens.edu/~gliberat/registrar/17f/17f_u.html"
springSite = "http://personal.stevens.edu/~gliberat/registrar/18s/18s_u.html"
schedule = []
global b, conflict, count, count2, xlist
count2 = 0
count = 1
conflict = False

def sendPDF(fileName, email):
    smtp_ssl_host = 'smtp.gmail.com'
    smtp_ssl_port = 465
    username = 'stevensstudyplangenerator@gmail.com'
    password = 'Study123'
    sender = 'stevensstudyplangenerator@gmail.com'
    targets = [email]

    msg = MIMEMultipart()
    msg['Subject'] = 'Study Plan'
    msg['From'] = sender
    msg['To'] = ', '.join(targets)

    #Source for PDF send: https://bugs.python.org/issue9040
    fp = open(fileName, 'rb')
    attach = MIMENonMultipart('application', 'pdf')
    payload = base64.b64encode(fp.read()).decode('ascii')
    attach.set_payload(payload)
    attach['Content-Transfer-Encoding'] = 'base64'
    fp.close()
    attach.add_header('Content-Disposition', 'attachment', filename = 'StudyPlan.pdf')
    msg.attach(attach)
    #End of found fix

    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)

    server.sendmail(sender, targets, msg.as_string())

    server.quit()
    return "Sent study plan to: " + email

def perm(a, t):
    global b
    b = list(itertools.permutations(a, len(a)))

    xlist = a
    addClasses(a, t)
def lS2(c, a):
    global conflict
    conflict = False
    for i in xrange(len(schedule)):#need to check type and if list == true run thru that list
        if type(c[a]) == list and type(schedule[i]) == list:#and schedule[i] is a list
            for j in xrange(len(c[a])):
                for d in xrange(len(schedule[i])):
                    if c[a][j] == schedule[i][d]:
                        conflict = True
                        #print "Conflict!"
                        return
                    if j % 2 == 0 or j == 0:
                        if c[a][j] <= schedule[i][d] and c[a][j+1] >= schedule[i][d]:
                            conflict = True
                            #print "Conflict!"
                            return

    if conflict == False:
        schedule.append(c[0])
        schedule.append(c[a])

def addClasses(a, t):
    #print "Here"
    global conflict, count, count2,xlist
    count = 1#xlist[2] is where class times start
    for idx, j in enumerate(a):#go thru/number the list of classes
        #print "In for loop"
        if (t%2) != 0:
            class1 = scrape.courseScrape(j,fallSite)#nth class is class1
        else:
            class1 = scrape.courseScrape(j,springSite)
        if len(class1) == 1:
            x = str(class1[0]) + " isn't offered"
            #print x
            return x
            #exit()
        for i in range(1, len(class1)):
            #print "Next loop"
            lS2(class1,count)#search for conflict starting at first time
            if conflict:#if there's a conflict increment count to check next time
                count = count + 1
            else:
                count = 1#reset count if no conflict1
                #print "No conflict"
                break
            #print "Count",count
            if len(schedule)/2 == len(a):
                #print "Final schedule: ", schedule
                return True
                #exit()
            if count == (len(class1)):#delete schedule and rotate order and start again
                count = 1
                #print "Current Schedule: ", schedule
                del schedule[:]
                count2 = count2+1
                #a = rotate(a,idx)
                if count2 >= len(b):
                    #print "Sorry no possible schedule."
                    exit()
                else:
                    #print "NEW PERMUTATION"
                    addClasses(b[count2], t)
