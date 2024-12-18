from flask import abort
import pymysql
from util.DB import DB

# 初期起動時にコネクションプールを作成し５つの接続を確立
db_pool = DB.init_db_pool()

# DB接続時にコネクションプールからコネクションを取得
# クエリ実行後、コネクションをプールに戻す

# ユーザークラス
class User:
    def create(uid, name, email, password):
        conn = db_pool.get_conn()
        try:
            with conn.cursor() as cur:
                sql = "INSERT INTO users (uid, user_name, email, password) VALUES (%s, %s, %s, %s);"
                cur.execute(sql, (uid, name, email, password))
                conn.commit()
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            db_pool.release(conn)


    def find_by_email(email):
        conn = db_pool.get_conn()
        try:
                with conn.cursor() as cur:
                    sql = "SELECT * FROM users WHERE email=%s;"
                    cur.execute(sql, (email))
                    user = cur.fetchone()
                return user
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            db_pool.release(conn)


# チャンネルクラス
class Channel:
    def create(uid, new_channel_name, new_channel_description):
        conn = db_pool.get_conn()
        try:
            with conn.cursor() as cur:
                sql = "INSERT INTO channels (uid, name, abstract) VALUES (%s, %s, %s);"
                cur.execute(sql, (uid, new_channel_name, new_channel_description))
                conn.commit()
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            db_pool.release(conn)


    def get_all():
        conn = db_pool.get_conn()
        try:
            with conn.cursor() as cur:
                sql = "SELECT * FROM channels;"
                cur.execute(sql)
                channels = cur.fetchall()
                return channels
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            db_pool.release(conn)


    def find_by_cid(cid):
        conn = db_pool.get_conn()
        try:
            with conn.cursor() as cur:
                sql = "SELECT * FROM channels WHERE id=%s;"
                cur.execute(sql, (cid))
                channel = cur.fetchone()
                return channel
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            db_pool.release(conn)


    def find_by_name(channel_name):
        conn = db_pool.get_conn()
        try:
            with conn.cursor() as cur:
                sql = "SELECT * FROM channels WHERE name=%s;"
                cur.execute(sql, (channel_name))
                channel = cur.fetchone()
                return channel
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            db_pool.release(conn)


    def update(uid, new_channel_name, new_channel_description, cid):
        conn = db_pool.get_conn()
        try:
            with conn.cursor() as cur:
                sql = "UPDATE channels SET uid=%s, name=%s, abstract=%s WHERE id=%s;"
                cur.execute(sql, (uid, new_channel_name, new_channel_description, cid))
                conn.commit()
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            db_pool.release(conn)


    def delete(cid):
        conn = db_pool.get_conn()
        try:
            with conn.cursor() as cur:
                sql = "DELETE FROM channels WHERE id=%s;"
                cur.execute(sql, (cid))
                conn.commit()
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            db_pool.release(conn)


# メッセージクラス
class Message:
    def create(uid, cid, message):
        conn = db_pool.get_conn()
        try:
            with conn.cursor() as cur:
                sql = "INSERT INTO messages(uid, cid, message) VALUES(%s, %s, %s)"
                cur.execute(sql, (uid, cid, message))
                conn.commit()
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            db_pool.release(conn)


    def get_all(cid):
        conn = db_pool.get_conn()
        try:
            with conn.cursor() as cur:
                sql = "SELECT id,u.uid, user_name, message FROM messages AS m INNER JOIN users AS u ON m.uid = u.uid WHERE cid = %s;"
                cur.execute(sql, (cid))
                messages = cur.fetchall()
                return messages
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            db_pool.release(conn)


    def delete(message_id):
        conn = db_pool.get_conn()
        try:
            with conn.cursor() as cur:
                sql = "DELETE FROM messages WHERE id=%s;"
                cur.execute(sql, (message_id))
                conn.commit()
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            db_pool.release(conn)

