from flask import Flask, render_template, request
import re
app = Flask(__name__)

def addToCourseList(number, key, classes, dictionary):
    for x in range (1, number+1):
        try:
            term = int(dictionary[key+str(x)+"Term"])
            course = str(dictionary[key+str(x)])
            if (course):
                classes[int(term)].append(course)
        except:
            print "Error appending with key: " + key+str(x) + "/Term"
    return classes

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

    #Set up lists within a list for 8 semesters
    classes = []
    for x in range (0, 9):
        x = []
        classes.append(x)
    #Check and sanitize the user input
    #checkInput(data)
    
    #Set up a dictionary containing all classes desired
    dictionary = {}
    for value in data:
        dictionary[value] = data[value]

    #Use function to add all courses to the list
    classes = addToCourseList(4, "formHumanity", classes, dictionary)
    classes = addToCourseList(2, "formGeneral", classes, dictionary)
    classes = addToCourseList(2, "formScience", classes, dictionary)
    classes = addToCourseList(1, "formScienceLab", classes, dictionary)
    classes = addToCourseList(4, "formTechnical", classes, dictionary)
    classes = addToCourseList(6, "formExtra", classes, dictionary)
    print classes
    
    return "success"
    

if __name__ == "__main__":
    app.run()
