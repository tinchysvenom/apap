# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 06:26:08 2020

@author: USER
"""

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=False)


# puts data in
# put('http://localhost:5000/todo1', data={'data': 'Remember the milk'}).json()

# gets data out
# get('http://localhost:5000/todo1').json()