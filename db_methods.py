import sqlite3
import datetime
from config import TABLE_NM, DATABASE_NM


def insert_data(conn, balance_amt, user_id = -1, transaction_amt = -1, transaction_desc = 'Manual set balance'):
    cursor = conn.cursor()
    cursor.execute(f'''INSERT INTO {TABLE_NM}(user_id, transaction_amt, transaction_desc, transaction_dttm, balance_amt)
                       VALUES(?, ?, ?, ?, ?)'''
                   , (user_id, transaction_amt, transaction_desc, datetime.datetime.now().timestamp(), balance_amt))
    conn.commit()


def select_balance(conn):
    cursor = conn.cursor()
    cursor.execute(f'''SELECT balance_amt FROM {TABLE_NM}
                       ORDER BY transaction_dttm DESC
                       LIMIT 1''')
    return cursor.fetchone()[0]


conn = sqlite3.connect(DATABASE_NM, check_same_thread=False)
conn.execute("pragma journal_mode=wal;")



