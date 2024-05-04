from flask import Flask, request, jsonify

app = Flask(__name__)


"""
get-standard data

Input json:


Output json:
-Sat array:
    -ID
    -Constellation Type
    -Quality
    -Fix
    -Azi
    -Ele



"""


@app.route('get-standard-data', methods=['POST'])
def get_standard_data():
    data = request.get_json()






if __name__ == '__main__':
    
    app.run(debug=True)