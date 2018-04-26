from marshmallow import Schema, fields
import random

class User():

    def __init__(self,first_name, last_name, username, email, password):
        self.user_id = random.randint(1,100)
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password 

class User_Schema(Schema):
    user_id = fields.Int()
    first_name = fields.Str()
    last_name = fields.Str()
    username = fields.Str()
    email = fields.Str()
    password = fields.Str()
    caterer = fields.Boolean()

  
class Meal():
    def __init__(self, meal_name, price, category):
        self.meal_id = random.randint(1,100)
        self.meal_name = meal_name
        self.price = price
        self.category = category

class Meal_Schema(Schema):
    meal_id = fields.Int()
    meal_name = fields.Str()
    price = fields.Float()
    category = fields.Str() 
        
class Menu():
    meals = []
    def __init__(self):
         meals = []
    def add(self, meal):
        meals.append(meal)
    def remove(self, meal_id):
        for meal in meals:
            if meal_id == meal.meal_id:
                del(meals[meal])
#returns a list of all meals 
    def get(self):
        return self.meals

    def edit(self,meal_id, meal_name, price, category):
        for meal in meals:
            if meal_id == meal.meal_id:
                meal.meal_name = meal_name
                meal.price = price
                meal.category = category
    
                
class Order():
    def __init__(self, customer,order_items):
        self.order_id = random.randint(1,100)
        self.customer = customer
        self.order_items = order_items

class Order_Schema(Schema):
    order_id = fields.Int()
    customer = fields.Str()
    order_items = fields.Str()


