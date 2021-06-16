import psycopg2

conn = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='brendan'
)



conn.close()

# # connect to the db
# con = psycopg2.connect(
#     host = 'localhost',
#     database ='messages_project',
#     user = 'postgres',
#     password = 'brendan',
#     port = '5432'
# )

# # cursor
# # client-side: allocate memory for everything (pull everything from server to client then start processing)
# # server-side: create cursor but do not obtain anything until they are asked for
# cur = con.cursor()

# # execute query
# cur.execute('select text, user from messages')

# rows = cur.fetchall()

# for r in rows:
#     print(f'user: {r[1]} message: {r[0]}')

# # close the cursor
# cur.close()
# # close the connection
# con.close()





