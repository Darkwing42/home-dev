from app import db

class ShopList(db.Model):
    
    __tablename__ = 'shoplists'

    shoplistID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    items = db.relationship('Item', backref='ShopList', lazy=True)

    def to_dict(self):
        return dict(
                shoplistID=self.shoplistID,
                title=self.title,
                items=[item.to_dict() for item in self.items]
                )

    def save(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_all(cls):
        return cls.query.all()


class Item(db.Model):
    __tablename__ = 'items'

    itemID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    list_id = db.Column(db.Integer, db.ForeignKey('shoplists.shoplistID'))

    def to_dict(self):
        return dict(
                itemID=self.itemID,
                name=self.name,
                list_id=self.list_id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()




