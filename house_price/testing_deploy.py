from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

# Mengambil lokasi folder file Python
folder = os.path.dirname(os.path.abspath(__file__))

# Memuat model dari folder yang sama
lokasi_model = os.path.join(folder, 'gbr_model.joblib')
joblib_model = joblib.load(lokasi_model)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['data']
    prediction = joblib_model.predict(data)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)