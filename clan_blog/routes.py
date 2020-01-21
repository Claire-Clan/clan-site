""" Set default routes for app """
from flask import current_app as app, db
from flask import render_template, url_for

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html') # Incomplete
