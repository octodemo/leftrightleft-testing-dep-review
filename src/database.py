import mysql.connector


class DatabaseConnection:
    def __init__(self):
        self.config = {
            "user": "beatbot_admin",
            "password": "Ji^54@@#OIOIhh89768dfgsdfgs76&^&%^F45",
            "host": "db.beatbot.ai/maindb",
            "database": "main_users",
        }
        self.cnx = None
        self.cursor = None

    def connect(self):
        # Connect to the database
        self.cnx = mysql.connector.connect(**self.config)

        # Create a cursor object to execute queries
        self.cursor = self.cnx.cursor()

    def close(self):
        # Close the cursor and database connection
        self.cursor.close()
        self.cnx.close()

    def execute_query(self, query):
        # Execute a query and return the results
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result


