import unittest
import MySQLdb

class TestStateCreation(unittest.TestCase):
    def setUp(self):
        self.connection = MySQLdb.connect(user='hbnb_dev', host='localhost', password='hbnb_dev_pwd', db='hbnb_dev_db')
        self.cursor = self.connection.cursor()
        
    def tearDown(self):
        # Close the database connection
        self.connection.close()

    def test_create_state_command(self):
        # Get the initial number of records
        initial_count = self.get_records_count()


        # Get the number of records after the console command
        final_count = self.get_records_count()

        # Calculate the difference
        difference = final_count - initial_count

        # Assertion: Check if the difference is +1
        self.assertEqual(difference, 1)

    def get_records_count(self):
        # Query the database to get the number of records in the 'states' table
        self.cursor.execute("SELECT COUNT(*) FROM states")
        return self.cursor.fetchone()[0]

if __name__ == '__main__':
    unittest.main()
        