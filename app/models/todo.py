from app import db
from datetime import datetime

class TodoItem(db.Model):
    __tablename__ = 'todoItems'

    id = db.Column(db.Integer, primary_key=True)
    todoList_id = db.Column(db.Integer, db.ForeignKey('todoLists.id'), nullable=False)
    name = db.Column(db.String(200))
    done = db.Column(db.Boolean, default=False, nullable=False)
    
    
    def to_dict(self):
        return dict(
                name=self.name,
                done=self.done
                )

class TodoList(db.Model):
    __tablename__ = 'todoLists'

    id = db.Column(db.Integer, primary_key=True)
    list_name = db.Column(db.String(200))
    todo_items = db.relationship('TodoItem', backref='todoList', lazy=False)
    done = db.Column(db.Boolean, default=False, nullable=False)


    def to_dict(self):
        return dict(
                list_name=self.list_name,
                done=self.done,
                todo_items=[l.to_dict() for l in self.todo_items]
                )



