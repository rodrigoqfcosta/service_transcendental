from flask import Flask, request
from flask import jsonify
from flask_cors import CORS

import math

app = Flask(__name__)
CORS(app)

@app.route('/fatorial')
def soma():
    int_input = request.args.get('int_input', type=int)
    int_output = {'fatorial': (math.factorial(int_input))}
    return jsonify(int_output)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
