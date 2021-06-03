#import packages
from flask import Flask,render_template,request,redirect
import json
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

#initializing global variables
__jsondata=[]
global __model
__locdata=[]


#app code
app=Flask(__name__)

@app.route("/")
def index():
    global __locdata
    global __jsondata
    with open("data/column_names.json",'r') as f:
        __jsondata=json.load(f)['columnnames']
        __locdata=__jsondata[3:]
    return render_template("index.html",locdata=__locdata)

@app.route('/',methods=['POST'])
def getvalue():
    #load model weights
    with open("data/model_weights.pickle",'rb') as f:
        __model=pickle.load(f)

    #get input data
    input_location=request.form['location']
    input_sqft=request.form['sqft']
    input_bedrooms=request.form['bhk']
    input_bathrooms=request.form['bathrooms']

    loc_index=-1
    #get the index of the input location in the list created to load json data.
    if input_location in __jsondata:
        loc_index=__jsondata.index(input_location)

    #create numpy array for inputs and pass it to predict function
    input=np.zeros(len(__jsondata))
    input[0]=input_sqft
    input[1]=input_bathrooms
    input[2]=input_bedrooms
    if loc_index!=-1:
        input[loc_index]=1
    result_price="Predicted Price: "+str(round(__model.predict([input])[0],3))+"Lakh Rupees..."
    return render_template('index.html',result_price=result_price,locdata=__locdata)

if __name__=="__main__":
    app.run(debug=True)