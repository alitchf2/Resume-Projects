from sqlalchemy.orm import Session
from datetime import datetime
from fastapi import HTTPException, status, Response, Depends
from ..models import (pizza as modelPizza,
                      orders as modelOrders,
                      customer as modelCustomer,
                      payment as modelPayment,
                      order_details as modelOrderDetails,
                      promo as modelPromo,
                      review as modelReview)
from sqlalchemy.exc import SQLAlchemyError

from ..schemas.pizza import PizzaUpdate
from ..schemas.orders import OrderUpdate
from ..schemas.customer import CustomerUpdate

def get_all_pizzas(db: Session):
    try:
        pizzas = db.query(modelPizza.Pizza).all()
        return pizzas
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def create_order(db:Session, request):
    new_item = modelOrders.Order(
        customer_id = request.customer_id,
        status = "pending",
        order_date = datetime.now(),
        total_price = 0.00,
        promo_id = None,
        delivery = request.delivery,
        payment_id = None
    )
    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item

def update_order(db:Session, item_id, request):
    try:
        item = db.query(modelOrders.Order).filter(modelOrders.Order.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        if item.first().status != "pending":
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Order can not be updated once paid or completed.")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()

def delete_order(db:Session, item_id):
    try:
        order_details = db.query(modelOrderDetails.OrderDetail).filter(modelOrderDetails.OrderDetail.order_id == item_id)
        order_details.delete(synchronize_session=False)
        item = db.query(modelOrders.Order).filter(modelOrders.Order.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not found")
        if item.first().status != "pending":
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Order can not be deleted once paid or completed.")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def create_order_details(db:Session, request):
    if request.amount <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Amount must be greater than 0."
        )

    pizza = (
        db.query(modelPizza.Pizza)
        .filter(modelPizza.Pizza.id == request.pizza_id)
        .first()
    )

    if not pizza:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pizza not found."
        )

    order = (
        db.query(modelOrders.Order)
        .filter(modelOrders.Order.id == request.order_id)
        .first()
    )

    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found."
        )
    
    if order.status != "pending":
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Order can not be updated once paid or completed.")

    new_item = modelOrderDetails.OrderDetail(
        order_id=request.order_id,
        pizza_id=request.pizza_id,
        amount=request.amount
    )

    try:
        order = db.query(modelOrders.Order).filter(modelOrders.Order.id == request.order_id).first()
        order.total_price += new_item.amount * db.query(modelPizza.Pizza).filter(modelPizza.Pizza.id == request.pizza_id).first().price

        db.add(new_item)
        db.add(order)
        db.commit()

        db.refresh(new_item)
        db.refresh(order)

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item

def update_order_details(db:Session, item_id, request):

    if hasattr(request, 'amount') and request.amount is not None:
        if request.amount < 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Amount must be greater than 0.")

    try:
        order_detail = db.query(modelOrderDetails.OrderDetail).filter(modelOrderDetails.OrderDetail.id == item_id).first()
        if not order_detail:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        
        old_cost = order_detail.amount * db.query(modelPizza.Pizza).filter(modelPizza.Pizza.id == order_detail.pizza_id).first().price

        item = db.query(modelOrderDetails.OrderDetail).filter(modelOrderDetails.OrderDetail.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        
        order = db.query(modelOrders.Order).filter(modelOrders.Order.id == request.order_id).first()
        if order.status != "pending":
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Order detail can not be updated once paid or completed.")

        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)

        order.total_price += request.amount * db.query(modelPizza.Pizza).filter(modelPizza.Pizza.id == request.pizza_id).first().price - old_cost
        if order.total_price < 0:
            order.total_price = 0.00

        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()

def delete_order_details(db:Session, item_id):
    try:

        order_detail = db.query(modelOrderDetails.OrderDetail).filter(modelOrderDetails.OrderDetail.id == item_id).first()
        if not order_detail:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        
        old_cost = order_detail.amount * db.query(modelPizza.Pizza).filter(modelPizza.Pizza.id == order_detail.pizza_id).first().price

        item = db.query(modelOrderDetails.OrderDetail).filter(modelOrderDetails.OrderDetail.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not found")
        
        order = db.query(modelOrders.Order).filter(modelOrders.Order.id == order_detail.order_id).first()
        if order.status != "pending":
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Order detail can not be deleted once paid or completed.")
        order.total_price -= old_cost
        if order.total_price < 0:
            order.total_price = 0.00

        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def create_customer(db:Session, request):
    new_item = modelCustomer.Customer(
        name = request.name,
        email = request.email,
        phone = request.phone,
        address = request.address
    )
    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item

def get_category(db: Session, category: str):
    try:
        pizzas = (
            db.query(modelPizza.Pizza)
            .filter(modelPizza.Pizza.category == category)
            .all()
        )
        if not pizzas:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No pizzas found in this category"
            )
        return pizzas

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )

def create_payment(db:Session, request):
    new_payment = modelPayment.Payment(
        payment_type = request.payment_type,
        card_info = request.card_info
    )
    try:
        db.add(new_payment)
        db.commit()
        db.refresh(new_payment)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return new_payment

def update_payment(db:Session, payment_id, request):
    try:
        payment = db.query(modelPayment.Payment).filter(modelPayment.Payment.id == payment_id)
        if not payment.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment information not found")
        update_data = request.dict(exclude_unset=True)
        payment.update(update_data)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return payment.first()

def delete_payment(db:Session, item_id):
    try:
        item = db.query(modelPayment.Payment).filter(modelPayment.Payment.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not found")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def get_order_status(db:Session, order_id):
    try:
        query = db.query(modelOrders.Order).filter(modelOrders.Order.id == order_id)
        order = query.first()

        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")

        return {
            "order_id": order.id,
            "status": order.status,
        }

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def pay_for_order(db:Session, order_id, payment_id):
    try:
        order = db.query(modelOrders.Order).filter(modelOrders.Order.id == order_id).first()

        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
        if order.status != "pending":
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Order has already been paid or completed")

        payment = db.query(modelPayment.Payment).filter(modelPayment.Payment.id == payment_id).first()

        if not payment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")

        order.payment_id = payment.id
        order.status = "paid"

        db.commit()
        db.refresh(order)

        return order

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    
def add_promo_to_order(db:Session, order_id, promo_code):
    try:
        order = db.query(modelOrders.Order).filter(modelOrders.Order.id == order_id).first()

        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
        if order.status != "pending":
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Order has already been paid or completed")
        
        if order.promo_id != None:
            old_promo = db.query(modelPromo.Promo).filter(modelPromo.Promo.id == order.promo_id).first()
            old_promo_amount = old_promo.discount
        else:
            old_promo_amount = 0

        promo = db.query(modelPromo.Promo).filter(modelPromo.Promo.code == promo_code).first()

        if not promo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promo not found")

        order.promo_id = promo.id

        order.total_price -= promo.discount + old_promo_amount
        if order.total_price < 0:
            order.total_price = 0.00

        db.commit()
        db.refresh(order)

        return order

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def create_review(db:Session, request):
    new_review = modelReview.Review(
        customer_id = request.customer_id,
        rating = request.rating,
        text = request.text,
        pizza_id = request.pizza_id
    )
    try:
        db.add(new_review)
        db.commit()
        db.refresh(new_review)

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_review

def delete_review(db:Session, item_id):
    try:
        item = db.query(modelReview.Review).filter(modelReview.Review.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not found")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def update_review(db:Session, review_id, request):
    try:
        review = db.query(modelReview.Review).filter(modelReview.Review.id == review_id)
        if not review.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found")
        update_data = request.dict(exclude_unset=True)
        review.update(update_data)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return review.first()


def create_review(db:Session, request):
    new_review = modelReview.Review(
        customer_id = request.customer_id,
        rating = request.rating,
        text = request.text,
        pizza_id = request.pizza_id
    )
    try:
        db.add(new_review)
        db.commit()
        db.refresh(new_review)

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_review

def delete_review(db:Session, item_id):
    try:
        item = db.query(modelReview.Review).filter(modelReview.Review.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not found")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def update_review(db:Session, review_id, request):
    try:
        review = db.query(modelReview.Review).filter(modelReview.Review.id == review_id)
        if not review.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found")
        update_data = request.dict(exclude_unset=True)
        review.update(update_data)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return review.first()