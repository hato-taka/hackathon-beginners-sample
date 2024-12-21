import pymysql
from pymysqlpool.pool import Pool


class DB:
    def init_db_pool():
        pool = Pool(
            host="db",
            user="testuser",
            password="testuser",
            database="chatapp",
            max_size=5,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )
        pool.init()
        return pool
