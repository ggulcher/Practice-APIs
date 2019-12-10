# Flask REST API without Flask RESTful
from Flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'you sent': some_json}), 281
    else:
        return jsonify({"about": "Hello World!"})

@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
    return jsonify({'result': num*10})

if __name__ == '__main__':
    app.run(debug=True)

# Flask REST API with Flask RESTful
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'about':'Hello World!'}
    
    def post(self):
        some_json = request.get_json()
        return {'you sent': some_json}, 281

class Multi(Resource):
    def get(self, num):
        return {'result': num*10}

api.add_resource(HelloWorld, '/')
api.add_resource(Multi, '/multi/<int:num>')

if __name__ == '__main__':
    app.run(debug=True)
