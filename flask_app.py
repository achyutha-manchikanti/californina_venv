from flask import Flask, request, render_template
import sklearn
import numpy as np
import joblib

# Load model
obj = joblib.load('california.joblib')

model = obj['Model']
columns = obj['Columns']

app = Flask(__name__)


@app.route('/')
def Main():
    return render_template('index.html', columns=columns)


@app.route('/predict', methods=['POST'])
def predict():

    Input = []

    for i in columns:
        val = float(request.form[i])
        Input.append(val)

    # Prediction
    out = model.predict([Input])

    prediction = out[0]

    return render_template(
        'index.html',
        columns=columns,
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)