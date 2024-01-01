from flask import Flask, render_template, request, redirect, session, flash, abort, url_for
app = Flask(__name__)
app.secret_key = 'ML_app'  # Set a secret key for session security

# Declare global variables
price = None
maint = None
doors = None
people = None
trunk = None
safety = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-features', methods=['POST'])
def getFeatures():
    price = request.form['buying']
    maint = request.form['maint']
    doors = request.form['doors']
    people = request.form['persons']
    trunk = request.form['lug_boot']
    safety = request.form['safety']
    print(price, maint, doors, people, trunk, safety)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=8080)