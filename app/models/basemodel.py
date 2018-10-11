from app import db
from datetime import datetime

class BaseModel(db.Model):
	
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
		return cls.query.find_by(id=id).first()
	
