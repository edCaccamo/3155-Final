from . import orders, order_details, customers, resources, sandwiches, recipies


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(customers.router)
    app.include_router(resources.router)
    app.include_router(sandwiches.router)
    app.include_router(recipies.router)