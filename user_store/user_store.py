from getpass import getpass
import os
import sqlite3

# TODO change into a class,  init once, then use methods to interact with the db

# TODO read: https://blog.rtwilson.com/a-python-sqlite3-context-manager-gotcha/
# TODO read: https://towardsdatascience.com/do-you-know-python-has-a-built-in-database-d553989c87bd
# TODO read: https://towardsdatascience.com/yes-python-has-a-built-in-database-heres-how-to-use-it-b3c033f172d3

USER_STORE_FOLDER = 'user_store'
USER_STORE_FILE = 'user_store.db'
USER_STORE_FILE_PATH = os.path.join(USER_STORE_FOLDER, USER_STORE_FILE)


def create_user_store(db_password: str):
    conn = sqlite3.connect(USER_STORE_FILE_PATH)
    c = conn.cursor()

    c.execute('''
        CREATE TABLE users(
            email TEXT PRIMARY KEY,
            secret TEXT NOT NULL
        )
    ''')

    encryption_canary = 'abcdef' # encrypt this using db_password
    c.execute(f'''
        INSERT INTO users(email, secret) VALUES('encryption-canary', '{encryption_canary}')
    ''')

    conn.commit()
    conn.close()


def init_user_store():
    # input password from console
    db_password = getpass('Enter db password:')
    # pbkdf2? argon2? bcrypt? how to encrypt password

    
    if not os.path.isfile(USER_STORE_FILE_PATH):
        create_user_store(db_password)

    # TODO - check db password against the encryption canary


def add_user(email: str, secret: str):
    conn = sqlite3.connect(USER_STORE_FILE_PATH)
    c = conn.cursor()

    # TODO encrypt secret

    c.execute(f'''
        INSERT INTO users(email, secret) VALUES('{email}', '{secret}')
    ''')

    conn.commit()
    conn.close()

def get_user_secret(email: str):
    # TODO - decrypt secret

    conn = sqlite3.connect(USER_STORE_FILE_PATH)
    c = conn.cursor()
    c.execute(f'''
        SELECT secret FROM users WHERE email = '{email}'
    ''')
    secret = c.fetchone()
    conn.close()

    if not secret:
        raise ValueError(f'User {email} not found in db')

    # TODO handle case when user is not found
    return secret[0]
    

# TODO - add a method to list all users
# TODO - add a method to remove user

# TODO - make cli command
def list_users():
    conn = sqlite3.connect(USER_STORE_FILE_PATH)
    c = conn.cursor()
    c.execute('SELECT email FROM users')
    users = c.fetchall()
    conn.close()

    return [user[0] for user in users]
