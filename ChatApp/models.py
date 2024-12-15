from flask import abort
import pymysql
from util.DB import DB


# ユーザーに関するクラス
class User:
    def create(uid, name, email, password):
        try:
            conn = DB.get_db_connection()
            with conn:
                with conn.cursor() as cur:
                    sql = "INSERT INTO users (uid, user_name, email, password) VALUES (%s, %s, %s, %s);"
                    cur.execute(sql, (uid, name, email, password))
                    conn.commit()
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)



    def find_by_email(email):
        try:
            conn = DB.get_db_connection()
            with conn:
                with conn.cursor() as cur:
                    sql = "SELECT * FROM users WHERE email=%s;"
                    cur.execute(sql, (email))
                    user = cur.fetchone()
                return user
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)



# チャンネルに関するクラス
class Channel:
    def create(uid, newChannelName, newChannelDescription):
        try:
            conn = DB.get_db_connection()
            with conn:
                with conn.cursor() as cur:
                    sql = "INSERT INTO channels (uid, name, abstract) VALUES (%s, %s, %s);"
                    cur.execute(sql, (uid, newChannelName, newChannelDescription))
                    conn.commit()
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)



    def get_all():
        try:
            conn = DB.get_db_connection()
            with conn:
                with conn.cursor() as cur:
                    sql = "SELECT * FROM channels;"
                    cur.execute(sql)
                    channels = cur.fetchall()
                    return channels
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)



    def find_by_CID(cid):
        try:
            conn = DB.get_db_connection()
            with conn:
                with conn.cursor() as cur:
                    sql = "SELECT * FROM channels WHERE id=%s;"
                    cur.execute(sql, (cid))
                    channel = cur.fetchone()
                    return channel
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)



    def find_by_name(channel_name):
        try:
            conn = DB.get_db_connection()
            with conn:
                with conn.cursor() as cur:
                    sql = "SELECT * FROM channels WHERE name=%s;"
                    cur.execute(sql, (channel_name))
                    channel = cur.fetchone()
                    return channel
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)



    def update(uid, newChannelName, newChannelDescription, cid):
        try:
            conn = DB.get_db_connection()
            with conn:
                with conn.cursor() as cur:
                    sql = "UPDATE channels SET uid=%s, name=%s, abstract=%s WHERE id=%s;"
                    cur.execute(sql, (uid, newChannelName, newChannelDescription, cid))
                    conn.commit()
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)



    def delete(cid):
        try:
            conn = DB.get_db_connection()
            with conn:
                with conn.cursor() as cur:
                    sql = "DELETE FROM channels WHERE id=%s;"
                    cur.execute(sql, (cid))
                    conn.commit()
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)



# メッセージに関するクラス
class Message:
    def create(uid, cid, message):
        try:
            conn = DB.get_db_connection()
            with conn:
                with conn.cursor() as cur:
                    sql = "INSERT INTO messages(uid, cid, message) VALUES(%s, %s, %s)"
                    cur.execute(sql, (uid, cid, message))
                    conn.commit()
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)



    def get_all(cid):
        try:
            conn = DB.get_db_connection()
            with conn:
                with conn.cursor() as cur:
                    sql = "SELECT id,u.uid, user_name, message FROM messages AS m INNER JOIN users AS u ON m.uid = u.uid WHERE cid = %s;"
                    cur.execute(sql, (cid))
                    messages = cur.fetchall()
                    return messages
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)



    def delete(message_id):
        try:
            conn = DB.get_db_connection()
            with conn:
                with conn.cursor() as cur:
                    sql = "DELETE FROM messages WHERE id=%s;"
                    cur.execute(sql, (message_id))
                    conn.commit()
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)

