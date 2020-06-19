import pymysql
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

db = pymysql.connect(host='localhost',
                    port=3306,
                     user='root',
                     passwd='test',
                     db='library',
                     charset='utf8')
cursor = db.cursor()



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
  # print(cursor.fetchall())
  return jsonify(cursor.fetchall())

if __name__ == "__main__":
    print('Listening on 8080')
    app.run(host="127.0.0.1", port="8080")