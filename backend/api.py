from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def sum_two_numbers():
    # Obtenemos los datos del cuerpo de la solicitud en formato JSON
    data = request.get_json()
    
    # Extraemos los números a sumar
    num1 = data['number1']
    num2 = data['number2']
    
    # Calculamos la suma
    result = num1 + num2
    
    # Devolvemos la suma como un JSON
    return jsonify({'result': result})

@app.route('get-standard-data', methods=['POST'])
def get_standard_data():
    data = request.get_json()

    



if __name__ == '__main__':
    app.run(debug=True)