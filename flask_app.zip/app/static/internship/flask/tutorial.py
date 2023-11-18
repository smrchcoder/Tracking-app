from flask import Flask,redirect,url_for
app=Flask(__name__)
@app.route("/")
def home():
    return "HI"
@app.route("/<name>")
def user(name):
    return f"Home{name}"
@app.route('/admin')
def admin():
    return redirect(url_for("user",name="Adimn"))
if(__name__=="__main__"):
    app.run()
