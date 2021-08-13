import numpy as np
import pandas as pd
import pickle
from flask import  Flask, render_template, url_for, request, jsonify
from flask_cors import cross_origin

app = Flask(__name__, template_folder="template")
model = pickle.load(open("./models/rf.pkl", "rb"))
print("Model Loaded")

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template("predict.html")

@app.route("/predict", methods=['GET', 'POST'])
@cross_origin()
def predict():
    if request.method == "POST":
        #variance
        variance = request.form['variance']
        #skewness
        skewness = request.form['skewness']
        #curtosis
        curtosis = request.form['curtosis']
        #entropy
        entropy = request.form['entropy']

        input_lst = [[variance, skewness, curtosis, entropy ]]
        pred = model.predict(input_lst)
        output = pred
        if output == 0:
            return render_template('predict.html', prediction_text = "This is an unauthenticated note!")
        if output ==1:
            return render_template('predict.html', prediction_text = "This is an authenticated note!")
    return render_template("predict.html")    

if __name__=='__main__':
    app.run(debug=True)