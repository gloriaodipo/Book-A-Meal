from app.views import app
import unittest
import json



class UserTestCase(unittest.TestCase):
    """This class represents the user login and signup test case."""

    def setUp(self):
        """Initialize app and define of test variables"""
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.data = {
                    "first_name": "gloria",
                    "last_name": "odipo",
                    "username":"gloriaodipo", 
                    "email":"godipo@gmail.com",
                    "password":"bubble"
                    }
    
    def test_login(self):
        """Test API can successfully log in registered users using username and password (POST request)"""
        response = self.client.post('/api/v1/user/login/1')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "You are successfully logged in")
        self.assertEqual(response.status_code, 200)

    def test_wrong_login(self):
        """Test API cannot authenticate login when wrong password is used or no password supplied (POST request)"""
        response = self.client.post('/api/v1/user/login/4')
        result = json.loads(response.data)
        self.assertEqual(result["password"], "")
        self.assertNotEqual(result["password"], "bubble")
        self.assertEqual(response.status_code, 401)

    def test_signup(self):
        """Test API can successfully register a new user (POST request)"""
        response = self.client.post('user/api/v1/signup', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["first_name"], "gloria")
        self.assertEqual(result["last_name"], "odipo")
        self.assertEqual(result["username"], "gloria")
        self.assertEqual(result["email"], "godipo@gmail.com")
        self.assertEqual(result["password"], "bubble")
        self.assertEqual(response.status_code, 201)

    
    def test_wrong_signup(self):
        """Test API cannot successfully register a new user with no password(POST request)"""
        response = self.client.post('/api/v1/signup', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["first_name"], "gloria")
        self.assertEqual(result["last_name"], "odipo")
        self.assertEqual(result["username"], "gloria")
        self.assertEqual(result["email"], "godipo@gmail.com")
        self.assertEqual(result["error"], "No password provided")
        self.assertEqual(response.status_code, 401)


class MealsTestCase(unittest.TestCase):
    """This is the class for meals test cases"""

    def setUp(self):
        """Initialize app and define of test variables"""
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.data = {
                    "meal_id": 1,
                    "meal_name": "rice with beef", 
                    "price": "ksh500",
                    "category": "main dish"
                    }

    def test_add_meals(self):
        """Test API can add a meal (POST request)"""
        response = self.client.post('/api/v1/meals', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["meal_id"], 1)
        self.assertEqual(result["meal_name"], "rice with beef")
        self.assertEqual(result["price"], "ksh500")
        self.assertEqual(result["category"], "main dish")
        self.assertEqual(response.status_code, 201) 

    def test_get_all_meals(self):
        """Test API can get all meals (GET request)"""
        response = self.client.get('/api/v1/meals', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["meal_id"], 1)
        self.assertEqual(result["meal_name"], "rice with beef")
        self.assertEqual(result["price"], "ksh500")
        self.assertEqual(result["category"], "main dish")
        self.assertEqual(response.status_code, 200) 

    def test_get_one_meal(self):
        """Test API can get a single meal from the meals list using meal_id (GET request)"""
        response = self.client.get('/api/v1/meals/2', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["meal_id"], 1)
        self.assertEqual(result["meal_name"], "rice with beef")
        self.assertEqual(result["price"], "ksh500")
        self.assertEqual(result["category"], "main dish")
        self.assertEqual(response.status_code, 200)

    def test_update_meal(self):
        """Test API can modify/update details of a given meal using meal_id (PUT request)"""
        response = self.client.put('/api/v1/meals/2', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["meal_id"], 1)
        self.assertEqual(result["meal_name"], "rice with beef")
        self.assertEqual(result["price"], "ksh700")
        self.assertEqual(result["category"], "main dish")
        self.assertEqual(response.status_code, 200) 

    def test_delete_meal(self):
        """Test API can delete a meal using meal_id (DELETE request)"""
        response = self.client.delete('/api/v1/meals/2', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["meal_id"], 1)
        self.assertEqual(result["meal_name"], "rice with beef")
        self.assertEqual(result["price"], "ksh500")
        self.assertEqual(result["category"], "main dish")
        self.assertEqual(response.status_code, 200) 

    def test_delete_invalid_meal(self):
        """Test API can return a 204:no content when deleting a meal that's inexistent"""
        response = self.client.delete('/api/v1/meals/7', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["meal_id"], 2)
        self.assertEqual(result["meal_name"], "rice with beef")
        self.assertEqual(result["price"], "ksh500")
        self.assertEqual(result["category"], "main dish")
        self.assertEqual(response.status_code, 204)


class OrderTestCase(unittest.TestCase):
    """This is the class for orders test cases"""

    def setUp(self):
        """Initialize app and define of test variables"""
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.data = {
                    "order_id": 1,
                    "customer": "gloria", 
                    "total": "ksh1500",
                    "order_items": "chapati with beef, fresh juice"
                    }
                    
    def test_add_order(self):
        """Test API can add an order (POST request)"""
        response = self.client.post('/api/v1/orders', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["order_id"], 1)
        self.assertEqual(result["customer"], "gloria")
        self.assertEqual(result["total"], "ksh500")
        self.assertEqual(result["order_items"], "chapati with beef, fresh juice")
        self.assertEqual(response.status_code, 201) 

    def test_get_one_order(self):
        """Test API can get a single order using order_id (GET request)"""
        response = self.client.get('/api/v1/orders/<int:1>', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["order_id"], 1)
        self.assertEqual(result["customer"], "gloria")
        self.assertEqual(result["total"], "ksh500")
        self.assertEqual(result["order_items"], "chapati with beef, fresh juice")
        self.assertEqual(response.status_code, 200)    

    def test_get_all_orders(self):
        """Test API can get all orders (GET request)"""
        response = self.client.get('/api/v1/orders', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["order_id"], 1)
        self.assertEqual(result["customer"], "gloria")
        self.assertEqual(result["total"], "ksh1500")
        self.assertEqual(result["order_items"], "chapati with beef, fresh juice")
        self.assertEqual(response.status_code, 200) 

    def test_update_order(self):
        """Test can modify/update details an order using order_id (PUT request)"""
        response = self.client.put('/api/v1/orders/<int:1>', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["order_id"], 1)
        self.assertEqual(result["customer"], "gloria")
        self.assertEqual(result["total"], "ksh1500")
        self.assertEqual(result["order_items"], "chapati with beef, fresh juice")
        self.assertEqual(response.status_code, 200) 




if __name__ == '__main__':
    unittest.main()
