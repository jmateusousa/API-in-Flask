from flask import Flask, request
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)

todos = {}

def abort_if_todo_doesnt_exist(number):
    if number not in todos:
        abort(404, message="Todo {} doesn't exist".format(number))

class Consultamacica(Resource):

    def get(self, number):
        abort_if_todo_doesnt_exist(number)
        return {number : todos[number]}

    def post(self):
        number  = len(todos) + 1
        todos[number] = request.form['data']
        return {number: todos[number]}

    def put(self, number):
        todos[number] = request.form['data']
        return {number: todos[number]}

    def delete(self, number):
        try:
            del todos[number]
            return {number: 'deletado'} 
        except:
            pass

api.add_resource(Consultamacica,'/', '/<int:number>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)