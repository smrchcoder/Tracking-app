from app import app

from flask import Flask, request, jsonify,render_template
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
def home():
      return render_template('sample.html')
@app.route('/login')
def login():
      return render_template('login.html')
@app.route('/signup')
def signup():
      return render_template('signup.html')

@app.route('/path')
@login_required
def admin_menu():
      return render_template('path.html')
@app.route('/insertshuttle')
@login_required
def insertshuttle():
      
      return render_template('shuttle.html')
@app.route('/addcordinate')
@login_required
def addcordinate():
      return render_template('index.html') 

