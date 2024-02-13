# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run(debug=True)

#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