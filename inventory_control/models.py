from inventory_control import db
from sqlalchemy.orm import relationship

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.Text)
    price = db.Column(db.Float)

    inventories = relationship("Inventory", back_populates="product")

class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    inventories = relationship("Inventory", back_populates="location")

class Inventory(db.Model):
    __tablename__ = 'inventories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    quantity = db.Column(db.Integer)

    product = relationship("Product", back_populates="inventories")
    location = relationship("Location", back_populates="inventories")