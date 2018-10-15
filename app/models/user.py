from app import db
from datetime import datetime
from app.models.shoppinglist import ShoppingList
from app.models.preferences import Preferences

class User(db.Model):
	__tablename__ = 'users'
	
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(120), nullable=False)
	
	password = db.Column(db.String(128), nullable=False)
	email = db.Column(db.String(120))
	
	preferences = db.relationship('Preferences', backref='User', lazy=True)
	shopppingLists = db.relationship('ShoppingList', backref='User', lazy=False)
	
	def hash_password(self):
		pass
	
	def check_password(self):
		pass
	
	def to_dict(self):
		return dict(
			id=self.id,
			username=self.username,
			email=self.username,
			shoppingLists=[ shopList.to_dict()  for shopList in self.shoppingLists ]
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
		return cls.query.filter_by(id=id).first()
	