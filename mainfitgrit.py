from flask import Flask, request,render_template,url_for
from fitgritemailer import send_email

app = Flask(__name__)
app.config['DEBUG'] = True#this reloads Flask app everytime I make changes to main.py

form = """
<!DOCTYPE HTML>
<html>
    <body>
        <form action="/hello" method='post'>
            <label for="myfirstname">My firstname</label>
            <input id="myfirstname" type="text" name="myfirstname" />
            <input type="submit" value="submit name now" />
        </form>
    </body>
</html>

"""
@app.route("/")
def index():
    return form
@app.route("/hello",methods=["POST"])
def hello():
    myfirstname = request.form['myfirstname']
    return '<h1> Hello, ' + myfirstname +'<h1>'

@app.route("/email",methods=["GET"])
def email():
    return render_template("fitgritaddList.html")
@app.route("/email",methods=["POST"])
def email_post():
    firstname= request.form["firstname"]
    email = request.form["email"]
    fitgrithours=request.form["fitgrithours"]
    print(firstname)
    print(email)
    print(fitgrithours)
    send_email(email,firstname,fitgrithours)
    return render_template("fitgritaddList.html")

app.run()
