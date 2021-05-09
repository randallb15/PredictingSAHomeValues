
from flask import Flask, request, render_template, url_for, redirect
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from datetime import date
import random

# Initialize app
app = Flask(__name__)

# load the pickled model
with open('data/model_rfr_locations.pkl', 'rb') as f:
    model = pickle.load(f)
    
flaskdf = pd.read_pickle('data/flaskdf.pkl')
locations_list = flaskdf.LOCATION.unique()
locations_list.sort()

zips_list = flaskdf['ZIP OR POSTAL CODE'].unique()
zips_list.sort()


#N = random.choice(locations_list)



# # load the pickled training data to display with prediction
# with open('data/trainXY.pkl', 'rb') as f:
#     trainXY = pickle.load(f)

# trainX = trainXY[:,:2]
# trainY = trainXY[:,2]

# Home page with form on it to submit new data
@app.route('/')
def get_new_data():
    

    flaskdf = pd.read_pickle('data/flaskdf.pkl')
    locations_list = flaskdf.LOCATION.unique()
    locations_list.sort()
    #     zips = zips_list
    return render_template('dropdown.html', locations_list=locations_list)


@app.route('/predict', methods = ["GET", "POST"])
def predict():
    # request the text from the form 
    Address = str(request.form['Address'])
    Bedrooms = float(request.form['Bedrooms'])
    Bathrooms = float(request.form['Bathrooms'])
    Neighborhood = (request.form['locations_list'])
    Zip = float(request.form['Zip Code'])
    SqFt = float(request.form['Square Feet'])
    YearBuilt = float(request.form['YearBuilt'])
    Lot = float(request.form['Lot Size'])
    Month = date.today().month
    Yeartoday = date.today().year
    #Placeholders for latitude and longitude and HOA
    Lat = 29.483
    Long = -98.51
    HOA = 0 

    locations_df = pd.read_pickle('data/locations_df.pkl')
    oneline = locations_df.sample().drop('PRICE',axis=1)
    for col in oneline.columns:
        oneline[col].values[:] = 0
    oneline.at[oneline.index,Neighborhood] = 1
    oneline.at[oneline.index,'SQUARE FEET'] = SqFt
    oneline.at[oneline.index,'ROOMS'] = Bedrooms + Bathrooms
    oneline.at[oneline.index,'ZIP OR POSTAL CODE'] = Zip
    oneline.at[oneline.index,'YEAR'] = Yeartoday
    oneline.at[oneline.index,'MONTH'] = Month
    oneline.at[oneline.index,'LOT SIZE'] = Lot
    oneline.at[oneline.index,'HOA/MONTH'] = HOA
    oneline.at[oneline.index,'LATITUDE'] = Lat
    oneline.at[oneline.index,'LONGITUDE'] = Long
    oneline.at[oneline.index,'YEAR BUILT'] = YearBuilt
    oneline_array = oneline.to_numpy()
    
    #X_n = np.array([[Zip, SqFt, Lot, Year, HOA, Lat, Long, (Bedrooms+Bathrooms), Month,Yeartoday]])
    
    # predict on the new data
    Y_pred = model.predict(oneline_array)

    '''
    # for plotting 
    X_0 = trainX[trainY == 0] # class 0
    X_1 = trainX[trainY == 1] # class 1
    X_2 = trainX[trainY == 2] # class 2
    
    # color-coding prediction 
    if Y_pred[0] == 0:
        cp = 'b'
    elif Y_pred[0] == 1:
        cp = 'r'
    else:
        cp = 'g'

    if plt:
        plt.clf() # clears the figure when browser back arrow used to enter new data

    plt.scatter(X_0[:, 0], X_0[:, 1], c='b', edgecolors='k', label = 'class 0')
    plt.scatter(X_1[:, 0], X_1[:, 1], c='r', edgecolors='k', label = 'class 1')
    plt.scatter(X_2[:, 0], X_2[:, 1], c='g', edgecolors='k', label = 'class 2')
    plt.scatter(X_n[:, 0], X_n[:, 1], c=cp, edgecolors='k', marker = 'd', \
        s=100, label = 'prediction')
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')
    plt.title('Prediction plotted with training data')
    plt.legend()
        
    image = BytesIO()
    plt.savefig(image)
    out = image.getvalue(), 200, {'Content-Type': 'image/png'}
    '''
    
    out = str(Y_pred)
    N = str(Neighborhood)
    
    return '${}'.format(out, N)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
