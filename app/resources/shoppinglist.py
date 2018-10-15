from flask_restful import Resource
from datetime import datetime
from app.models.shoppinglist import ShoppingList, Item
from app.models.user import User 


class ShoppingLists(Resource):
	def get(self):
		shoplists = ShoppingList.get_all()
		return {'shoppinglists': [ shoplist.to_dict() for shoplist in shoplists ]}, 201

	

	
	
