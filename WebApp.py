from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('home.html')

@app.route('/generate', methods = ['POST'])
def generate():
    print request.files
    transcript = request.files.get('formTranscript')
    print transcript.read()
    data = request.form
    for key in data:
        print key + ": " + data[key]
    return "success"

if __name__ == "__main__":
    app.run()
