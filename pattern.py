import json

from utils import *
from config import db

"""=================== USERS ==================="""


def pattern_for_user(data_base):
    """
    Шаблон для Пользователей
    """
    for data_ in data_base:
        db.session.add(User(**data_))

    db.session.commit()


# def get_all_users():
#     """
#     Получаем список всех пользователей
#     """
#     dict_users = []
#     for user in db.session.query(User).all():
#         dict_users.append(user.user_dict())
#     return dict_users


# def get_user_by_id(User, user_id):
#     """
#     Получаем пользователя по его 'id'
#     """
#     return db.session.query(User).get(user_id).to_dict()


"""=================== ORDERS ==================="""


def pattern_for_order(data_base):
    """
    Шаблон для заказов
    """
    for data_ in data_base:
        db.session.add(Order(**data_))

    db.session.commit()


# def get_all_orders():
#     """
#     Получаем список всех заказов
#     """
#     dict_orders = []
#     for order in db.session.query(Order).all():
#         dict_orders.append(order.order_dict())
#     return dict_orders


# def get_order_by_id(Order, order_id):
#     """
#     Получаем все заказы по 'id'
#     """
#     return db.session.query(Order).get(order_id).to_dict()


"""=================== OFFERS ==================="""


def pattern_for_offer(data_base):
    """
    Шаблон для предложений
    """
    for data_ in data_base:
        db.session.add(Offer(**data_))

    db.session.commit()


# def get_all_offers():
#     """
#     Получаем список всех предложений
#     """
#     dict_offers = []
#     for offer in db.session.query(Offer).all():
#         dict_offers.append(offer.offer_dict())
#     return dict_offers


# def get_offer_by_id(Offer, offer_id):
#     """
#     Получаем все предложения по 'id'
#     """
#     return db.session.query(Offer).get(offer_id).to_dict()


"""=================== SERVICE ==================="""


def get_for_all(model):
    data_base = []
    for data in db.session.query(model).all():
        data_base.append(data.to_dict())
    return data_base


def get_for_all_by_id(model, user_id):
    try:
        return db.session.query(model).get(user_id).to_dict()
    except Exception:
        return {}


def update_data_for_all(model, user_id, values):
    """
    Обновление данных
    """
    try:
        db.session.query(model).filter(model.id == user_id).update(values)
        db.session.commit()
    except Exception as error:
        print(error)
        return {}


def delete_data_for_all(model, user_id):
    """
    Удаление данных
    """
    try:
        db.session.query(model).filter(model.id == user_id).delete()
        db.session.commit()
    except Exception as error:
        print(error)
        return {}


db.drop_all()
db.create_all()

with open("data/user.json") as file:
    pattern_for_user(json.load(file))

with open("data/offer.json") as file:
    pattern_for_offer(json.load(file))

with open("data/order.json") as file:
    pattern_for_order(json.load(file))
