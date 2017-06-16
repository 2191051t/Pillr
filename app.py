from flask import Flask, url_for, render_template, request, session, flash, redirect
import os
import web


def urltodb(url):
    url = url.replace('//', '').replace('@', ':').split(':')
    url[-1] = url[-1][url[-1].index('/') + 1:]
    return web.database(dbn=url[0], db=url[4], user=url[1], pw=url[2], host=url[3])


DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL is None:
    db = urltodb(
        'postgres://gmidudxcequwfh:6b2dc6b5aaaabd99b657660d646000dd3bc31e6d6c4d0762b722a93296431842@ec2-54-228-235-185.eu-west-1.compute.amazonaws.com:5432/dckaen6f7jcmrd')
else:
    db = urltodb(DATABASE_URL)
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/user/<int:id>')
def signup_user(id):

    q = list(db.select('users', where='id=' + str(id)))
    if len(q) == 0:
        #db.insert('users', id=id)
        # send to welcome page
        return render_template("signup.html", id=id)
    else:
        # send to current page
        return 'not done'


@app.route('/login/<id>', methods=['GET', 'POST'])
def login(id):
    error = None
    if request.method == 'POST':
        if request.form['drugName'] == "":
            error = 'Empty Drug Name'
        elif request.form['dosage'] == "":
            error = 'Empty Dosage'
        elif request.form['frequency'] == "":
            error = 'Empty frequency'
        else:
            #db.insert('users', id=id, drug=request.form['drugName'], dosage=request.form['dosage'], frequency=request.form['frequency'])
            session['logged_in'] = True
            flash('You were logged in')
            print "added"
            return "Logged in"


        return error

if __name__ == "__main__":
    # Bind to PORT if defined, otherwise default to 5000.
    app.run(debug=True)
