from flask import Flask, render_template, request, jsonify
import pymysql
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='test',
                     db='book',
                     charset='utf8')
cursor = db.cursor()
app = Flask(__name__)

# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'test'
# app.config['MYSQL_DATABASE_DB'] = 'library'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql = MySQL(app)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/searchBook/<book>')
def searchBook(book):
  print(book)
  return jsonify({"book" : book})

@app.route('/rentBook', methods = ['PUT'])
def rentBook():
  book = request.get_json()
  return

@app.route('/returnBook', methods = ['PUT'])
def returnBook():
  return

@app.route('/searchAllBook')
def searchAllBook():
  sql = """select * from book"""
  cursor.execute(sql)
  print(cursor.fetchall())
  return 

if __name__ == "__main__":
  app.run()