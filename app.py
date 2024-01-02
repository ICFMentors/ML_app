from flask import Flask, render_template, request, redirect, session, flash, abort, url_for
import pandas as pd
import numpy as np
import pprint
from numpy.testing import assert_almost_equal
import onnx
from onnx.tools.net_drawer import GetPydotGraph, GetOpNodeProducer
import onnxruntime as rt
import skl2onnx
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType, StringTensorType
from skl2onnx.common.data_types import Int64TensorType
from model import get_rating
app = Flask(__name__)
app.secret_key = 'ML_app'  # Set a secret key for session security

# Declare global variables
price = ""
maint = ""
doors = ""
people = ""
trunk = ""
safety = ""

@app.route('/')
def index():
    return render_template('index.html', rating=0)

@app.route('/get-features', methods=['POST'])
def getFeatures():
    price = request.form['buying']
    maint = request.form['maint']
    doors = request.form['doors']
    people = request.form['persons']
    trunk = request.form['lug_boot']
    safety = request.form['safety']
    car_eval_features = [[price, maint, doors, people, trunk, safety]]
    print(car_eval_features)
    car_eval_class = get_rating(car_eval_features)
    print(car_eval_class)
    return render_template('index.html', rating=car_eval_class)

if __name__ == '__main__':
    app.run(debug=True, port=8080)