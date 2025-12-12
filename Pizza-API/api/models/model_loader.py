from . import (orders, order_details, ingredient, ingredient_usage,
               payment, pizza, customer, promo, review)

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    customer.Base.metadata.create_all(engine)
    ingredient.Base.metadata.create_all(engine)
    ingredient_usage.Base.metadata.create_all(engine)
    payment.Base.metadata.create_all(engine)
    pizza.Base.metadata.create_all(engine)
    promo.Base.metadata.create_all(engine)
    review.Base.metadata.create_all(engine)
