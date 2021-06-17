import psycopg2

def create_user(con, username):
    user = find_user(con, username)
    if len(user) == 0:
        print('creating new user')
        with con:
            with con.cursor() as curs:
                sql = """INSERT INTO user_information (username) VALUES (%s);"""
                curs.execute(sql, (username,))
    else:
        print('User already exists')


def find_user(con, username):
    with con:
        with con.cursor() as curs:
            sql = """SELECT * from user_information WHERE username LIKE (%s)"""
            curs.execute(sql, (username,))
            rows = curs.fetchall()
    return rows

def create_message(con, username, message):
    user_id = find_user(con, username)
    user_id = user_id[0][0]

    with con:
        with con.cursor() as curs:
            sql = """INSERT INTO messages (message, user_id) VALUES (%s, %s);"""
            curs.execute(sql, (message, user_id))

def find_messages(con, username):
    user_id = find_user(con, username)
    user_id = str(user_id[0][0])
    with con:
        with con.cursor() as curs:
            sql = """SELECT message from messages WHERE user_id::text LIKE (%s)"""
            curs.execute(sql, (user_id,))
            messages = curs.fetchall()
    return messages

if __name__ == '__main__':
    con = psycopg2.connect(
        host = 'localhost',
        database ='messaging_project',
        user = 'postgres',
        password = 'brendan',
        port = '5432',
        # autocommit = True
    )

    username = 'lewis'
    message = 'ty!!!'
    # create_message(con, username, message)
    # create_user(con, username)
    messages = find_messages(con, username)
    if messages is not None:
        for message in messages:
            print(message[0])

    con.close()





