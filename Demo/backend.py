from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



# route for store inventory managment
@app.route('/predict', methods=['POST'])
def get_prediction():
    try:
        print(type(request))
        json_payload = request.get_json()

        # unpack the request
        inputMatrix = json_payload["inputMatrix"]
        inputData = np.array(inputMatrix)

        model = tf.keras.models.load_model('../CNN_ver1.h5')
        print(inputData.shape)
        print(type(inputData[0][0][0]))

        inputData_float32 = inputData.astype(np.float32)
        print(type(inputData_float32[0][0][0]))

        wraped_input = np.array([inputData_float32])

        predictions = model.predict(wraped_input)

        # Get the indices of the largest 4 numbers
        prediction_1st = np.argsort(predictions[0])[-1]
        prediction_2nd = np.argsort(predictions[0])[-2]
        prediction_3rd = np.argsort(predictions[0])[-3]
        prediction_4th = np.argsort(predictions[0])[-4]

        
        print("????")
        class_names = ['0' '1' '2' '3' '4' '5' '6' '7' '8' '9' 'A' 'B' 'C' 'D' 'E' 'F' 'G' 'H'
         'I' 'J' 'K' 'L' 'M' 'N' 'O' 'P' 'Q' 'R' 'S' 'T' 'U' 'V' 'W' 'X' 'Y' 'Z'
         'a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j' 'k' 'l' 'm' 'n' 'o' 'p' 'q' 'r'
         's' 't' 'u' 'v' 'w' 'x' 'y' 'z']
        result = []
        resultIndex = []
        
        result += [class_names[0][prediction_1st]]
        result += [class_names[0][prediction_2nd]]
        result += [class_names[0][prediction_3rd]]
        result += [class_names[0][prediction_4th]]

        
        resultIndex += [prediction_1st]
        resultIndex += [prediction_2nd]
        resultIndex += [prediction_3rd]
        resultIndex += [prediction_4th]

        print(result)
        # Format the return data
        response_data = {"Result": result}
        print("????")
        return jsonify(response_data)
    # exception
    except KeyError as e:
        # Handle missing field error
        return f'Missing field error: {e}', 400
    except Exception as e:
        # Handle other exceptions
        return f'Internal server error: {e}', 500


# Run the application
if __name__ == '__main__':
    # change host to local IP address for hardware public request
    # app.run(host="172.20.10.3")
    app.run()