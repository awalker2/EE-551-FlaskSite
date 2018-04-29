from flask import Flask, render_template, request, send_file
import helperFunctions as helper
#import dannyHelper
import conflictCheck
from subprocess import check_output

app = Flask(__name__)
        
@app.route("/")
def main():
    return render_template('home.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route('/generate', methods = ['POST'])
def generate():
    #Check if transcript was uploaded
    transcript = request.files.get('formTranscript')
    if transcript:
        #for line in transcript:
            print "test"
        
    else:
        return "No transcript uploaded"
    data = request.form

    #Set up lists within a list for 9 semesters, semester 0 is taken already
    classes = []
    for x in range (0, 9):
        x = []
        classes.append(x)
    
    #Set up a dictionary containing all classes desired
    dictionary = {}
    major = None
    for value in data:
        dictionary[value] = data[value]
        if dictionary[value] == "CPE2017" or dictionary[value] == "EE2017":
            major = dictionary[value]
            print major
        if value == "formEmail":
            email = dictionary[value]
            print email

    #Standardize the user input for courses
    helper.standardizeInput(dictionary)

    #Use function to add all courses to the list
    helper.addDictToCourseList(4, "formHumanity", classes, dictionary)
    helper.addDictToCourseList(2, "formGeneral", classes, dictionary)
    helper.addDictToCourseList(2, "formScience", classes, dictionary)
    helper.addDictToCourseList(1, "formScienceLab", classes, dictionary)
    helper.addDictToCourseList(4, "formTechnical", classes, dictionary)
    helper.addDictToCourseList(6, "formExtra", classes, dictionary)
    helper.addDictToCourseList(1, "formExtraLab", classes, dictionary, "L")
    helper.addDictToCourseList(1, "formExtraRec", classes, dictionary, "R")

    #Add in the required courses if CPE or EE
    if (major == "EE2017"):
        classList = [
                     "CH 115", 1, "CH 117", 1, "E 101", 1, "E 121", 1, "E 120", 1,
                     "E 115", 1, "MA 121", 1, "CAL 103", 1,
                     "E 122", 2, "MA 123", 2, "PEP 111", 2, "CAL 105", 2, "MGT 103", 2,
                     "MA 221", 3,"MA 221R", 3, "PEP 112", 3, "PEP 112R", 3, "E 126", 3,
                     "E 245", 3, "E 245L", 3,"E 231", 3,
                     "EE 250", 4, "E 232", 4, "E 232L", 4, "E 234", 4, "E 234R", 4,
                     "CPE 390", 4, "CPE 390L", 4, "EE 359", 4,
                     "EE 471", 5, "E 344", 5, "E 321", 5, "E 243", 5, "E 243R", 5, "EE 348", 5,
                     "EE 345", 6, "E 355", 6, "EE 322", 6, "EE 448", 6, "IDE 400", 6,
                     "EE 465", 7, "EE 423", 7, "IDE 401", 7,
                     "EE 424", 8, "IDE 402", 8
                    ]
    elif (major == "CPE2017"):
        classList = [
                     "CH 115", 1, "CH 117", 1, "E 101", 1, "E 121", 1, "E 120", 1,
                     "E 115", 1, "MA 121", 1, "CAL 103", 1,
                     "E 122", 2, "MA 123", 2, "PEP 111", 2, "CAL 105", 2, "MGT 103", 2,
                     "MA 221", 3, "MA 221R", 3, "PEP 112", 3, "PEP 112R", 3, "E 126", 3,
                     "E 245", 3, "E 245L", 3, "E 231", 3,
                     "MA 134", 4, "E 232", 4, "E 232L", 4, "E 234", 4, "E 234R", 4,
                     "CPE 360", 4, "CPE 390L", 4, "CPE 390", 4,
                     "EE 471", 5, "E 344", 5, "E 321", 5, "E 243", 5, "E 243R", 5, "CPE 487", 5,
                     "EE 345", 6, "E 355", 6, "CPE 322", 6, "CPE 462", 6, "IDE 400", 6,
                     "CPE 490", 7, "CPE 423", 7, "IDE 401", 7,
                     "CPE 424", 8, "IDE 402", 8
                    ]
    else:
        return "Major invalid"

    #Add the required courses to the list
    helper.addListToCourseList(classList, classes)
    print classes

    #Clean up lists to be handled by conflict function, then test for time conflicts/bad input
    errorString = ""
    for x in xrange(1, 9):
        checkList = classes[x]
        c = 0
        for item in checkList:
            if ":" in item:
                temp = checkList[c].split(":")
                checkList[c] = temp[1]
                c = c + 1
        #Check for conflicts/valid classes for every term that hasn't been taken
        if x > 2:
            check = conflictCheck.checkAllForConflict(checkList, x)
            if (check != "no conflict"):
                errorString = errorString + "Term: " + str(x) + ":\n" + check

    #Either return the pdf file or return a string with a list of potential issues
    if (errorString != ""):
        return errorString
    else:
        return "test.pdf"

@app.route("/pdf")
def sendPDF():
    fileName = request.args.get("fileName")
    if (fileName != None and ".pdf" in fileName):
        return send_file(fileName,attachment_filename=fileName, mimetype='application/pdf', as_attachment=True)
    else:
        return "Error obtaining file"
   
@app.route('/snipe', methods = ['POST'])
def snipe():
    data = request.form
    #Try to run the registration script, not running means another instance already or bad crecentials
    try:
        check_output(["python","seleniumRegister.py", data["formUser"], data["formPass"], data["formCall1"], data["formCall2"],
                    data["formCall3"], data["formCall4"], data["formCall5"], data["formCall6"], data["formCall7"],
                    data["formCall8"], data["formCall9"], data["formCall10"]])
    except:
            return "Unable to register for classes - another current user or wrong credentials"
    return "Registration Attempted"
        

if __name__ == "__main__":
    app.run()
