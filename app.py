from flask import Flask, request
from flask import render_template

# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML templates
@app.route("/login")
def login():
    return render_template('Login-Page.html')

@app.route("/register")
def register():
    return render_template('Register-Page.html')

@app.route("/dashboard")
def dashboard():
    return render_template('Dashboard-Page.html')

@app.route("/login_submit",methods=["POST"])
def login_submit():
    username = request.form['username']
    password = request.form['password']
    print(username,password)
    return render_template('Dashboard-Page.html',username=username)

@app.route("/register_submit",methods=["POST"])
def register_submit():
    Firstname = request.form['fname']
    Middlename = request.form['mname']
    Lastname = request.form['lname']
    username = request.form['username']
    password = request.form['password']
    rpassword = request.form['rpassword']
    print(Firstname, Middlename, Lastname, username, password, rpassword)
    return render_template('Dashboard-Page.html', username=username)



@app.route("/dashboard_logout", methods=["POST"])
def dashboard_logout():

    return render_template('Login-Page.html')

# run the application
if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8080,debug=True)