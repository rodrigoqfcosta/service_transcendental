from flask import Flask, request
from flask import jsonify
from flask_cors import CORS

import math

app = Flask(__name__)
CORS(app)

@app.route('/fatorial')
def fatorial():
    arg1 = request.args.get('arg1', type=int)
    int_output = {'result': (math.factorial(arg1))}
    return jsonify(int_output)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
