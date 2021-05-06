
from flask import Flask, request
import pickle
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from datetime import date

# Initialize app
app = Flask(__name__)

# load the pickled model
with open('data/model_rfr_full.pkl', 'rb') as f:
    model = pickle.load(f)

# # load the pickled training data to display with prediction
# with open('data/trainXY.pkl', 'rb') as f:
#     trainXY = pickle.load(f)

# trainX = trainXY[:,:2]
# trainY = trainXY[:,2]

# Home page with form on it to submit new data
@app.route('/')
def get_new_data():
    return '''
        <form action="/predict" method='POST'>
          House Address:
          <br>
          <input type="str" name="Address"> 
          <br>
          Bedrooms:
          <br>
          <input type="int" name="Bedrooms"> 
          <br>
          Bathrooms:
          <br>
          <input type="text" name="Bathrooms"> 
          <br>
          Neighborhood:
          <br>
          <input type="text" name="Neighborhood"> 
          <br>
          Zip Code:
          <br>
          <input type="text" name="Zip Code"> 
          <br>
          Square Feet:
          <br>
          <input type="text" name="Square Feet"> 
          <br>
          Year Built:
          <br>
          <input type="text" name="Year"> 
          <br>
          Lot Size:
          <br>
          <input type="text" name="Lot Size"> 
          <br>
          <br>
          <input type="submit" value="Submit for house price estimation">
        </form>
        '''

@app.route('/predict', methods = ["GET", "POST"])
def predict():
    # request the text from the form 
    Address = str(request.form['Address'])
    Bedrooms = float(request.form['Bedrooms'])
    Bathrooms = float(request.form['Bathrooms'])
    # Neighborhood = float(request.form['Neighborhood'])
    Zip = float(request.form['Zip Code'])
    SqFt = float(request.form['Square Feet'])
    Year = float(request.form['Year'])
    Lot = float(request.form['Lot Size'])
    Month = date.today().month
    Yeartoday = date.today().year
    #Placeholders for latitude and longitude and HOA
    Lat = 29.483
    Long = -98.51
    HOA = 0 
    X_n = np.array([[Zip, SqFt, Lot, Year, HOA, Lat, Long, (Bedrooms+Bathrooms), Month,Yeartoday]])
    
    # predict on the new data
    Y_pred = model.predict(X_n)

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
    
    return '${}'.format(out[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
