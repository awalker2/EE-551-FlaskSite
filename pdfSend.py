import smtplib
import datetime
from email.mime.nonmultipart import MIMENonMultipart
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEImage import MIMEImage
import base64

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
    try
    fp = open(fileName, 'rb')
    attach = MIMENonMultipart('application', 'pdf')
    payload = base64.b64encode(fp.read()).decode('ascii')
    attach.set_payload(payload)
    attach['Content-Transfer-Encoding'] = 'base64'
    fp.close()
    attach.add_header('Content-Disposition', 'attachment', filename = 'file.pdf')
    msg.attach(attach)
    #End of found fix

    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)

    server.sendmail(sender, targets, msg.as_string())

    server.quit()
    return "Sent study plan to: " + email

#sendPDF('test.pdf','awalker2@stevens.edu')
