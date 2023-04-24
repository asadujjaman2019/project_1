from flask import Flask, jsonify
import json

f = open('quize.json')

app = Flask(__name__)
data = json.load(f)

@app.route('/books')
def list_of_books():
    books = [
        {'name': 'The Call of the Wild', 'author': 'Jack London'},
        {'name': 'Heart of Darkness', 'author': 'Joseph Conrad'}
    ]
    return jsonify(books)

@app.route('/quize')
def list_of_quize():

    return jsonify(data)

if __name__ == '__main__':
    app.run()