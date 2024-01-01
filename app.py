from flask import Flask, render_template, request, redirect, session, flash, abort, url_for
app = Flask(__name__)
app.secret_key = 'ML_app'  # Set a secret key for session security

@app.route('/')
def index():
    return render_template('webpage.html')

@app.route('/get-features', methods=['POST'])
def getFeatures():
    price = request.form['Buying']
    maint = request.form['maint']
    doors = request.form['doors']
    people = request.form['Persons']
    trunk = request.form['lug_boot']
    safety = request.form['safety']
    print(price, maint, doors, people, trunk, safety)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=8080)