from flask import Flask, redirect, url_for, render_template, request, session,flash
from datetime import timedelta 
app = Flask(__name__)
app.secret_key = "your_secret_key"  # Add a secret key for session management
#seesions store data only untill the browser is not closed
#using the below command we can store the session data for some time
app.permanent_sessions_lifetime=timedelta(minutes=5)
@app.route("/")

def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session['user'] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route('/user')
def user():
    if "user" in session:
        user = session["user"]  # Retrieve the user from the session
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop('user', None)
    flash("You have to been logeout","info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
