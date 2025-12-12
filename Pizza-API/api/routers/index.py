from . import staff, customer, system


def load_routes(app):
    app.include_router(system.router)
    app.include_router(staff.router)
    app.include_router(customer.router)
