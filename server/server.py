from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)



@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'

@app.route('/craig')
@cross_origin(supports_credentials=True)
def test():
    return jsonify({"name" : "Craig", "profession" : "Software Engineer"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
