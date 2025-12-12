from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from ..models import (customer as modelCustomer,
                      promo as modelPromo,
                      ingredient as modelIngredient,
                      pizza as modelPizza,
                      ingredient_usage as modelIngredientUsage,
                      orders as modelOrders,
                      order_details as modelOrderDetails,
                      payment as modelPayment,
                      review as modelReview)


def setup_database(db: Session):
    # Reset all database tables to initial state with default data
    try:
        # Clear all tables in correct order to respect foreign key constraints
        db.query(modelOrderDetails.OrderDetail).delete()
        db.query(modelIngredientUsage.IngredientUsage).delete()
        db.query(modelReview.Review).delete()
        db.query(modelOrders.Order).delete()
        db.query(modelPayment.Payment).delete()
        db.query(modelPromo.Promo).delete()
        db.query(modelPizza.Pizza).delete()
        db.query(modelIngredient.Ingredient).delete()
        db.query(modelCustomer.Customer).delete()
        
        db.commit()
        
        # Add Customers
        customer_data = [
            {"id": 1, "name": "Guest", "email": "guest@guest.com", "phone": "0000000000", "address": "000 guest dr."},
        ]
        for customer_data in customer_data:
            customer = modelCustomer.Customer(**customer_data)
            db.add(customer)

        # Add Promos
        promo_data = [
            {"id": 1, "code": 0, "discount": 0, "expiration_date": "9999-12-31 23:59:59"},
        ]

        for promo_data in promo_data:
            promo = modelPromo.Promo(**promo_data)
            db.add(promo)

        # Add Ingredients
        ingredients_data = [
            {"id": 1, "name": "crust", "amount": 50},
            {"id": 2, "name": "sauce", "amount": 75},
            {"id": 3, "name": "cheese", "amount": 100},
            {"id": 4, "name": "sausage", "amount": 25},
            {"id": 5, "name": "pepperoni", "amount": 25},
            {"id": 6, "name": "ham", "amount": 25},
            {"id": 7, "name": "mushroom", "amount": 25},
            {"id": 8, "name": "green pepper", "amount": 25},
            {"id": 9, "name": "olive", "amount": 10},
            {"id": 10, "name": "onion", "amount": 20}
        ]
        
        for ingredient_data in ingredients_data:
            ingredient = modelIngredient.Ingredient(**ingredient_data)
            db.add(ingredient)
        
        # Add Pizzas
        pizzas_data = [
            {"id": 1, "name": "Classic Cheese", "price": 11.99, "calories": 1800, "category": "Main"},
            {"id": 2, "name": "Classic Sausage", "price": 13.99, "calories": 2200, "category": "Main"},
            {"id": 3, "name": "Classic Pepperoni", "price": 12.99, "calories": 2100, "category": "Main"},
            {"id": 4, "name": "Triple Cheese", "price": 13.99, "calories": 2400, "category": "Specialty"},
            {"id": 5, "name": "Meat Lovers", "price": 15.99, "calories": 2700, "category": "Specialty"},
            {"id": 6, "name": "Supreme", "price": 14.99, "calories": 2300, "category": "Specialty"},
            {"id": 7, "name": "Vegetarian", "price": 13.99, "calories": 1900, "category": "Specialty"}
        ]
        
        for pizza_data in pizzas_data:
            pizza = modelPizza.Pizza(**pizza_data)
            db.add(pizza)
        
        db.flush()  # Flush to get IDs for foreign keys
        
        # Add Ingredient Usage
        ingredient_usage_data = [
            # Classic Cheese (ID: 1)
            {"id": 1, "pizza_id": 1, "ingredient_id": 1, "quantity": 1},
            {"id": 2, "pizza_id": 1, "ingredient_id": 2, "quantity": 2},
            {"id": 3, "pizza_id": 1, "ingredient_id": 3, "quantity": 4},
            # Classic Sausage (ID: 2)
            {"id": 4, "pizza_id": 2, "ingredient_id": 1, "quantity": 1},
            {"id": 5, "pizza_id": 2, "ingredient_id": 2, "quantity": 2},
            {"id": 6, "pizza_id": 2, "ingredient_id": 3, "quantity": 2},
            {"id": 7, "pizza_id": 2, "ingredient_id": 4, "quantity": 4},
            # Classic Pepperoni (ID: 3)
            {"id": 8, "pizza_id": 3, "ingredient_id": 1, "quantity": 1},
            {"id": 9, "pizza_id": 3, "ingredient_id": 2, "quantity": 2},
            {"id": 10, "pizza_id": 3, "ingredient_id": 3, "quantity": 2},
            {"id": 11, "pizza_id": 3, "ingredient_id": 5, "quantity": 4},
            # Triple Cheese (ID: 4)
            {"id": 12, "pizza_id": 4, "ingredient_id": 1, "quantity": 1},
            {"id": 13, "pizza_id": 4, "ingredient_id": 2, "quantity": 2},
            {"id": 14, "pizza_id": 4, "ingredient_id": 3, "quantity": 12},
            # Meat Lovers (ID: 5)
            {"id": 15, "pizza_id": 5, "ingredient_id": 1, "quantity": 1},
            {"id": 16, "pizza_id": 5, "ingredient_id": 2, "quantity": 2},
            {"id": 17, "pizza_id": 5, "ingredient_id": 3, "quantity": 2},
            {"id": 18, "pizza_id": 5, "ingredient_id": 4, "quantity": 3},
            {"id": 19, "pizza_id": 5, "ingredient_id": 5, "quantity": 3},
            {"id": 20, "pizza_id": 5, "ingredient_id": 6, "quantity": 3},
            # Supreme (ID: 6)
            {"id": 21, "pizza_id": 6, "ingredient_id": 1, "quantity": 1},
            {"id": 22, "pizza_id": 6, "ingredient_id": 2, "quantity": 2},
            {"id": 23, "pizza_id": 6, "ingredient_id": 3, "quantity": 2},
            {"id": 24, "pizza_id": 6, "ingredient_id": 4, "quantity": 1},
            {"id": 25, "pizza_id": 6, "ingredient_id": 5, "quantity": 1},
            {"id": 26, "pizza_id": 6, "ingredient_id": 6, "quantity": 1},
            {"id": 27, "pizza_id": 6, "ingredient_id": 7, "quantity": 1},
            {"id": 28, "pizza_id": 6, "ingredient_id": 8, "quantity": 1},
            {"id": 29, "pizza_id": 6, "ingredient_id": 9, "quantity": 1},
            {"id": 30, "pizza_id": 6, "ingredient_id": 10, "quantity": 1},
            # Vegetarian (ID: 7)
            {"id": 31, "pizza_id": 7, "ingredient_id": 1, "quantity": 1},
            {"id": 32, "pizza_id": 7, "ingredient_id": 2, "quantity": 2},
            {"id": 33, "pizza_id": 7, "ingredient_id": 3, "quantity": 2},
            {"id": 34, "pizza_id": 7, "ingredient_id": 7, "quantity": 3},
            {"id": 35, "pizza_id": 7, "ingredient_id": 8, "quantity": 3},
            {"id": 36, "pizza_id": 7, "ingredient_id": 9, "quantity": 3},
            {"id": 37, "pizza_id": 7, "ingredient_id": 10, "quantity": 3}
        ]
        
        for usage_data in ingredient_usage_data:
            usage = modelIngredientUsage.IngredientUsage(**usage_data)
            db.add(usage)
        
        db.commit()
        
        return {
            "status": "success",
            "message": "Database has been reset to initial state",
            "tables_initialized": [
                "customers",
                "promos", 
                "ingredients",
                "pizza",
                "ingredient_usage"
            ],
            "default_records_added": {
                "customers": 1,
                "promos": 1,
                "ingredients": 10,
                "pizzas": 7,
                "ingredient_usage": 37
            }
        }
        
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__['orig']) if 'orig' in e.__dict__ else str(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database setup failed: {error}"
        )