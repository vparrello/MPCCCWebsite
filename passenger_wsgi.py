from flask import Flask, request, render_template, redirect, url_for

application = Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/currentparents')
def currentparents():
    return render_template('currentparents.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/ourstaff')
def ourstaff():
    return render_template('ourstaff.html')

@app.route('/programs')
def programs():
    return render_template('programs.html')

@app.route('/prospectiveparents')
def prospectiveparents():
    return render_template('prospectiveparents.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

if __name__ == "__main__":
    app.run(debug=True)