from app.warehouse import Warehouse
from app.product_catalog import product_catalog

def test_allocation_scenario(name, product_id, quantity, expected_found, expected_cell=None):
    print(f"{name}")
    warehouse = Warehouse()
    product = product_catalog[product_id]
    result = warehouse.allocate_cell(product,quantity)
    print("Input:", product_id, quantity)
    print("Result", result)
    if expected_found:
        assert result["foundCell"] is True
        assert result["cell"] == expected_cell
        print("Passed")
    else:
        assert result["foundCell"] is False
        print("Passed")

if __name__== "__main__":

    #Scenario 1 
    test_allocation_scenario("scenario 1.1","bread", 2, True, "0,0")
    test_allocation_scenario("Scenatrio 1.2","bamba", 6, True, "0,0")

    #Scenatio 2
    test_allocation_scenario("Scenario 2", "yogourt", 6, True, "7,0")

    #Scenario 3
    test_allocation_scenario("Scenario 3", "apple",11, False)

    #Scenario 4
    test_allocation_scenario("Scenario 4", "stain removal", 7, True, "0,9")

    #Scenatio 5
    test_allocation_scenario("Scenario 5", "insulin", 10, True, "7,6")
