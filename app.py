from flask import Flask, url_for, render_template
import os
import web
#db = web.database(dbn='postgres', db='dbname', user='username', pw='password')


app = Flask(__name__)
#app.config.from_object(__name__)
#app.config.update(dict(
#    #DATABASE=os.path.join(app.root_path, 'pillar.db'),
#    SECRET_KEY='development key',
#    USERNAME='admin',
#    PASSWORD='default'
#))
#app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/signup/<int:id>')
def signup_user(id):
    # show signup page and have unique id
    return render_template('signup.html', id=id)

if __name__ == "__main__":
    # Bind to PORT if defined, otherwise default to 5000.
    #port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', debug=True)