# doing necessary imports

from flask import Flask, render_template, request, jsonify
import joblib
from sklearn.linear_model import LinearRegression
import requests
import numpy as np

app = Flask(__name__)  # initialising the flask app with the name 'app'


@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')


# base url + /
# http://localhost:8000 + /
@app.route('/predict', methods=['POST'])  # route with allowed methods as POST and GET
def index():
    if request.method == 'POST':
        try:
            GRE_Score = request.form['GRE Score']
            print('GRE_Score:', GRE_Score)
            University_Rating = request.form['University Rating']
            print('University_Rating:', University_Rating)
            SOP = request.form['SOP']
            print('SOP:', SOP)
            LOR = request.form['LOR']
            print('LOR:', LOR)
            CGPA = request.form['CGPA']
            print('CGPA:', CGPA)
            Research = request.form['Research']
            print('Research:', Research)

            chk = [GRE_Score, University_Rating, SOP, LOR, CGPA, Research]
            chk = np.array(chk)
            chk = chk.reshape(1, -1)
            scaler=joblib.load('SimpleLinearRegression_Scaler.pkl')
            scaled_data=scaler.transform(chk)

            LinReg=joblib.load('SimpleLinearRegression.pkl')
            y_pred=LinReg.predict(scaled_data)

            return render_template('results.html', y_pred=y_pred)  # showing the review to the user
        except:
            return 'something is wrong'


if __name__ == "__main__":
    app.run(port=8000, debug=True)  # running the app on the local machine on port 8000
