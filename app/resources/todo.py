from app.models.todo import TodoItem, TodoList
from flask import request
from flask_restful import Resource
from app import db

class TodoList(Resource):
    def get(self):
        try:
            lists = TodoList.query.all()
            return {'todoLists': [l.to_dict()  for l in lists] }, 201
        except:
            return {'message': 'No Data'}, 500


    def post(self):

        data = request.get_json()

        print(data)

        todo_list = TodoList(
               list_name=data['list_name'],
               done=data['done'],
                )
        
        todo_items_list = []
        for item in data['todo_items']:
            obj = TodoItem(
                    name=item['name'],
                    done=item['done']
                        )
            todo_items_list.append(obj)

        todo_list.todo_items = todo_items_list

        db.session.add(todo_list)
        db.session.commit()

        return {'message': 'Successfully saved new data'}, 201
