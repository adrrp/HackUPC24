from flask import Flask, request, jsonify
from gestor import Gestor
import json

app = Flask(__name__)


"""
get-standard data

Input json (nombre)
-time
-timeError
-svid
-constellationType
-cn0DbHz
-agcDb
-deviceLongitude
-deviceLatitude
-azimuthDegrees
-elevationDegrees

"""



@app.route('/set-standard-data', methods=['POST'])
def get_standard_data():
    data = request.get_json()
    gestor.actualizar(json.loads(data)) # tiene que ser el creado en el main
    return jsonify({"result": "okay"})

@app.route('/api', methods=['POST'])
def deleteOldSatellites():
    data = request.get_json()
    timeMargin = data.get('timeMargin', 0)
    gestor.deleteOldSats(timeMargin)
    return jsonify({"result": "okay"})

@app.route('/getCurrentSats', methods=['GET'])
def getCurrentSats():
    jsondata = gestor.getSats()
    return jsondata



if __name__ == '__main__':
    Gestor gestor = #crear un nuevo gestor
    app.run(debug=True)