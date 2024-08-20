import unittest
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel
from models import storage
from models.user import User
from io import StringIO

class TestConsoleCreateCommand(unittest.TestCase):
    """
    This class contains unit tests for the create command in the HBNBCommand class.
    Methods:
    - setUp: Method that runs before each test method to set up the necessary objects.
    - tearDown: Method that runs after each test method to clean up the created objects.
    - test_Create_basic: Method that tests the create command with basic usage.
    - test_create_with_params: Method that tests the create command with parameters.
    - test_create_invalid_params: Method that tests the create command with invalid parameters.
    - test_create_invalid_value: Method that tests the create command with an invalid value.
    - test_create_with_float_param: Method that tests the create command with a float parameter.
    """
    def setUp(self):
        self.console = HBNBCommand()
        self.test_objects = []
        
    def tearDown(self):
        for obj in self.test_objects:
            storage.delete(obj)
        self.test_objects = []
        
    def test_Create_basic(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            obj_id = mock_stdout.getvalue().strip()
            self.test_objects.append(storage.get(BaseModel, obj_id))
            self.assertIsInstance(storage.get('BaseModel', obj_id), BaseModel)

    def test_create_with_params(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd('create User email="test@example.com" password="password" age=25')
            obj_id = mock_stdout.getvalue().strip()
            self.test_objects.append(storage.get('User', obj_id))
            user_obj = storage.get('User', obj_id)
            self.assertIsInstance(user_obj, User)
            self.assertEqual(user_obj.email, "test@example.com")
            self.assertEqual(user_obj.password, "password")
            self.assertEqual(user_obj.age, 25)

    def test_create_invalid_params(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd('create BaseModel invalid_param="value"')
            output = mock_stdout.getvalue().strip()
            self.assertIn("Invalid parameter format: invalid_param=value. Skipping.", output)

    def test_create_invalid_value(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd('create BaseModel name="My_"invalid_house')
            output = mock_stdout.getvalue().strip()
            self.assertIn("Invalid value for parameter name: My_\"invalid_house. Skipping.", output)

    def test_create_with_float_param(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd('create BaseModel value=3.14')
            obj_id = mock_stdout.getvalue().strip()
            self.test_objects.append(storage.get('BaseModel', obj_id))
            self.assertIsInstance(storage.get('BaseModel', obj_id), BaseModel)
            self.assertEqual(storage.get('BaseModel', obj_id).value, 3.14)

if __name__ == '__main__':
    unittest.main()