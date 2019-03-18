from flask import Flask, request
from flask import render_template
from redis import Redis, RedisError
import os
import socket
import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["project1"]

mycol = mydb["student"]

# creates a Flask application, named app
app = Flask(__name__)

# connect a redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

# a route where we will display a welcome message via an HTML templates
@app.route("/login")
def login():
    try:
        visits = redis.incr("counter")
        return render_template('Login-Page.html')
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>login {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("USERNAME", "project"), hostname=socket.gethostname(), visits=visits)


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
    login_sumbit = mycol.find_one({'name': username,'password':password})
    if login_sumbit:
        return render_template('Dashboard-Page.html',username=username)
    return "Invalid Username"

@app.route("/register_submit",methods=["POST"])
def register_submit():
    if request.method == 'POST':
        Firstname = request.form['fname']
        Middlename = request.form['mname']
        Lastname = request.form['lname']
        username = request.form['username']
        password = request.form['password']
        rpassword = request.form['rpassword']
        print(Firstname, Middlename, Lastname, username, password, rpassword)

        existing_user = mycol.find_one({'name' : username})

        if existing_user is None:
            mycol.insert({'fname':Firstname,'mname': Middlename,'lname':Lastname,'name' : username,'password' : password,'rpassword':rpassword})
            return render_template('Dashboard-Page.html', username=username)
        return 'That user Already Exists'
    return render_template('register.html')




@app.route("/dashboard_logout", methods=["POST"])
def dashboard_logout():

    return render_template('Login-Page.html')

# run the application
if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8080,debug=True)