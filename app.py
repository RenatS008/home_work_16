import json

from config import app
from flask import request
from pattern import pattern_for_user, pattern_for_order, pattern_for_offer, get_for_all, get_for_all_by_id, \
    update_data_for_all, delete_data_for_all

from utils import *

"""=================== USERS ==================="""


@app.route("/users/", methods=['GET', 'POST'])
def all_users():
    """
    В зависимости от метода выполняем:
         'GET' - получаем весь список пользователей,
         'POST' - создание пользователя.
    """
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_for_all(User), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            pattern_for_user(request.json)
        elif isinstance(request.json, dict):
            pattern_for_user([request.json])
        else:
            print("File type is not defined")

        return app.response_class(
            response=json.dumps(["Added successfully"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/users/<int:user_id>/", methods=['GET', 'PUT', 'DELETE'])
def user_by_id(user_id):
    """
    В зависимости от метода выполняем:
         'GET' - получаем пользователя по его id,
         'PUT' - обновляем данные пользователя по его id,
         'DELETE' - удаляем пользователя по его id.
    """
    if request.method == 'GET':
        data = get_for_all_by_id(User, user_id)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        update_data_for_all(User, user_id, request.json)
        return app.response_class(
            response=json.dumps(["Updated successfully"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'DELETE':
        delete_data_for_all(User, user_id)
        return app.response_class(
            response=json.dumps(["Deleted successfully"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


"""=================== ORDERS ==================="""


@app.route("/orders/", methods=['GET', 'POST'])
def all_orders():
    """
    В зависимости от метода выполняем:
         'GET' - получаем весь список заказов,
         'POST' - создание заказа.
    """
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_for_all(Order), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            pattern_for_order(request.json)
        elif isinstance(request.json, dict):
            pattern_for_order([request.json])
        else:
            print("File type is not defined")

        return app.response_class(
            response=json.dumps(["Added successfully"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/orders/<int:order_id>/", methods=['GET', 'PUT', 'DELETE'])
def order_by_id(order_id):
    """
    В зависимости от метода выполняем:
         'GET' - получаем заказ по его id,
         'PUT' - обновляем данные заказа по его id,
         'DELETE' - удаляем заказ по его id.
    """
    if request.method == 'GET':
        data = get_for_all_by_id(Order, order_id)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        update_data_for_all(Order, order_id, request.json)
        return app.response_class(
            response=json.dumps(["Updated successfully"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'DELETE':
        delete_data_for_all(Order, order_id)
        return app.response_class(
            response=json.dumps(["Deleted successfully"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


"""=================== OFFERS ==================="""


@app.route("/offers/", methods=['GET', 'POST'])
def all_offers():
    """
    В зависимости от метода выполняем:
         'GET' - получаем весь список предложений,
         'POST' - создание предложения.
    """
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_for_all(Offer), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            pattern_for_offer(request.json)
        elif isinstance(request.json, dict):
            pattern_for_offer([request.json])
        else:
            print("File type is not defined")

        return app.response_class(
            response=json.dumps(["Added successfully"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/offers/<offer_id>/", methods=['GET', 'PUT', 'DELETE'])
def offer_by_id(offer_id):
    """
    В зависимости от метода выполняем:
         'GET' - получаем предложение по его id,
         'PUT' - обновляем данные предложение по его id,
         'DELETE' - удаляем предложение по его id.
    """
    if request.method == 'GET':
        data = get_for_all_by_id(Offer, offer_id)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        update_data_for_all(Offer, offer_id, request.json)
        return app.response_class(
            response=json.dumps(["Updated successfully"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'DELETE':
        delete_data_for_all(Offer, offer_id)
        return app.response_class(
            response=json.dumps(["Deleted successfully"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


if __name__ == "__main__":
    app.run(debug=True)
