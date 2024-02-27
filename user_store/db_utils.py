from typing import Dict


def insert_text_into_db(conn, table: str, kwargs: Dict[str, str]):
    keys = ','.join(kwargs.keys())
    q_marks = ','.join(['?' * len(kwargs)])

    sql = f"INSERT INTO {table}({keys}) VALUES({q_marks})"

    args = tuple(kwargs.values())
    conn.execute(sql, args)
    conn.commit()
    conn.close()



def describe_db_table(conn, table: str):

    conn = sqlite3.connect(USER_STORE_FILE_PATH)
    c = conn.cursor()

    c = conn.cursor()
    c.execute(f"PRAGMA table_info({table})")
    print(c.fetchall())
    conn.close()
