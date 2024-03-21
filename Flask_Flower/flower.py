# flower.py
from flask import Flask, request, render_template
import pickle

V1 = open(r'C:\Users\hisha\Desktop\Python\Flower SVM\Flower_SVM.pkl', 'rb')
V = pickle.load(V1)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        SEL = float(request.form['Sepal_length'])
        SW = float(request.form['Sepal_width'])
        PEL = float(request.form['Petal_length'])
        PW = float(request.form['Petal_width'])

        prediction = V.predict([[SEL, SW, PEL, PW]])
        # prediction = prediction[0]
        print('prediction=', prediction)
        return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
