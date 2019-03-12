from flask import Flask
from flask import render_template

# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML templates
@app.route("/login")
def login():
    return render_template('Login-Page.html')
    return render_template('css.css')

@app.route("/register")
def register():
    return render_template('Register-Page.html')
    return render_template('style.css')

@app.route("/dashboard")
def dashboard():
    return render_template('Dashboard-Page.html')
    return render_template('style1.css')
# run the application
if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8080,debug=True)