from flask import Flask, render_template, request, redirect, session, flash, abort, url_for
app = Flask(__name__)
app.secret_key = 'ML_app'  # Set a secret key for session security

@app.route('/')
def index():
    return render_template('webpage.html')

