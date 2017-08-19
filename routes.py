from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bcrypt import Bcrypt
from User import User
import db

from nocache import nocache

app = Flask(__name__)
bcrypt = Bcrypt(app)
error = None

@app.route('/')
@nocache
def hello_world():
    db.get_db()
    return render_template('home.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/', methods=['POST', 'GET'])
def login():

    txt_uname = request.form['uname']
    txt_passwd = request.form['passwd']
    error = 'Invalid username or password. Please try again!'

    if txt_uname == "" or txt_passwd == "":
        flash("Require username and password")

    if request.form['submit'] == "Login":

        uquery = db.query_db("SELECT * from Users WHERE Username = ?", [txt_uname], one=True)

        if uquery is None:
            print ('No such user')
            return render_template('home.html', error=error)
            flash("TRASH")
        else:
            print ("User exists")
            return redirect(url_for('hello_world'))

        # uquery[1] is username; [2] is pw from uquery

        # cpuser = User (uquery[1])

        # CHANGE THIS LATER
        # cpuser.pw_hash = user.set_password("resolve")

        print (user.pw_hash)
        print ("Input hash:")
        print (cpuser.pw_hash)
        print ("\n")

        user.check_password (txt_passwd)

        print ("Query hash:\n")
        print ()

        if user.check_password(txt_passwd) == True:
            print ('YES')
            return redirect(url_for('login', user=user))

        else:
            print ('NO')
            return redirect(url_for('hello_world'))

    elif request.form['submit'] == "Register":
        uquery = db.query_db("SELECT * from Users WHERE Username = ?", [txt_uname], one=True)
        if uquery == None:
            user = User(txt_uname, txt_passwd)
            # print(user.pw_hash)
            db.commit_db("INSERT INTO Users (Username, Password) VALUES (?,?)",
                         (txt_uname, user.pw_hash))
            user = None
            return render_template('home.html', error=error)

        else:
            print("This user already exists")
            return redirect(url_for('hello_world'))



if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True)
