#from app.models.basemodel import BaseModel as db
from app import db
from datetime import datetime
from app.models.user import User

class Item(db.Model):
	__tablename__ = 'items'
	
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120), nullable=False)
	quantity = db.Column(db.Integer, nullable=False)
	date_created = db.Column(db.DateTime, default=datetime.now)
	date_modified = db.Column(db.DateTime, default=datetime.now, onchange=datetime.now)
	done = db.Column(db.Boolean, default=False)
	
	def save(self):
		db.session.add(self)
		db.session.commit()
	
	def delete(self):
		db.session.delete(self)
		db.session.commit()
		
	@classmethod
	def get_all(cls):
		return cls.query.all()
	
	@classmethod
	def get_by_id(cls, id):
		return cls.query.filter_by(id=id).first()
	
	def to_dict(self):
		return dict(
				id=self.id,
				name=self.name,
				quantity=self.quantity,
				date_created=self.date_created.strftime('%d-%m-%Y %H:%M'),
				date_modified=self.date_modified.strftime('%d-%m-%Y %H:%M'),
				done=self.done
			)

class ShoppingList(db.Model):
	__tablename__ = 'shoppinglists'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(120, nullable=False))
	date_created = db.Column(db.DateTime, default=datetime.now)
	date_modified = db.Column(db.DateTime, default=datetime.now, onchange=datetime.now)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	done = db.Column(db.Boolean, default=False)
	items = db.relationshiip('Item', backref='ShoppingList', lazy=False)
	
	def to_dict(self):
		return dict(
			id=self.id,
			title=self.title,
			date_created=self.date_created.strftime('%d-%m-%Y %H:%M'),
			date_modified=self.date_modified.strftime('%d-%m-%Y %H:%M'),
			done=self.done,
			items=[item.to_dict() for item in self.items ]
		)
	
	def save(self):
		db.session.add(self)
		db.session.commit()
		
	def delete(self):
		db.session.delete(self)
		db.session.commit()
		
	@classmethod
	def get_all(cls):
		return cls.query.all()
	
	@classmethod
	def get_by_id(cls, id):
		return cls.query.filter_by(id=id).first.()





