from flask import Flask, request, render_template, redirect, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Programs')
def programs():
    return render_template('Programs.html')

@app.route('/Registration')
def registration():
    return render_template('Registration.html')

application = app

if __name__ == "__main__":
    app.run(debug=True)