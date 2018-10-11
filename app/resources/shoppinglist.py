from flask_restful import Resource, reqparser
from datetime import datetime
from app.models.shoppinglist import ShoppingList, Item
from app.models.user import User 


class ShoppingLists(Resource):
	def get(self):
		pass
	
class ShoppingList(Resource):
	def get(self, id):
		pass
	

	
	
