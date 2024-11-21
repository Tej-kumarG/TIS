# import sqlite3
# import json
#
#
# class Database:
#     def __init__(self, db_name='colleges.db'):
#         self.conn = sqlite3.connect(db_name)
#         self.init_db()
#
#     def init_db(self):
#         cursor = self.conn.cursor()
#
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS colleges (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT UNIQUE,
#                 data TEXT
#             )
#         ''')
#
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS courses (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT,
#                 college_name TEXT,
#                 data TEXT
#             )
#         ''')
#
#         self.conn.commit()
#
#     def store_university_data(self, college_name, data):
#         cursor = self.conn.cursor()
#         cursor.execute('''
#             INSERT OR REPLACE INTO colleges (name, data) VALUES (?, ?)
#         ''', (college_name, json.dumps(data)))
#         self.conn.commit()
#
#     def retrieve_college_data(self, college_name):
#         cursor = self.conn.cursor()
#         cursor.execute('SELECT data FROM colleges WHERE name = ?', (college_name,))
#         result = cursor.fetchone()
#         return json.loads(result[0]) if result else None
#
#     def retrieve_courses_data(self, college_name):
#         cursor = self.conn.cursor()
#         cursor.execute('SELECT data FROM courses WHERE college_name = ?', (college_name,))
#         results = cursor.fetchall()
#
#         # Extract JSON from each row and return as a list
#         return [json.loads(row[0]) for row in results] if results else []
#
#     def store_courses_data(self, college_name, course_name, data):
#         cursor = self.conn.cursor()
#         cursor.execute('''
#             INSERT OR REPLACE INTO courses (name, college_name, data) VALUES (?, ?, ?)
#         ''', (course_name, college_name, json.dumps(data)))
#         self.conn.commit()
#
#     def close(self):
#         self.conn.close()
