from marshmallow import Schema, fields

from config import db


class User(db.Model):
    """
    Модель для USER
    """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    role = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def to_dict(self):
        """
        Формируем словарь из полученных данных
        """
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "role": self.role,
            "phone": self.phone
        }


# class UserSchema(Schema):
#     id = fields.Integer(dump_only=True)
#     first_name = fields.String()
#     last_name = fields.String()
#     age = fields.Integer()
#     email = fields.String()
#     role = fields.String()
#     phone = fields.Integer()


class Offer(db.Model):
    """
    Модель для OFFER
    """
    __tablename__ = "offer"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def to_dict(self):
        """
        Формируем словарь из полученных данных
        """
        return {
            "id": self.id,
            "order_id": self.order_id,
            "executor_id": self.executor_id
        }


# class OfferSchema(Schema):
#     id = fields.Integer(dump_only=True)
#     order_id = fields.String()
#     executor_id = fields.String()


class Order(db.Model):
    """
    Модель для ORDER
    """
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100))
    start_date = db.Column(db.Integer)
    end_date = db.Column(db.Integer)
    address = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def to_dict(self):
        """
        Формируем словарь из полученных данных
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "address": self.address,
            "price": self.price,
            "customer_id": self.customer_id,
            "executor_id": self.executor_id
        }


# class OrderSchema(Schema):
#     id = fields.Integer(dump_only=True)
#     name = fields.String()
#     description = fields.String()
#     start_date = fields.Integer()
#     end_date = fields.Integer()
#     address = fields.String()
#     price = fields.Integer()
#     customer_id = fields.Integer()
#     executor_id = fields.Integer()
