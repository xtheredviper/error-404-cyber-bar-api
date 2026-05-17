from api.database.models import (
    OrderModel,
    OrderItemModel
)

from orders import find_product, calculate_item_total
from menu import menu


def create_new_order(order, db):

    new_order = OrderModel(
        status="preparing"
    )

    db.add(new_order)

    db.commit()

    db.refresh(new_order)

    total_order_price = 0

    for item in order.items:

        result = find_product(menu, item.product)

        if not result:
            return {
                "error": f"Product '{item.product}' not found"
            }

        name, price = result

        item_total = calculate_item_total(
            price,
            item.quantity
        )

        total_order_price += item_total

        new_item = OrderItemModel(
            product=name,
            quantity=item.quantity,
            total=item_total,
            order_id=new_order.id
        )

        db.add(new_item)

    db.commit()

    db.refresh(new_order)

    return {
        "order_id": new_order.id,
        "status": new_order.status,
        "total_order_price": total_order_price,
        "items": new_order.items
    }


def get_all_orders(db):

    orders = db.query(OrderModel).all()

    response = []

    for order in orders:

        total = sum(item.total for item in order.items)

        response.append({
            "order_id": order.id,
            "status": order.status,
            "total": total,
            "items": order.items
        })

    return response


def update_status(order_id, updated_status, db):

    order = db.query(OrderModel).filter(
        OrderModel.id == order_id
    ).first()

    if not order:
        return {"error": "Order not found"}

    order.status = updated_status.status

    db.commit()

    db.refresh(order)

    return {
        "message": "Order status updated successfully",
        "order": order
    }