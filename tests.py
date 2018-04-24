from app.views import app
import unittest
import json

class UserTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.data = {
                    "first_name": "gloria",
                    "last_name": "odipo",
                    "username":"gloriaodipo", 
                    "email":"godipo@gmail.com",
                    "password":"bubble"
                    }
    
    def test_login(self):
        response = self.app.get('/api/v1/login')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "You are successfully logged in")
        self.assertEqual(response.status_code, 200)

    def test_signup(self):
        response = self.app.post('/api/v1/signup', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["first_name"], "gloria")
        self.assertEqual(result["last_name"], "odipo")
        self.assertEqual(result["username"], "gloria")
        self.assertEqual(result["email"], "godipo@gmail.com")
        self.assertEqual(result["password"], "bubble")
        self.assertEqual(response.status_code, 201)


class MealsTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.data = {
                    "meal_id": 1,
                    "meal_name": "rice with beef", 
                    "price": "ksh500",
                    "category": "main dish"
                    }

    def test_addmeals(self):
        response = self.app.post('/api/v1/meals', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["meal_id"], 1)
        self.assertEqual(result["meal_name"], "rice with beef")
        self.assertEqual(result["price"], "ksh500")
        self.assertEqual(result["category"], "main dish")
        self.assertEqual(response.status_code, 201) 

    def test_getallmeals(self):
        response = self.app.get('/api/v1/meals', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["meal_id"], 1)
        self.assertEqual(result["meal_name"], "rice with beef")
        self.assertEqual(result["price"], "ksh500")
        self.assertEqual(result["category"], "main dish")
        self.assertEqual(response.status_code, 200) 

    def test_updatemeal(self):
        response = self.app.put('/api/v1/meals/<int:1>', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["meal_id"], 1)
        self.assertEqual(result["meal_name"], "rice with beef")
        self.assertEqual(result["price"], "ksh700")
        self.assertEqual(result["category"], "main dish")
        self.assertEqual(response.status_code, 200) 

    def test_deletemeal(self):
        response = self.app.delete('/api/v1/meals/<int:1>', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["meal_id"], 1)
        self.assertEqual(result["meal_name"], "rice with beef")
        self.assertEqual(result["price"], "ksh500")
        self.assertEqual(result["category"], "main dish")
        self.assertEqual(response.status_code, 200) 


class OrderTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.data = {
                    "order_id": 1,
                    "customer": "gloria", 
                    "total": "ksh1500",
                    "order_items": "chapati with beef, fresh juice"
                    }
                    
    def test_addorder(self):
        response = self.app.post('/api/v1/orders', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["order_id"], 1)
        self.assertEqual(result["customer"], "gloria")
        self.assertEqual(result["total"], "ksh500")
        self.assertEqual(result["order_items"], "chapati with beef, fresh juice")
        self.assertEqual(response.status_code, 201) 

    def test_getallorders(self):
        response = self.app.get('/api/v1/orders', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["order_id"], 1)
        self.assertEqual(result["customer"], "gloria")
        self.assertEqual(result["total"], "ksh1500")
        self.assertEqual(result["order_items"], "chapati with beef, fresh juice")
        self.assertEqual(response.status_code, 200) 

    def test_updateorder(self):
        response = self.app.put('/api/v1/orders/<int:1>', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["order_id"], 1)
        self.assertEqual(result["customer"], "gloria")
        self.assertEqual(result["total"], "ksh1500")
        self.assertEqual(result["order_items"], "chapati with beef, fresh juice")
        self.assertEqual(response.status_code, 200) 

    

    if __name__ == '__main__':
        unittest.main()