from flask_restful import Resource
from flask import request
from datetime import datetime
from app.models.shoppinglist import ShoppingList, Item
from app.models.user import User


class ShoppingLists(Resource):
	def get(self):
		shoplists = ShoppingList.get_all()
		return {'shoppinglists': [ shoplist.to_dict() for shoplist in shoplists ]}, 201

class ShoppingList(Resource):
	def get(self, id):
		# TODO: get shopping list with specific id
		pass

	def post(self):
		data = request.get_json()
		print(data)


		shoppingItems = []

		for item in data['items']:
			obj = Item(
			name=item['name'],
			quantity=item['quantity']
			)
			shoppingItems.append(obj)

		shopList = ShoppingList(
			title=data['title'],
			done=data['done']
		)
		shopList.save()
		return {'message': 'Liste angelegt'}, 201


	def put(self, id):
		pass

	def delete(self, id):
		pass
