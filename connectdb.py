import mysql.connector
#Conncet with mysql database by importing mysql.connector library


class Connect:
    #Into constractor we create a function to connect with database.
    def __init__(self):
        try:
            #Creating connection object
            self.conn=mysql.connector.connect(host='localhost',user='root',password='',database='bank_users')
            self.mycursor = self.conn.cursor()
            print("Connected to Database")
        except:
            print("Some error occured")


    #By this function we store users name, account no, password into database.
    def register_user(self,store_name,store_account_no,store_password):
        try:
            query = "INSERT INTO all_users (user_id,name,account_number,password) VALUES (NULL,'{}','{}','{}')".format(store_name,store_account_no,store_password)
            self.mycursor.execute(query)
            self.conn.commit()
            return 1
        except:
            return 0


    #By this function we check user's enter account_no and password with accoutn_no and passord that present into the database .if it  same the user can log in 
    def login_user(self,store_account_no,store_password):
        try:
            query = "SELECT * FROM all_users WHERE account_number LIKE '{}' AND password LIKE '{}'".format(store_account_no,store_password)
            self.mycursor.execute(query)
            data = self.mycursor.fetchall()
            return data
        except:
            return 0


    #To fetch stored users data.
    def fetch_user_data(self,user_id):
        try:
            query = "SELECT * FROM all_users WHERE user_id={}".format(user_id)
            self.mycursor.execute(query)
            data = self.mycursor.fetchall()
            return data
        except:
            return 0

    #this function is for doing update user's account balance.
    def store_capital(self,capital,account_id):
        try:
            query = "UPDATE all_users SET store_balance={} WHERE user_id={};".format(capital,account_id)
            self.mycursor.execute(query)
            self.conn.commit()
            return 1
        except:
            return 0


    #For fetch user's account balance.
    def fetch_capital(self,user_id):
        try:
            query="SELECT * FROM all_users WHERE user_id LIKE {}".format(user_id)
            self.mycursor.execute(query)
            data = self.mycursor.fetchall()
            return data
        except:
            return 0
 
