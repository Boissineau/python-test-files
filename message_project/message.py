import psycopg2

def create_user(username):
    exist = find_user(username)
    if not exist:
        print('creating new user')
        with con:
            with con.cursor() as curs:
                sql = """INSERT INTO user_information (username) VALUES (%s);"""
                curs.execute(sql, (username,))
    else:
        print('User already exists')


def find_user(username):
    with con:
        with con.cursor() as curs:
            sql = """SELECT * from user_information WHERE username LIKE (%s)"""
            curs.execute(sql, (username,))
            rows = curs.fetchall()
    if len(rows) > 0:
        return True
    else:
        return False



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
    create_user(username)



    con.close()





