# conventional way to import pandas
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

def get_rating(car_eval_features):
    # car_eval_features = [['vhigh', 'vhigh', '2', '2', 'small', 'low']]
    input_df = pd.DataFrame(car_eval_features, columns=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety'])
    inputs = {c: input_df[c].values for c in input_df.columns}
    for k in inputs:
        inputs[k] = inputs[k].reshape((inputs[k].shape[0], 1))
    sess = rt.InferenceSession("ML_model/pipeline_car_eval.onnx")
    outputs = sess.run(None,inputs)
    car_eval_class = outputs[0]
    return car_eval_class

car_eval_features = [['vhigh', 'vhigh', '2', '2', 'small', 'low']]
car_eval_class = get_rating(car_eval_features)
print(car_eval_class)




# car_eval_features = [['med', 'low', '5more', '4', 'big', 'med']]
# input_df = pd.DataFrame(car_eval_features, columns=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety'])
# inputs = {c: input_df[c].values for c in input_df.columns}
# for k in inputs:
#     inputs[k] = inputs[k].reshape((inputs[k].shape[0], 1))
# outputs = sess.run(None,inputs)
# car_eval_class = outputs[0]
# #probabilities = outputs[1]
# #confidence_class = car_eval_class[0]
# print(car_eval_class)