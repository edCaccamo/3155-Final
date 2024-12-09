from . import orders, order_details, reviews, promotions, payment_info


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(reviews.router)
    app.include_router(promotions.router)
    app.include_router(payment_info.router)