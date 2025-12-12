from datetime import date
from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from datetime import datetime
from ..controllers import staff as controller
from ..schemas import (pizza as schemaPizza,
                       orders as schemaOrders,
                       customer as schemaCustomer,
                       promo as schemaPromo,
                       ingredient as schemaIngredient,
                       ingredient_usage as schemaIngredientUsage,
                       review as schemaReview,
                       order_details as schemaOrderDetails,)
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Staff'],
    prefix="/staff"
)


@router.post("/pizza_create", response_model=schemaPizza.Pizza)
def create_pizza(request: schemaPizza.PizzaBase, db: Session = Depends(get_db)):
    return controller.create_pizza(db=db , request=request)

@router.post("/ingredient_create", response_model=schemaIngredient.Ingredient)
def create_ingredient(request: schemaIngredient.IngredientBase, db: Session = Depends(get_db)):
    return controller.create_ingredient(db=db , request=request)

@router.put("/ingredient/{item_id}", response_model=schemaIngredient.Ingredient)
def update_ingredient(ingredient_id: int, request: schemaIngredient.IngredientUpdate, db: Session = Depends(get_db)):
    return controller.update_ingredient(db=db, request=request, ingredient_id=ingredient_id)

@router.put("/pizza/{pizza_id}", response_model=schemaPizza.Pizza)
def update_pizza(item_id: int, request: schemaPizza.PizzaUpdate, db: Session = Depends(get_db)):
    return controller.update_pizza(db=db, request=request, item_id=item_id)


@router.delete("/pizza/{pizza_id}")
def delete_pizza(item_id: int, db: Session = Depends(get_db)):
    return controller.delete_pizza(db=db, item_id=item_id)

@router.post("/promo_create", response_model=schemaPromo.Promo)
def create_promo(request: schemaPromo.PromoBase, db: Session = Depends(get_db)):
    return controller.create_promo(db=db , request=request)

@router.put("/promos/{item_id}", response_model=schemaPromo.Promo)
def update_promo(item_id: int, request: schemaPromo.PromoUpdate, db: Session = Depends(get_db)):
    return controller.update_promo(db=db, request=request, item_id=item_id)

@router.put("/order/{order_id}/status", response_model=schemaOrders.Order)
def update_order_status(order_id: int, request: schemaOrders.OrderUpdateStaff , db: Session = Depends(get_db)):
    return controller.update_order_status(db=db, order_id=order_id, request=request)

@router.post("/ingredient_usage_create", response_model=schemaIngredientUsage.IngredientUsage)
def create_ingredient_usage(request: schemaIngredientUsage.IngredientUsageBase, db: Session = Depends(get_db)):
    return controller.create_ingredient_usage(db=db , request=request)

@router.put("/ingredient_usage/{ingredient_usage_id}", response_model=schemaIngredientUsage.IngredientUsage)
def update_ingredient_usage(item_id: int, request: schemaIngredientUsage.IngredientUsageUpdate, db: Session = Depends(get_db)):
    return controller.update_ingredient_usage(db=db, request=request, item_id=item_id)


@router.delete("/ingredient_usage/{ingredient_usage_id}")
def delete_ingredient_usage(item_id: int, db: Session = Depends(get_db)):
    return controller.delete_ingredient_usage(db=db, item_id=item_id)

@router.get("/order", response_model=list[schemaOrders.Order])
def read_all_orders(db: Session = Depends(get_db)):
    return controller.get_all_orders(db)

@router.get("/order_by_status", response_model=list[schemaOrders.Order])
def read_all_orders_by_status(category: str, db: Session = Depends(get_db)):
    return controller.get_orders_of_status(db, category)

@router.get("/order_by_timeframe", response_model=list[schemaOrders.Order])
def read_orders_by_timeframe(start_date: datetime, end_date: datetime, db: Session = Depends(get_db)):
    return controller.get_orders_by_timeframe(db, start_date, end_date)

@router.get("/get_details_of_order", response_model=list[schemaOrderDetails.OrderDetail])
def get_details_of_order(
    order_id: int,
    db: Session = Depends(get_db)
):
    return controller.get_details_of_order(db, order_id)

@router.get("/reviews/{customer_id}", response_model=list[schemaReview.Review])
def read_reviews_by_customer(customer_id: int, db: Session = Depends(get_db)):
    return controller.get_reviews_by_customer(customer_id,db)

@router.get("/revenue/{target_date}")
def read_revenue_by_date(
    target_date: date,
    db: Session = Depends(get_db)
):
    return {"date": target_date, "total_revenue": controller.get_revenue_by_date(db, target_date)}


# @router.post("/", response_model=schema.Order)
# def create(request: schema.OrderCreate, db: Session = Depends(get_db)):
#     return controller.create(db=db, request=request)
#
#
# @router.get("/", response_model=list[schema.Order])
# def read_all(db: Session = Depends(get_db)):
#     return controller.read_all(db)
#
#
# @router.get("/{item_id}", response_model=schema.Order)
# def read_one(item_id: int, db: Session = Depends(get_db)):
#     return controller.read_one(db, item_id=item_id)
#

