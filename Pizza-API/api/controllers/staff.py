from datetime import date
from sqlalchemy import func
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import (pizza as modelPizza, orders as modelOrders,
                      customer as modelCustomer, promo as modelPromo,
                      ingredient as modelIngredient, ingredient_usage as modelIngredientUsage,
                      order_details as modelOrderDetails, review as modelReview)
from sqlalchemy.exc import SQLAlchemyError

from ..schemas.pizza import PizzaUpdate
from ..schemas.orders import OrderUpdate
from ..schemas.customer import CustomerUpdate
from ..schemas.promo import PromoUpdate


def create_pizza(db:Session, request):
    new_item = modelPizza.Pizza(
        name=request.name,
        price=request.price,
        calories=request.calories,
        category=request.category
    )
    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def update_pizza(db:Session, item_id, request):
    try:
        item = db.query(modelPizza.Pizza).filter(modelPizza.Pizza.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()

def delete_pizza(db:Session, item_id):
    try:
        item = db.query(modelPizza.Pizza).filter(modelPizza.Pizza.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not found")
        item.delete(synchronize_session=False)
        db.commit()

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def create_promo(db:Session, request):
    new_item = modelPromo.Promo(
        code= request.code,
        discount = request.discount,
        expiration_date = request.expiration_date
    )
    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item

def update_promo(db:Session, item_id, request):
    try:
        item = db.query(modelPromo.Promo).filter(modelPromo.Promo.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    
    return item.first()

def create_ingredient(db:Session, request):
    new_ingredient = modelIngredient.Ingredient(
        name= request.name,
        amount=request.amount
    )
    try:
        db.add(new_ingredient)
        db.commit()
        db.refresh(new_ingredient)

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_ingredient

def update_ingredient(db:Session, ingredient_id, request):
    try:
        ingredient = db.query(modelIngredient.Ingredient).filter(modelIngredient.Ingredient.id == ingredient_id)
        if not ingredient.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not found")
        update_data = request.dict(exclude_unset=True)
        ingredient.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return ingredient.first()

def update_order_status(db:Session, order_id, request):
    try:
        valid_statuses = ["pending", "paid", "complete"]
        if request.status and request.status not in valid_statuses:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid status. Must be pending, paid, or complete")

        order = db.query(modelOrders.Order).filter(modelOrders.Order.id == order_id).first()
        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")

        if request.status == "complete":
            if order.status != "paid":
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Order can not be complete if not paid")

            if not check_and_update_inventory(db, order_id):
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not enough ingredients to complete this order")

        order.status = request.status
        db.commit()
        db.refresh(order)

        return order

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def check_and_update_inventory(db, order_id) -> bool:
    try:
        order_details = db.query(modelOrderDetails.OrderDetail).filter(modelOrderDetails.OrderDetail.order_id == order_id).all()

        if not order_details:
            return True

        ingredient_requirements = {}

        for order_detail in order_details:
            ingredient_usages = db.query(modelIngredientUsage.IngredientUsage).filter(modelIngredientUsage.IngredientUsage.pizza_id == order_detail.pizza_id).all()

            for usage in ingredient_usages:
                total_needed = usage.quantity * order_detail.amount
                if usage.ingredient_id in ingredient_requirements:
                    ingredient_requirements[usage.ingredient_id] += total_needed
                else:
                    ingredient_requirements[usage.ingredient_id] = total_needed

        for ingredient_id, total_needed in ingredient_requirements.items():
            ingredient = db.query(modelIngredient.Ingredient).filter(modelIngredient.Ingredient.id == ingredient_id).first()

            if not ingredient or ingredient.amount < total_needed:
                return False

        for ingredient_id, total_needed in ingredient_requirements.items():
            ingredient = db.query(modelIngredient.Ingredient).filter(modelIngredient.Ingredient.id == ingredient_id).first()

            ingredient.amount -= total_needed
            db.add(ingredient)

        db.commit()
        return True

    except SQLAlchemyError as e:
        db.rollback()
        return False

def create_ingredient_usage(db:Session, request):
    new_item = modelIngredientUsage.IngredientUsage(
        pizza_id= request.pizza_id,
        ingredient_id = request.ingredient_id,
        quantity = request.quantity
    )
    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item

def update_ingredient_usage(db:Session, item_id, request):
    try:
        item = db.query(modelIngredientUsage.IngredientUsage).filter(modelIngredientUsage.IngredientUsage.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()

def delete_ingredient_usage(db:Session, item_id):
    try:
        item = db.query(modelIngredientUsage.IngredientUsage).filter(modelIngredientUsage.IngredientUsage.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not found")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def get_reviews_by_customer(customer_id: int, db:Session):
    try:
        reviews = db.query(modelReview.Review).filter(modelReview.Review.customer_id == customer_id).all()

        if not reviews:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No reviews found from this customer"
            )
        return reviews

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )
    
def get_revenue_by_date(db: Session, target_date: date):
    revenue = (
        db.query(func.sum(modelOrders.Order.total_price))
        .filter(func.date(modelOrders.Order.order_date) == target_date)
        .scalar()
    )

    return revenue or 0

def get_all_orders(db: Session):
    try:
        orders = db.query(modelOrders.Order).all()
        return orders
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def get_orders_of_status(db: Session, ord_status):
    try:

        valid_statuses = ["pending", "paid", "complete"]
        if ord_status not in valid_statuses:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Status must be Pending, Paid, or Completed")

        orders = (
            db.query(modelOrders.Order)
            .filter(modelOrders.Order.status == ord_status)
            .all()
        )
        if not orders:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No orders found in with this status")
        return orders

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )

def get_orders_by_timeframe(db: Session, start_date, end_date):
    try:
        orders = (
            db.query(modelOrders.Order)
            .filter(modelOrders.Order.order_date >= start_date)
            .filter(modelOrders.Order.order_date <= end_date)
            .order_by(modelOrders.Order.order_date).all()
        )

        if not orders:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No orders found in with this timeframe")

        return orders

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    
def get_details_of_order(db: Session, order_id):
    try:
        order_details = (
            db.query(modelOrderDetails.OrderDetail)
            .filter(modelOrderDetails.OrderDetail.order_id == order_id)
            .all()
        )
        if not order_details:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No order details found for this order"
            )
        return order_details

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )