from flask import Flask, render_template, request
import helperFunctions as helper
app = Flask(__name__)
        
@app.route("/")
def main():
    return render_template('home.html')

@app.route('/generate', methods = ['POST'])
def generate():
    #Check if transcript was uploaded
    transcript = request.files.get('formTranscript')
    if transcript:
        transcript.read()
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

    #Standardize the user input for courses
    helper.standardizeInput(dictionary)

    #Use function to add all courses to the list
    helper.addDictToCourseList(4, "formHumanity", classes, dictionary)
    helper.addDictToCourseList(2, "formGeneral", classes, dictionary)
    helper.addDictToCourseList(2, "formScience", classes, dictionary)
    helper.addDictToCourseList(1, "formScienceLab", classes, dictionary)
    helper.addDictToCourseList(4, "formTechnical", classes, dictionary)
    helper.addDictToCourseList(6, "formExtra", classes, dictionary)

    #Add in the required courses if CPE or EE
    if (major == "EE2017"):
        classList = [
                     "CH 115", 1, "CH 117", 1, "E 101", 1, "E 121", 1, "E 120", 1,
                     "E 115", 1, "MA 121", 1, "CAL 103", 1,
                     "E 122", 2, "MA 123", 2, "PEP 111", 2, "CAL 105", 2, "MGT 103", 2,
                     "MA 221", 3, "PEP 112", 3, "E 126", 3, "E 245", 3, "E 231", 3,
                     "EE 250", 4, "E 232", 4, "E 234", 4, "CPE 390", 4, "EE 359", 4,
                     "EE 471", 5, "E 344", 5, "E 321", 5, "E 243", 5, "EE 348", 5,
                     "EE 345", 6, "E 355", 6, "EE 322", 6, "EE 448", 6, "IDE 400", 6,
                     "EE 465", 7, "EE 423", 7, "IDE 401", 7,
                     "EE 424", 8, "IDE 402", 8
                    ]
    elif (major == "CPE2017"):
        classList = [
                     "CH 115", 1, "CH 117", 1, "E 101", 1, "E 121", 1, "E 120", 1,
                     "E 115", 1, "MA 121", 1, "CAL 103", 1,
                     "E 122", 2, "MA 123", 2, "PEP 111", 2, "CAL 105", 2, "MGT 103", 2,
                     "MA 221", 3, "PEP 112", 3, "E 126", 3, "E 245", 3, "E 231", 3,
                     "MA 134", 4, "E 232", 4, "E 234", 4, "CPE 360", 4, "CPE 390", 4,
                     "EE 471", 5, "E 344", 5, "E 321", 5, "E 243", 5, "CPE 487", 5,
                     "EE 345", 6, "E 355", 6, "CPE 322", 6, "CPE 462", 6, "IDE 400", 6,
                     "CPE 490", 7, "CPE 423", 7, "IDE 401", 7,
                     "CPE 424", 8, "IDE 402", 8
                    ]
    else:
        return "Major invalid"

    #Add the required courses to the list
    helper.addListToCourseList(classList, classes)

    print classes
    return "success"
    

if __name__ == "__main__":
    app.run()
