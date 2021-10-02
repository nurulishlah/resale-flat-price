from flask import Flask, request, render_template
from xgboost import XGBRegressor
import numpy as np

app = Flask(__name__)

model = XGBRegressor()
model.load_model('model.json')

flat_type = {
    1: "4 ROOM",
    2: "5 ROOM",
    3: "3 ROOM",
    4: "EXECUTIVE",
    5: "2 ROOM",
    6: "MULTI-GENERATION",
    7: "1 ROOM",
}

@app.route('/')
def index():
    return render_template('index.html', insurance_cost=0)

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    tipe, ukuran, tahun = [x for x in request.form.values()]

    data = []

    data.append(int(tipe))
    data.append(float(ukuran))
    data.append(int(tahun))

    print(data)

    prediction = model.predict(np.array(data))
    output = round(prediction[0], 2)

    return render_template('index.html', resale_price=output, flat_type=flat_type[tipe], size=ukuran)


if __name__ == '__main__':
    app.run(debug=True)