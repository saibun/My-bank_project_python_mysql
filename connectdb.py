import mysql.connector

class Connect:
    def __init__(self):
        try:
            self.conn=mysql.connector.connect(host='localhost',user='root',password='',database='bank_users')
            self.mycursor = self.conn.cursor()
            print("Connected to Database")
        except:
            print("Some error occured")

    def register_user(self,store_name,store_account_no,store_password):
        try:
            query = "INSERT INTO all_users (user_id,name,account_number,password) VALUES (NULL,'{}','{}','{}')".format(store_name,store_account_no,store_password)
            self.mycursor.execute(query)
            self.conn.commit()
            return 1
        except:
            return 0


    def login_user(self,store_account_no,store_password):
        try:
            query = "SELECT * FROM all_users WHERE account_number LIKE '{}' AND password LIKE '{}'".format(store_account_no,store_password)
            self.mycursor.execute(query)
            data = self.mycursor.fetchall()
            return data
        except:
            return 0

    def fetch_user_data(self,user_id):
        try:
            query = "SELECT * FROM all_users WHERE user_id={}".format(user_id)
            self.mycursor.execute(query)
            data = self.mycursor.fetchall()
            return data
        except:
            return 0

    def store_capital(self,capital,account_id):
        try:
            query = "UPDATE all_users SET store_balance={} WHERE user_id={};".format(capital,account_id)
            self.mycursor.execute(query)
            self.conn.commit()
            return 1
        except:
            return 0

    def fetch_capital(self,user_id):
        try:
            query="SELECT * FROM all_users WHERE user_id LIKE {}".format(user_id)
            self.mycursor.execute(query)
            data = self.mycursor.fetchall()
            return data
        except:
            return 0


