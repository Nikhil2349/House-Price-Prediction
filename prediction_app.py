from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__, template_folder=r'C:\Users\Nikhil G\Documents\Projects\House price prediction\templates')
data=pd.read_csv('cleaned_datset.csv')
pipe=pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
   
    # Ensure all 'location' values are strings
    data['location'] = data['location'].fillna('Unknown').astype(str)
    
    locations = sorted(data['location'].unique())
    area_types = sorted(data['area_type'].fillna('Unknown').astype(str).unique())

    return render_template('prediction.html', locations=locations, area_types=area_types)
@app.route('/predict',methods=['POST'])
def predict():
    location=request.form.get('location')
    area_type=request.form.get('area_type')
    bhk=request.form.get('bhk')
    bath=request.form.get('bath')
    balcony=request.form.get('balcony')
    sqft=request.form.get('sqft')

    print(location,bhk,bath,sqft)
    input_data = pd.DataFrame([[location ,area_type, float(bhk), float(bath), float(balcony), float(sqft)]], columns=['location','area_type', 'BHK', 'bath','balcony', 'total_sqft'])
    print("Input Data:", input_data)
    prediction=pipe.predict(input_data)[0] * 100000
    return str(np.round(prediction,2))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
