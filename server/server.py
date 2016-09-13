from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
import mysql.connector

app = Flask(__name__)
cors = CORS(app)



@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'

@app.route('/craig')
@cross_origin(supports_credentials=True)
def test():
     cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1', database='test')
     cursor = cnx.cursor(dictionary=True);
     query = ("SELECT * FROM test.post")
     cursor.execute(query)
     res = []
     for x in cursor :
          res.append(x)
          print "Here"
     #return jsonify(dict(res)), 200
     print "This : " + str(res)
     return jsonify({"name" : "Craig", "profession" : "Software Engineer"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
