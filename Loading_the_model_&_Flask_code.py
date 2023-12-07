# Create a Flask server
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load your machine learning model
model = joblib.load('new_model.joblib')  

# Mapping for reverse class lookup
reverse_class_mapping = {0: "Iris-setosa", 1: "Iris-versicolor", 2: "Iris-virginica"}

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the request
        data = request.get_json()
        input_data = np.array(data['features']).reshape(1, -1)

        # Make prediction using the loaded model
        prediction = model.predict(input_data)

        # Get the actual class name based on the numerical prediction
        actual_class_name = reverse_class_mapping[prediction[0]]

        return jsonify({'prediction': actual_class_name})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000, threaded=True)
