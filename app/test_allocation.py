from app.warehouse import Warehouse
from app.product_catalog import product_catalog

def test_allocation_scenario(name, product_id, quantity, expected_found, expected_cell=None):
    print(f"{name}")
    warehouse = Warehouse()
    product = product_catalog[product_id]
    result = warehouse.allocate_cell(product,quantity)
    