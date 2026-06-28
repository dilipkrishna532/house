from flask import Flask, render_template, request, jsonify
from model import predict_price, get_line_data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    size = float(request.form['size'])
    price = predict_price(size)
    return jsonify({'price': price})

@app.route('/data')
def data():
    X, y, y_pred = get_line_data()
    return jsonify({
        'x': X,
        'y': y,
        'y_pred': y_pred
    })

if __name__ == '__main__':
    app.run(debug=True)