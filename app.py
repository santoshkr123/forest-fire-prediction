import pickle
from flask import Flask, request, jsonify, render_template
import pandas as pd 
import numpy as np 
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

# Load the ridge regression model and the standard scaler
ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
standard_scaler_pickle = pickle.load(open('models/scaler.pkl', 'rb'))

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')  # Your main input form should be here

@app.route('/predictdata', methods=['POST', 'GET'])
def predict_datapoint():
    if request.method == 'POST':
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        # Make prediction
        new_data = [[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]]
        new_data_scaled = standard_scaler_pickle.transform(new_data)
        result = ridge_model.predict(new_data_scaled)

        return render_template('home.html', result=result[0])
    else:
        return render_template('home.html')  # Or redirect to index.html instead

if __name__ == "__main__": 
    app.run(debug=True)
