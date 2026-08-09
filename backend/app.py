
# Import necessary libraries
import numpy as np
import joblib                                   # For loading the serialized model
import pandas as pd                             # For data manipulation
from flask import Flask, request, jsonify       # For creating the Flask API

# Initialize the Flask app
superkart_api = Flask("SuperKart")

# Load the trained pipeline (preprocessing + model) once at startup
model = joblib.load("superkart_model.joblib")

# Home route - simple health check
@superkart_api.get('/')
def home():
    return "Welcome to the SuperKart System"

# Online (single) prediction endpoint
@superkart_api.post('/v1/predict')
def predict_sales():
    data = request.get_json()                   # read the JSON body
    # Assemble the 10 model features from the request
    sample = {
        'Product_Weight': data['Product_Weight'],
        'Product_Sugar_Content': data['Product_Sugar_Content'],
        'Product_Allocated_Area': data['Product_Allocated_Area'],
        'Product_MRP': data['Product_MRP'],
        'Store_Size': data['Store_Size'],
        'Store_Location_City_Type': data['Store_Location_City_Type'],
        'Store_Type': data['Store_Type'],
        'Product_Id_char': data['Product_Id_char'],
        'Store_Age_Years': data['Store_Age_Years'],
        'Product_Type_Category': data['Product_Type_Category'],
    }
    input_data = pd.DataFrame([sample])          # single-row DataFrame
    prediction = model.predict(input_data).tolist()[0]
    return jsonify({'Sales': prediction})        # return prediction as JSON

# Batch prediction endpoint
@superkart_api.post('/v1/predictbatch')
def predict_sales_batch():
    file = request.files['file']                 # uploaded CSV file
    input_data = pd.read_csv(file)               # read into a DataFrame
    predictions = model.predict(input_data).tolist()
    # Map each row index to its predicted sales
    output_dict = {str(i): round(pred, 2) for i, pred in enumerate(predictions)}
    return output_dict

# Run the app (Gunicorn is used in the container; this is for local runs)
if __name__ == '__main__':
    superkart_api.run(debug=True)
