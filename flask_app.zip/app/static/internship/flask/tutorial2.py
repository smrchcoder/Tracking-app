from flask import Flask,redirect,url_for,render_template
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
if(__name__=="__main__"):
    app.run(debug=True)
#get means getting information which  is not secured
#post is getting information which is encrypted
