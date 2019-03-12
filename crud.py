from flask import Flask, request
app = Flask(__name__)

@app.route('/login',methods['GET'])
def login_p():
    if request.method='GET':
        username = request.form['username']
        password = request.form['password']

        login = request.form['login']

        return render_template("Login-Page.html",username=username)
        return render_template("Login-Page.html",password=password)
        return render_template("Login-Page.html",login=login)

@app.route('/register',methods['GET'])
def register_p():
    if request.method='GET':
        firstname = request.form['firstname']
        middlename = request.form['middlename']
        lastname = request.form['lastname']
        mobile = request.form['mobile']
        email = request.form['email']
        password = request.form['password']
        repassword = request.form['repassword']
        male = request.form['male']
        female = request.form['female']
        other = request.form['other']
        submit = request.form['submit']

        return render_template("Register-Page.html", firstname=firstname)
        return render_template("Register-Page.html", middlename=middlename)
        return render_template("Register-Page.html", lastname=lastname)
        return render_template("Register-Page.html", mobile=mobile)
        return render_template("Register-Page.html", email=email)
        return render_template("Register-Page.html", password=password)
        return render_template("Register-Page.html", repassword=repassword)
        return render_template("Register-Page.html", male=male)
        return render_template("Register-Page.html", female=female)
        return render_template("Register-Page.html", other=other)
        return render_template("Register-Page.html", submit=submit)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080,debug=True)