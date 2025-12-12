from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import customer as controller
from ..schemas import (pizza as schemaPizza,
                       orders as schemaOrders,
                       customer as schemaCustomer,
                       payment as schemaPayment,
                       order_details as schemaOrderDetails,
                       review as schemaReview)
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Customer'],
    prefix="/customer"
)


@router.get("/pizza", response_model=list[schemaPizza.Pizza])
def read_all_pizzas(db: Session = Depends(get_db)):
    return controller.get_all_pizzas(db)

@router.get("/pizza_by_category", response_model=list[schemaPizza.Pizza])
def read_all_pizzas_by_category(
    category: str,
    db: Session = Depends(get_db)
):
    return controller.get_category(db, category)

@router.post("/order_create", response_model=schemaOrders.Order)
def create_order(request: schemaOrders.OrderCreateRequest, db: Session = Depends(get_db)):
    return controller.create_order(db=db , request=request)

@router.put("/order/{order_id}", response_model=schemaOrders.Order)
def update_order(item_id: int, request: schemaOrders.OrderUpdateCust, db: Session = Depends(get_db)):
    return controller.update_order(db=db, request=request, item_id=item_id)

@router.delete("/order/{order_id}")
def delete_order(item_id: int, db: Session = Depends(get_db)):
    return controller.delete_order(db=db, item_id=item_id)

@router.get("/order/{order_id}/status", response_model=schemaOrders.OrderStatus)
def get_order_status(order_id: int, db: Session = Depends(get_db)):
    return controller.get_order_status(db=db, order_id=order_id)

@router.post("/order_detail_create", response_model=schemaOrderDetails.OrderDetail)
def create_order_details(request: schemaOrderDetails.OrderDetailBase, db: Session = Depends(get_db)):
    return controller.create_order_details(db=db , request=request)

@router.put("/order_detail/{order_detail_id}", response_model=schemaOrderDetails.OrderDetail)
def update_order_details(item_id: int, request: schemaOrderDetails.OrderDetailUpdate, db: Session = Depends(get_db)):
    return controller.update_order_details(db=db, request=request, item_id=item_id)

@router.delete("/order_detail/{order_detail_id}")
def delete_order_details(item_id: int, db: Session = Depends(get_db)):
    return controller.delete_order_details(db=db, item_id=item_id)

@router.post("/customer_create", response_model=schemaCustomer.Customer)
def create_customer(request: schemaCustomer.CustomerBase, db: Session = Depends(get_db)):
    return controller.create_customer(db=db , request=request)

@router.post("/payment_create", response_model=schemaPayment.Payment)
def create_payment(request: schemaPayment.PaymentCreate, db: Session = Depends(get_db)):
    return controller.create_payment(db=db , request=request)

@router.put("/payment_update", response_model=schemaPayment.Payment)
def update_payment(payment_id: int, request: schemaPayment.PaymentUpdate, db: Session = Depends(get_db)):
    return controller.update_payment(db=db , payment_id = payment_id, request=request)

@router.delete("/payment/{payment_id}")
def delete_payment(item_id: int, db: Session = Depends(get_db)):
    return controller.delete_payment(db=db, item_id=item_id)

@router.put("/pay_for_order", response_model=schemaOrders.Order)
def pay_for_order(request: schemaOrders.PayForOrder, db: Session = Depends(get_db)):
    return controller.pay_for_order(db=db, order_id=request.order_id, payment_id=request.payment_id)

@router.post("/review_create", response_model=schemaReview.Review)
def create_review(request: schemaReview.ReviewCreate, db: Session = Depends(get_db)):
    return controller.create_review(db=db, request=request)

@router.delete("/review_delete/{review_id}")
def delete_review(review_id: int, db: Session = Depends(get_db)):
    return controller.delete_review(db=db, review_id = review_id)

@router.put("/review_update", response_model=schemaReview.Review)
def update_review(review_id: int, request: schemaReview.ReviewUpdate, db: Session = Depends(get_db)):
    return controller.update_review(db=db, review_id=review_id, request=request)

@router.put("/add_promo_to_order", response_model=schemaOrders.Order)
def add_promo_to_order(request: schemaOrders.AddPromoToOrder, db: Session = Depends(get_db)):
    return controller.add_promo_to_order(db=db, order_id=request.order_id, promo_code=request.promo_code)