from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import json
import random


from .models import User, Meal, Menu, Order, Meal_Schema, Order_Schema

app = Flask(__name__)
api = Api(app)

users = [User( "gloria", "odipo", "gloriaodipo", "godipo@gmail.com", "bubble")]
meals = [Meal( "beef with rice", 500.00, "main dish")]
orders = [Order( "caren", "beef with rice, juice")]


class UserSignupAPI(Resource):
    def post(self):
        user = request.get_json()
        u = User(first_name=user.get('first_name'), last_name=user.get('last_name'),
        username=user.get('username'), email=user.get('email'), password=user.get('password'))

        users.append(u)

        result=jsonify ({"message": "successfully registered"})
        result.status_code = 201
        return result

class UserLoginAPI(Resource):
    def post(self, user_id):
        access = request.get_json()
        username = access.get('username')
        password= access.get('password')
        for user in users:
            if user_id == user.user_id:
                if username == user.username and password == user.password:

                    result=jsonify ({"message": "You are successfully logged in"})
                    result.status_code = 200
                    return result
            
            result=jsonify ({"message": "user unavailable"})
            result.status_code = 401
            return result
                        
        
class MealsAPI(Resource):
    def post(self):
        meal = request.get_json()
        m = Meal(meal_name=meal.get('meal_name'), price=meal.get('price'),
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


class SingleMealAPI(Resource):
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


class OrdersAPI(Resource):
    def post(self):
        order = request.get_json()
        o =  Order( customer=order.get('customer'), order_items=order.get('order_items'))

        orders.append(o)

        result = jsonify({"message": "order added"})
        result.status_code = 201
        return result

    def get(self):
        order = Order_Schema(many = True)
        order_items = order.dump(orders)

        result = jsonify(order_items.data)
        result.status_code = 200
        return result

    
class UpdateOrderAPI(Resource):
    def put(self, order_id): 
            for order in orders:
                if order_id == order.order_id:
                    orders.remove(order) 
                    order = json.loads(request.data)
                    o =  Order(order_id=order.get('order_id'), customer=order.get('customer'), order_items=order.get('order_items'))

                    result = jsonify({"message": "order has been modified"})
                    result.status_code = 200
                    return result 





api.add_resource(UserSignupAPI, '/api/v1/user/signup')

api.add_resource(UserLoginAPI, '/api/v1/user/login')

api.add_resource(MealsAPI, '/api/v1/meals')

api.add_resource(SingleMealAPI, '/api/v1/meals/<int:meal_id>')

api.add_resource(OrdersAPI, '/api/v1/orders')

api.add_resource(UpdateOrderAPI, '/api/v1/orders/<int:order_id>')



if __name__ == '__main__':

    app.run(debug=True)
