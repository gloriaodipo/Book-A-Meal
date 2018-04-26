from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import json

app = Flask(__name__)
api = Api(app)

class UserAPI(Resource):
    def post(self):
        pass
   
class MealsAPI(Resource):
    def post(self):
        pass

    def get(self):
        pass

    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass

class OrdersAPI(Resource):
    def post(self):
        pass

    def get(self):
        pass
        
    def get(self, id):
        pass

    def put(self, id):
        pass

    
        






if __name__ == '__main__':

    app.run(debug=True)
