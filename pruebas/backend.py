from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/random-number', methods=['GET'])
def random_number():
    number = random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100
    return jsonify({"number": number})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Acepta conexiones en todas las interfaces


