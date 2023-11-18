from flask import Flask, request, jsonify
from app import app
from app.repo.create_tables import *
from app.repo.create_cursor import connect_db
from sqlalchemy.exc import IntegrityError
import re
#signup is api. checking whether correct data is being recived
@app.route('/register', methods=['POST'])
def check_register():
    success = False
    msg = ''

    data = request.get_json()
    if data and 'name' in data and 'password' in data and 'email' in data:
        name = data['name']
        password = data['password']
        email = data['email']

        db = connect_db()
        
        # Check if the email already exists in the database
        existing_user = db.session.query(user_table).filter_by(email=email).first()

        if existing_user:
            msg = 'Account already exists'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', name):
            msg = 'Username must contain only characters and numbers!'
        elif not name or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Registration successful
            new_user = user_table(name=name, email=email, password=password,is_active=True)
            try:
                db.session.add(new_user)
                db.session.commit()
                success = True
                msg = 'You have successfully registered!'
            except IntegrityError:
                db.session.rollback()
                msg = 'An error occurred during registration. Please try again.'

    else:
        msg = 'Please fill out the form!'

    response_data = {
        'success': success,
        'message': msg
    }

    return jsonify(response_data)
