from flask import Flask, jsonify, request, render_template
from project_app.utils import MedicalInsurance
import numpy as np
app = Flask(__name__)

##########################################################################################
  ################################ Homepage API ########################################
##########################################################################################

@app.route('/')
def homepage():
    print('Medical Insurance Project')
    return render_template('Medical_Health_Insurance.html')

##########################################################################################
################################ Prediction API ########################################
##########################################################################################

@app.route('/predict_charges',methods = ['POST','GET'])
def get_insurance_charges():
    if request.method == 'POST':
        print('We are in POST Method')
        data = request.form
        name=request.form['name']
        sex=request.form['sex']
        age = eval(data['age'])
        bmi = eval(data['bmi'])
        children = eval(data['children'])
        smoker = request.form['smoker']
        region = data['region']
        print(data)
        print(f'age >> {age}, sex >>{sex} , bmi >> {bmi}, children >> {children}, smoker >> no, region >> {region} ')
        med_ins = MedicalInsurance(age, sex, bmi, children,smoker, region)    
        Charges = med_ins.get_predicted_charges()
        return render_template('Result.html',name=name,Charges=Charges)
        # return jsonify({f'Hello {name}': f' Your Predicted Medical Insurance Charges are:  RS.{Charges} '})
        
app.run()