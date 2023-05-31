from flask import request, jsonify, Blueprint
from PIL import Image
import tensorflow as tf
import numpy as np

fileCounter = 0
# filePath = "../../IncomingImg/5_30/img"
filePath = "../../0_IncomingImg/5_31/img"


bp = Blueprint('predict', __name__)

# route for Compressed prediction
@bp.route('/predict/Compressed', methods=['POST'])
def get_Compressed_prediction():
    try:
        print(type(request))
        json_payload = request.get_json()

        # unpack the request
        inputMatrix = json_payload["inputMatrix"]
        inputData = np.array(inputMatrix)

        model = tf.keras.models.load_model('../CNN_ver0_compressedImg.h5')
        print(inputData.shape)

        inputData_float32 = inputData.astype(np.float32)
        img_compressed = []
        for i in range(20):
            row_compressed = []
            for j in range(20):
                sum = 0
                for r in range(5):
                    for c in range(5):
                        sum += inputData_float32[5 * i + r][5 *j + c]
                row_compressed += [sum/25]
                
            img_compressed += [row_compressed]

        wraped_input = np.array([img_compressed])
        predictions = model.predict(wraped_input)

        
        # Get the indices of the largest 4 numbers
        prediction_1st = np.argsort(predictions[0])[-1]
        prediction_2nd = np.argsort(predictions[0])[-2]
        prediction_3rd = np.argsort(predictions[0])[-3]
        prediction_4th = np.argsort(predictions[0])[-4]

        class_names = ['0' '1' '2' '3' '4' '5' '6' '7' '8' '9' 'A' 'B' 'C' 'D' 'E' 'F' 'G' 'H'
         'I' 'J' 'K' 'L' 'M' 'N' 'O' 'P' 'Q' 'R' 'S' 'T' 'U' 'V' 'W' 'X' 'Y' 'Z'
         'a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j' 'k' 'l' 'm' 'n' 'o' 'p' 'q' 'r'
         's' 't' 'u' 'v' 'w' 'x' 'y' 'z']
        result = []
        resultProb = []
        
        result += [class_names[0][prediction_1st]]
        result += [class_names[0][prediction_2nd]]
        result += [class_names[0][prediction_3rd]]
        result += [class_names[0][prediction_4th]]

        resultProb += [round(predictions[0][prediction_1st] * 100, 1)]
        resultProb += [round(predictions[0][prediction_2nd] * 100, 1)]
        resultProb += [round(predictions[0][prediction_3rd] * 100, 1)]
        resultProb += [round(predictions[0][prediction_4th] * 100, 1)]
        resultProb = np.array(resultProb).tolist()

        saveImage(inputData, resultProb[0])

        print(result)
        print(resultProb)
        # Format the return data
        response_data = {"Result": result, "ResultProb": resultProb}
        return jsonify(response_data)
    # exception
    except KeyError as e:
        # Handle missing field error
        return f'Missing field error: {e}', 400
    except Exception as e:
        # Handle other exceptions
        return f'Internal server error: {e}', 500

# route for Basic prediction
@bp.route('/predict/Basic', methods=['POST'])
def get_Basic_prediction():
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

        class_names = ['0' '1' '2' '3' '4' '5' '6' '7' '8' '9' 'A' 'B' 'C' 'D' 'E' 'F' 'G' 'H'
         'I' 'J' 'K' 'L' 'M' 'N' 'O' 'P' 'Q' 'R' 'S' 'T' 'U' 'V' 'W' 'X' 'Y' 'Z'
         'a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j' 'k' 'l' 'm' 'n' 'o' 'p' 'q' 'r'
         's' 't' 'u' 'v' 'w' 'x' 'y' 'z']
        result = []
        resultProb = []
        
        result += [class_names[0][prediction_1st]]
        result += [class_names[0][prediction_2nd]]
        result += [class_names[0][prediction_3rd]]
        result += [class_names[0][prediction_4th]]

        resultProb += [round(predictions[0][prediction_1st] * 100, 1)]
        resultProb += [round(predictions[0][prediction_2nd] * 100, 1)]
        resultProb += [round(predictions[0][prediction_3rd] * 100, 1)]
        resultProb += [round(predictions[0][prediction_4th] * 100, 1)]
        resultProb = np.array(resultProb).tolist()
        
        saveImage(inputData, resultProb[0])

        print(result)
        print(resultProb)
        # Format the return data
        response_data = {"Result": result, "ResultProb": resultProb}
        return jsonify(response_data)
    # exception
    except KeyError as e:
        # Handle missing field error
        return f'Missing field error: {e}', 400
    except Exception as e:
        # Handle other exceptions
        return f'Internal server error: {e}', 500

# route for Centered prediction
@bp.route('/predict/Centered', methods=['POST'])
def get_Centered_prediction():
    try:
        print(type(request))
        json_payload = request.get_json()

        # unpack the request
        inputMatrix = json_payload["inputMatrix"]
        inputData = np.array(inputMatrix)

        model = tf.keras.models.load_model('../CNN_ver2_centeredImg.h5')
        print(inputData.shape)

        inputData_float32 = inputData.astype(np.float32)
        input_np = centerChar(inputData_float32)
        wraped_input = np.array([input_np])
        predictions = model.predict(wraped_input)

        # Get the indices of the largest 4 numbers
        prediction_1st = np.argsort(predictions[0])[-1]
        prediction_2nd = np.argsort(predictions[0])[-2]
        prediction_3rd = np.argsort(predictions[0])[-3]
        prediction_4th = np.argsort(predictions[0])[-4]

        class_names = ['0' '1' '2' '3' '4' '5' '6' '7' '8' '9' 'A' 'B' 'C' 'D' 'E' 'F' 'G' 'H'
         'I' 'J' 'K' 'L' 'M' 'N' 'O' 'P' 'Q' 'R' 'S' 'T' 'U' 'V' 'W' 'X' 'Y' 'Z'
         'a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j' 'k' 'l' 'm' 'n' 'o' 'p' 'q' 'r'
         's' 't' 'u' 'v' 'w' 'x' 'y' 'z']
        result = []
        resultProb = []
        
        result += [class_names[0][prediction_1st]]
        result += [class_names[0][prediction_2nd]]
        result += [class_names[0][prediction_3rd]]
        result += [class_names[0][prediction_4th]]

        resultProb += [round(predictions[0][prediction_1st] * 100, 1)]
        resultProb += [round(predictions[0][prediction_2nd] * 100, 1)]
        resultProb += [round(predictions[0][prediction_3rd] * 100, 1)]
        resultProb += [round(predictions[0][prediction_4th] * 100, 1)]
        resultProb = np.array(resultProb).tolist()
        
        saveImage(inputData, resultProb[0])

        print(result)
        print(resultProb)
        # Format the return data
        response_data = {"Result": result, "ResultProb": resultProb}
        return jsonify(response_data)
    # exception
    except KeyError as e:
        # Handle missing field error
        return f'Missing field error: {e}', 400
    except Exception as e:
        # Handle other exceptions
        return f'Internal server error: {e}', 500

# route for Centered-test prediction
@bp.route('/predict/Centered-2', methods=['POST'])
def get_Centered2_prediction():
    try:
        print(type(request))
        json_payload = request.get_json()

        # unpack the request
        inputMatrix = json_payload["inputMatrix"]
        inputData = np.array(inputMatrix)

        model = tf.keras.models.load_model('../CNN_ver3_center_new_struct.h5')
        print(inputData.shape)

        inputData_float32 = inputData.astype(np.float32)
        input_np = centerChar(inputData_float32)
        wraped_input = np.array([input_np])
        predictions = model.predict(wraped_input)

        # Get the indices of the largest 4 numbers
        prediction_1st = np.argsort(predictions[0])[-1]
        prediction_2nd = np.argsort(predictions[0])[-2]
        prediction_3rd = np.argsort(predictions[0])[-3]
        prediction_4th = np.argsort(predictions[0])[-4]

        class_names = ['0' '1' '2' '3' '4' '5' '6' '7' '8' '9' 'A' 'B' 'C' 'D' 'E' 'F' 'G' 'H'
         'I' 'J' 'K' 'L' 'M' 'N' 'O' 'P' 'Q' 'R' 'S' 'T' 'U' 'V' 'W' 'X' 'Y' 'Z'
         'a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j' 'k' 'l' 'm' 'n' 'o' 'p' 'q' 'r'
         's' 't' 'u' 'v' 'w' 'x' 'y' 'z']
        result = []
        resultProb = []
        
        result += [class_names[0][prediction_1st]]
        result += [class_names[0][prediction_2nd]]
        result += [class_names[0][prediction_3rd]]
        result += [class_names[0][prediction_4th]]

        resultProb += [round(predictions[0][prediction_1st] * 100, 1)]
        resultProb += [round(predictions[0][prediction_2nd] * 100, 1)]
        resultProb += [round(predictions[0][prediction_3rd] * 100, 1)]
        resultProb += [round(predictions[0][prediction_4th] * 100, 1)]
        resultProb = np.array(resultProb).tolist()
        
        saveImage(inputData, resultProb[0])

        print(result)
        print(resultProb)
        # Format the return data
        response_data = {"Result": result, "ResultProb": resultProb}
        return jsonify(response_data)
    # exception
    except KeyError as e:
        # Handle missing field error
        return f'Missing field error: {e}', 400
    except Exception as e:
        # Handle other exceptions
        return f'Internal server error: {e}', 500

# route for Onehot-Encoded prediction
@bp.route('/predict/Onehot', methods=['POST'])
def get_Onehot_prediction():
    try:
        print(type(request))
        json_payload = request.get_json()

        # unpack the request
        inputMatrix = json_payload["inputMatrix"]
        inputData = np.array(inputMatrix)

        model = tf.keras.models.load_model('../CNN_ver4_85-80.h5')
        print(inputData.shape)

        inputData_float32 = inputData.astype(np.float32)
        input_np = centerChar(inputData_float32)
        wraped_input = np.array([input_np])
        predictions = model.predict(wraped_input)

        # Get the indices of the largest 4 numbers
        prediction_1st = np.argsort(predictions[0])[-1]
        prediction_2nd = np.argsort(predictions[0])[-2]
        prediction_3rd = np.argsort(predictions[0])[-3]
        prediction_4th = np.argsort(predictions[0])[-4]

        class_names = ['0' '1' '2' '3' '4' '5' '6' '7' '8' '9' 'A' 'B' 'C' 'D' 'E' 'F' 'G' 'H'
         'I' 'J' 'K' 'L' 'M' 'N' 'O' 'P' 'Q' 'R' 'S' 'T' 'U' 'V' 'W' 'X' 'Y' 'Z'
         'a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j' 'k' 'l' 'm' 'n' 'o' 'p' 'q' 'r'
         's' 't' 'u' 'v' 'w' 'x' 'y' 'z']
        result = []
        resultProb = []
        
        result += [class_names[0][prediction_1st]]
        result += [class_names[0][prediction_2nd]]
        result += [class_names[0][prediction_3rd]]
        result += [class_names[0][prediction_4th]]

        resultProb += [round(predictions[0][prediction_1st] * 100, 1)]
        resultProb += [round(predictions[0][prediction_2nd] * 100, 1)]
        resultProb += [round(predictions[0][prediction_3rd] * 100, 1)]
        resultProb += [round(predictions[0][prediction_4th] * 100, 1)]
        resultProb = np.array(resultProb).tolist()

        saveImage(inputData, resultProb[0])

        print(result)
        print(resultProb)
        # Format the return data
        response_data = {"Result": result, "ResultProb": resultProb}
        return jsonify(response_data)
    # exception
    except KeyError as e:
        # Handle missing field error
        return f'Missing field error: {e}', 400
    except Exception as e:
        # Handle other exceptions
        return f'Internal server error: {e}', 500



# helper functions =================================================================================
def centerChar(Img):
    dimension = len(Img)
    location = locatChar(Img)
    
    resultImg = []
    for i in range(dimension):
        row = []
        for j in range(dimension):
            row += [[np.float32(1.0)]]
            
        resultImg += [row]
    
    offset_row = int((dimension-(location[1] + 1 -location[0]))/2)    
    offset_col = int((dimension-(location[3] + 1 -location[2]))/2)
    
    for i in range(0, location[1] + 1 - location[0]):
        for j in range(0, location[3] + 1 - location[2]):
            resultImg[i + offset_row][j + offset_col][0] = Img[i + location[0]][j + location[2]][0]
    
    
    resultImg = np.array(resultImg)
    return resultImg
    
def locatChar(Img):
    dimension = len(Img)
    top = dimension
    bottom = 0
    left = dimension
    right = 0
    
    for i in range(dimension):
        for j in range(dimension):
            if Img[i][j][0] < 0.2:
                if top > i:
                    top = i
                if bottom < i:
                    bottom = i
                if left > j:
                    left = j
                if right < j:
                    right = j
    return [top, bottom, left, right]

def saveImage(Img, prob):
    global fileCounter
    global filePath

    
    if prob > 0.2:
        # revert normaliztion
        Img_scaled = np.uint8(Img * 255)

        image = Image.fromarray(Img_scaled.squeeze(), mode='L')

        file_path = f"{filePath}_{fileCounter}.png"
        image.save(file_path)
        fileCounter += 1
        print("Input saved")