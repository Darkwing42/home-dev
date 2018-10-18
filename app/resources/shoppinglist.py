from flask_restful import Resource
from flask import request
from datetime import datetime
from app.models.shoppinglist import ShopList, Item


class ShoppingLists(Resource):
    def get(self):
        shoplists = ShopList.get_all()
        return {'shoppinglists': [ shoplist.to_dict() for shoplist in shoplists ]}, 201

class ShoppingList(Resource):

    def post(self):
          data = request.get_json()
          print("")
          print(data)
          items = []
          for item in data['items']:
              obj = Item(
                      name=item['name']
                      )
              items.append(obj)

          shopList = ShopList(
                  title=data['title'],
                  items=items
                  )

          shopList.save()
          return {'message': 'Liste angelegt'}, 201

