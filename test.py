import datetime
import sqlite3
from config import DATABASE_NM, TABLE_NM

# get the current datetime and store it in a variable
currentDateTime = datetime.datetime.now().timestamp()
print(currentDateTime)

conn = sqlite3.connect(DATABASE_NM, check_same_thread=False)
conn.execute("pragma journal_mode=wal;")
c = conn.cursor()

# c.execute(f'''INSERT INTO {TABLE_NM}(user_id, transaction_amt, transaction_desc, transaction_dttm, balance_amt)
#                    VALUES
#                         (
#                               ?
#                             , ?
#                             , ?
#                             , ?
#                             , ?
#                         )
#                 ''', (123, 213, 'sdfsdf',datetime.datetime.now().timestamp(), 1213))
# conn.commit()


#c.execute(f"SELECT * FROM {TABLE_NM}")
#c.execute(f"PRAGMA table_info({TABLE_NM})")
# c.execute(f'''SELECT *
#               FROM {TABLE_NM}
#               WHERE 1 = 1
#               --  AND transaction_desc BETWEEN '2023-06-16 11:28:55.742950' and '2023-06-16 11:28:58'
#               --order by transaction_dttm desc''')
# print(c.fetchall())


def select_balance(conn):
    cursor = conn.cursor()
    cursor.execute(f'''SELECT balance_amt FROM {TABLE_NM}
                       ORDER BY transaction_dttm DESC
                       LIMIT 1''')
    return cursor.fetchone()

print(select_balance(conn)[0])