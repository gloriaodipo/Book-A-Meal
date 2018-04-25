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

    
       

from .models import User, Meal, Menu, Order, Meal_Schema

app = Flask(__name__)
api = Api(app)

users = [User(1, "gloria", "odipo", "gloriaodipo", "godipo@gmail.com", "bubble")]
meals = [Meal(2, "beef with rice", 500.00, "main dish")]
orders = []

class User_signup_API(Resource):
    def post(self):
        user = json.loads(request.data)
        u = User(user_id=user.get('user_id'), first_name=user.get('first_name'), last_name=user.get('last_name'),
        username=user.get('username'), email=user.get('email'), password=user.get('password'))

        users.append(u)

        result=jsonify ({"message": "successfully registered"})
        result.status_code = 201
        return result

class User_login_API(Resource):
    def post(self, user_id):
        access = json.loads(request.data)
        username = access.get('username')
        password= access.get('password')
        for user in users:
            if user_id == user.user_id:
                if username == user.username and password == user.password:

                    result=jsonify ({"message": "welcome!"})
                    result.status_code = 200
                    return result
            
            result=jsonify ({"message": "user unavailable"})
            result.status_code = 404
            return result
                        
        
class Meals_API(Resource):
    def post(self):
        meal = json.loads(request.data)
        m = Meal(meal_id=meal.get('meal_id'), meal_name=meal.get('meal_name'), price=meal.get('price'),
        category=meal.get('category'))

        meals.append(m)

        result = jsonify({"message": "meal added"})
        result.status_code = 201
        return result

    def get(self):
        meal = Meal_Schema(many = True)
        meal_items = meal.dump(meals)

        result = jsonify(meal_items.data)
        result.status_code = 200
        return result


class Single_meal_API(Resource):
    def get(self, meal_id):
        meal = Meal_Schema(many = True)
        meal_items = meal.dump(meals)
        for meal in meals:
            if meal_id == meal.meal_id:
                result = jsonify(meal_items.data)
                result.status_code = 200
                return result
            else:
                result = jsonify({"message": "meal not found"})
                result.status_code = 404
                return result   

    def put(self, meal_id):
        for meal in meals:
            if meal_id == meal.meal_id:
                meals.remove(meal) 
                meal = json.loads(request.data)
                m = Meal(meal_id, meal_name=meal.get('meal_name'), price=meal.get('price'),
                category=meal.get('category'))

                result = jsonify({"message": "meal has been modified"})
                result.status_code = 200
                return result
        
    def delete(self, meal_id):
        meal = Meal_Schema(many = True)
        meal_items = meal.dump(meals)
        for meal in meals:
            if meal_id == meal.meal_id:

                meals.remove(meal)

                result = jsonify({"message": "meal has been deleted"})
                result.status_code = 200
                return result 
            else:
                result = jsonify({"message": "invalid selection"})
                result.status_code = 404
                return result 

    
        
api.add_resource(User_signup_API, '/user/api/v1/signup')

api.add_resource(User_login_API, '/user/api/v1/login/<int:user_id>')

api.add_resource(Meals_API, '/api/v1/meals')

api.add_resource(Single_meal_API, '/api/v1/meals/<int:meal_id>')



if __name__ == '__main__':

    app.run(debug=True)
