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
  sql = """select * from book where title = %s"""
  cursor.execute(sql, book);
  result = cursor.fetchone()
  if(result is None):
    return jsonify({"result": "fail"})
  return jsonify({"book" : result})

@app.route('/addBook', methods = ['POST'])
def rentBook():
  data = request.get_json().get('book')
  try:
    sql = """insert into book(title) values(%s)"""  
    cursor.execute(sql, data)
    db.commit()
    return jsonify({'result' : 'success'})
  except:
    return jsonify({'result' : 'fail'})

@app.route('/deleteBook', methods = ['POST'])
def returnBook():
  data = request.get_json().get('book')
  try:
    sql = """delete from book where title=%s"""  
    cursor.execute(sql, data)
    db.commit()
    return jsonify({'result' : 'success'})
  except:
    return jsonify({'result' : 'fail'})

@app.route('/searchAllBook')
def searchAllBook():
  sql = """select * from book"""
  cursor.execute(sql)
  result = cursor.fetchall()
  return jsonify(result)

if __name__ == "__main__":
    print('Listening on 8080')
    app.run(host="127.0.0.1", port="8080")