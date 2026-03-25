#Date 24-Mar-2026
# import sqlite3

# conn = sqlite3.connect('test.db')

# c = conn.cursor()
# # print(c)

# # query = '''CREATE TABLE IF NOT EXISTS user(
# #             user_id INTEGER PRIMARY KEY NOT NULL,
# #             first_name TEXT NOT NULL,
# #             height INTEGER
# #             )
# #             '''
# # c.execute(query)

# # my_data = ''' INSERT INTO user(user_id,first_name,height)
# #               VALUES (?,?,?) '''
# # for i in range(100):
# #     c.execute(my_data, (i, f'Bob-{i}', 170+i))
# # conn.commit()
# # conn.close()

# data = c.execute('SELECT * FROM user WHERE user_id=3').fetchall()
# print(data)

# c.execute('DELETE FROM user WHERE user_id=3')
# conn.commit()

