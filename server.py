from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    numbers = request.json
    return jsonify(int(numbers['first'] + numbers['second']))

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    numbers = request.json
    return jsonify(int(numbers['first'] - numbers['second']))

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
