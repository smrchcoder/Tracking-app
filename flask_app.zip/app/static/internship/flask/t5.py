from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Add a secret key for session management
app.permanent_session_lifetime = timedelta(minutes=5)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db=SQLAlchemy(app)
class users(db.Model):
    _id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))
    def __init__(self, name,email):
        self.name=name
        self.email=email
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session['user'] = user
        # after creating the user check if the user already exist in the database
        found_user=users.query.filter_by(name=user).first()
        if found_user:
            session["email"]=found_user.email
        else:
            #adding the instance on to the database
            usr=users(user,"")
            db.session.add(usr)
            db.commit()
        flash("Login successful", "success")
        return redirect(url_for("user"))
    else:
        flash("Already logged in", "info")
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route('/user', methods=["POST", "GET"])
def user():
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            email = request.form['email']
            found_user=users.query.filter_by(name=user).first()
            found_user.email=email
            db.commit()
            session["email"] = email
        else:
            if "email" in session:
                email = session["email"]
            else:
                email = None  # Set a default value if email is not in session
        return render_template("user.html", email=email)
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" in session:
        session.pop('user', None)
        flash("You have been logged out", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
