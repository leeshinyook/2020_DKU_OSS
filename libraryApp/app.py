from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/searchBook/<book>')
def searchBook(book):
  print(book)
  return jsonify({"book" : book})

# 
@app.route('/rentBook', methods = ['PUT'])
def rentBook():
  book = request.get_json()
  return

@app.route('/returnBook', methods = ['PUT'])
def returnBook():
  return


@app.route('/searchAllBook')
def searchAllBook():
  return 

if __name__ == "__main__":
  app.run()