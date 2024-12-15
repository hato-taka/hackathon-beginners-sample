import pymysql

class DB:
    def get_db_connection():
        try:
            conn = pymysql.connect(
            host="db",
            db="chatapp",
            user="testuser",
            password="testuser",
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
            return conn
        except (ConnectionError):
            print("コネクションエラーです")
            conn.close()
