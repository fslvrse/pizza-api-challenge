from flask import Blueprint, request, jsonify
from ..models.restaurant_pizza import RestaurantPizza
from ..models.pizza import Pizza
from ..models.restaurant import Restaurant
from ..app import db

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizza_bp.route('', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    if not RestaurantPizza.validate_price(price):
        return jsonify({'errors': ['Price must be between 1 and 30']}), 400

    rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
    db.session.add(rp)
    db.session.commit()

    return jsonify({
        'id': rp.id,
        'price': rp.price,
        'pizza_id': rp.pizza.id,
        'restaurant_id': rp.restaurant.id,
        'pizza': {
            'id': rp.pizza.id,
            'name': rp.pizza.name,
            'ingredients': rp.pizza.ingredients
        },
        'restaurant': {
            'id': rp.restaurant.id,
            'name': rp.restaurant.name,
            'address': rp.restaurant.address
        }
    }), 201
