from app import db
from app.models.user import User

class Preferences(db.Model):
	__tablename__ = 'preferences'
	
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	weather_api_key = db.Column(db.String(50))
	
	
