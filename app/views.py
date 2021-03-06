from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import json
import random

from app.models import User, Meal, Menu, Order, Meal_Schema, Order_Schema, Menu_Schema

app = Flask(__name__)
api = Api(app)

users = [User(first_name="gloria", last_name="odipo", username="gloriaodipo", email="godipo@gmail.com", password="bubble")]
meals = [Meal(meal_id = 2, meal_name = "beef with rice", price = 500.00, category ="main dish")]
orders = [Order( order_id = 1, customer="caren", order_items="beef with rice, juice")]
menus = [Menu(meal_id = 2, meal_name = "beef with rice", price = 500.00, category ="main dish")]

class UserSignupAPI(Resource):
    def post(self):
        user = request.get_json()
        if user.get('first_name') is None or user.get('last_name') is None or user.get('username') is None\
                 or user.get('email') is None or user.get('password') is None:
            result = jsonify({'message': 'All fields required'}) 
            result.status_code = 400
            return result

        u = User(first_name=user.get('first_name'), last_name=user.get('last_name'),
        username=user.get('username'), email=user.get('email'), password=user.get('password'))

        users.append(u)

        result = jsonify({'message': 'Successfully registered'})
        result.status_code = 201
        return result

class UserLoginAPI(Resource):

    def post(self):
        access = request.get_json()
        username = access.get('username')
        password = access.get('password')
        for user in users:
            if username == user.username:
                if password == user.password:
                    result = jsonify({"message": "You are successfully logged in"})
                    result.status_code = 200
                    return result
                else:
                    result =jsonify({'message': 'Wrong password.'})
                    result.status_code = 401
                    return result

            result = jsonify({"message": "User unavailable"})
            result.status_code = 404
            return result
                       
class MealsAPI(Resource):
    def post(self):
        meal = request.get_json()
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

class SingleMealAPI(Resource):  

    def put(self, meal_id):
        for meal in meals:
            if meal_id == meal.meal_id: 
                meal = json.loads(request.data)
                m = Meal(meal_id = meal.get('meal_id'), meal_name=meal.get('meal_name'), price=meal.get('price'),
                category=meal.get('category'))
                result = jsonify({"message": "meal has been modified"})
                result.status_code = 200
                return result
        
    def delete(self, meal_id):
        for meal in meals:
            if meal_id == meal.meal_id:

                meals.remove(meal)

                result = jsonify({"message": "meal deleted"})
                result.status_code = 200
                return result  

class OrdersAPI(Resource):
    def post(self):
        order = request.get_json()
        o =  Order( order_id = order.get('oredr_id'), customer=order.get('customer'), order_items=order.get('order_items'))

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

class SingleOrderAPI(Resource):
    def put(self, order_id): 
            for order in orders:
                if order_id == order.order_id:
                    od = json.loads(request.data)
                    o =  Order(order_id=od.get('order_id'), customer=od.get('customer'), order_items=od.get('order_items'))

                    result = jsonify({"message": "order has been modified"})
                    result.status_code = 200
                    return result 

class MenuAPI(Resource):

    def post(self):
        menu = request.get_json()
        m = Menu(meal_id=menu.get('meal_id'), meal_name=menu.get('meal_name'), price=menu.get('price'),
        category=menu.get('category'))

        menus.append(m)

        result = jsonify({"message": "meal added to menu"})
        result.status_code = 201
        return result
    
    def get(self):
        menu = Menu_Schema(many = True)
        menu_items = menu.dump(menus)

        result = jsonify(menu_items.data)
        result.status_code = 200
        return result

api.add_resource(UserSignupAPI, '/api/v1/user/signup')
api.add_resource(UserLoginAPI, '/api/v1/user/login')
api.add_resource(MealsAPI, '/api/v1/meals')
api.add_resource(SingleMealAPI, '/api/v1/meals/<int:meal_id>')
api.add_resource(OrdersAPI, '/api/v1/orders')
api.add_resource(SingleOrderAPI, '/api/v1/orders/<int:order_id>')
api.add_resource(MenuAPI, '/api/v1/menu')



if __name__ == '__main__':

    app.run(debug=True)
