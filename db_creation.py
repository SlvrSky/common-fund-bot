import sqlite3
from pathlib import Path
from config import DATABASE_NM, TABLE_NM

def sqlite_connect():
    conn = sqlite3.connect(DATABASE_NM, check_same_thread=False)
    conn.execute("pragma journal_mode=wal;")
    return conn

# подумать над тем, чтобы разделить методы коннект и инит, тк бд может быть создана, а таблицы в ней может не быть
# + подумать над добавлением в инит кваргов, чтобы можно было через этот метод создавать любые таблицы
def init_sqlite():
    conn = sqlite_connect()
    c = conn.cursor()
    c.execute(f'''CREATE TABLE {TABLE_NM}(  id                 integer primary key autoincrement
                                          , user_id            integer
                                          , transaction_amt    real
                                          , transaction_desc   text
                                          , transaction_dttm   integer
                                          , balance_amt        real
                                          )''')
    conn.commit()
    conn.close()
    return


db = Path("./database.db")
try:
    db.resolve(strict=True)
    print("Database already exists")
except FileNotFoundError:
    print("Database not found, trying to create a new one.")
    try:
        init_sqlite()
    except Exception as e:
        print("Error when creating database : ", e.__repr__(), e.args)
        pass
    else:
        print("Success.")

# #
# con = sqlite3.connect('db/example.db')
# # def char_generator():
# #     for c in string.ascii_lowercase:
# #         yield (c,)
# #
# cur = con.cursor()
# #cur.execute("create table characters(c)")
#
# cur.execute("insert into characters(c) values (?)", '2')
#
#
# print(cur.lastrowid)
#
# last_row_id = cur.lastrowid
# #cur.execute(f"select c from characters where rowid = {last_row_id}")
# cur.execute(f"select max(rowid) from characters")  # where rowid = 1
# res = cur.fetchall()
# print(res)
#
# con.commit()
# con.close()