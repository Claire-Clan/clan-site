from htdoc import app
from flask import render_template, url_for, redirect

@app.route('/')
def landing_page():
    return render_template('index.html')
