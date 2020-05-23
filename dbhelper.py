import mysql.connector


class DBHelper:

    def __init__(self):
        #connect to database

        try:
            self._conn = mysql.connector.connect(host="127.0.0.1", user="root", password="", database="tinder")
            self._mycursor = self._conn.cursor()
        except:
            print("Can't connect to Database")
            exit()




    def check_login(self, email, password):

        # perform login
        self._mycursor.execute("SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}'".format(email, password))
        data = self._mycursor.fetchall()

        return data




    def fetch_userdata(self, user_id):

        # Displaying remaining information about the user
        self._mycursor.execute("SELECT * FROM users WHERE user_id NOT LIKE {}".format(user_id))
        data = self._mycursor.fetchall()

        return data



    def fetch_otheruserdata(self, user_id):

        self._mycursor.execute("SELECT * FROM proposals WHERE user_id NOT LIKE {}".format(user_id))
        data = self._mycursor.fetchall()

        return data


    
    def insert_proposal(self, romeo, juliet):

        self._mycursor.execute("SELECT * FROM proposals WHERE romeo = {} AND juliet={}".format(romeo, juliet))
        data = self._mycursor.fetchall()

        if len(data) == 0:
            try:
                self._mycursor.execute(
                    "INSERT INTO proposals (proposal_id, romeo, juliet) VALUES (NULL, '{}', '{}')".format(romeo,juliet))
                self._conn.commit()
                return 1
            except:
                return 0
        
        else:
            return 2

    def fetch_proposals(self, user_id):
        self._mycursor.execute("""SELECT * FROM proposals p JOIN users u ON u.user_id = p.romeo WHERE p.juliet={}""".format(user_id))
        data = self._mycursor.fetchall()

        return data



    def fetch_requests(self, user_id):
        self._mycursor.execute("""SELECT * FROM proposals p JOIN users u ON u.user_id = p.juliet WHERE p.romeo={}""".format(user_id))
        data = self._mycursor.fetchall()
        return data
                


    def fetch_matches(self, user_id):
        self._mycursor.execute("SELECT * FROM proposals JOIN users ON users.user_id=proposals.juliet WHERE juliet IN (SELECT romeo FROM proposals WHERE juliet={}) AND romeo={}".format(user_id, user_id))
        data = self._mycursor.fetchall()

        return data

    def register(self, name, email, password, age, gender, city, dp, intro):

        try:

            self._mycursor.execute("INSERT INTO usres (user_id, name, email, password, age, gender, city, dp, intro) VALUES (NULL, '{}','{}', '{}', {}, '{}', '{}', '{}', '{}')".format(name, email, password, age, gender, city, dp, intro))
            self._conn.commit()
            return 1
        except:
            return 0


    def update_info(self, n, a, c, fln, intr, user_id):

        try:
            self._mycursor.execute("UPDATE users SET name='{}', age={}, city='{}', dp='{}', intro='{}' WHERE user_id LIKE {}".format(n, a, c, fln, intr, user_id))
            self._conn.commit()
            return 1
        except:
            return 0