from flask import Flask, request, jsonify, session
from app import app
from app.repo.create_tables import *
from app.repo.create_cursor import connect_db
from sqlalchemy.orm.exc import NoResultFound
from flask_login import login_user, logout_user, login_required, current_user
#added the user to login manneger
@app.route('/checklogin', methods=['POST'])
def checklogin():
    success = False
    msg = ''

    data = request.get_json()
    if 'email' in data and 'password' in data:
        email = data['email']
        password = data['password']

        db = connect_db()

        try:
            # Query the database for the user with the provided email
            user = db.session.query(user_table).filter_by(email=email).one()
       
            if user and user.password == password:
                session['loggedin'] = True
                session['id'] = user.id
                session['email'] = user.email
                success = True
                login_user(user)
                msg = "Logged in successfully"
            else:
                msg = "Incorrect email or password."
        except NoResultFound:
            msg = "User not found."
    else:
        msg = "Invalid request format."

    response_data = {
        'success': success,
        'message': msg
    }
    return jsonify(response_data)


#user can only access this api if logged in
@app.route('/logout')
@login_required
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('email', None)
    logout_user()
    return 'Logged out'