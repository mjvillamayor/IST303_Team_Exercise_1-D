#Tests file all the required functionality and edge cases, ensuring that the InventorySystem class behaves as expected.

import pytest 
from problem4_code import InventorySystem

@pytest.fixture #to creaate a fresh inventory object for each test 
def inventory():
    return InventorySystem()
# This fixture creates a new InventorySystem instance for each test
# When a test function has a parameter named 'inventory', pytest automatically calls this fixture
# and passes the result to the test function

#Test 1, Tests adding products to the inventory
def test_add_product(inventory): 
    inventory.add_product("A001", "Laptop", 5, 1200.00)     # Calls the add_product method to add a laptop to the inventory
    assert inventory.search_products("Laptop") == [{"id": "A001", "name": "Laptop", "quantity": 5, "price": 1200.00}]
    #assert statement for assertions 

    #for second product testing 
    inventory.add_product("A002", "Mouse", 20, 25.50)
    assert len(inventory.search_products("")) == 2 # Verifies that searching with an empty string returns both products (2 items)


#Test 2, Tests updating existing products
def test_update_existing_product(inventory):
    # Add initial product
    inventory.add_product("A001", "Laptop", 5, 1200.00)
    
    # Update the product
    inventory.add_product("A001", "Laptop Pro", 10, 1500.00)
    
    # Verify the product was updated
    product = inventory.search_products("Laptop Pro")[0]
    assert product["name"] == "Laptop Pro"
    assert product["quantity"] == 10
    assert product["price"] == 1500.00
    
    # Verify only one product exists with that ID, updated and not duplicated 
    assert len(inventory.search_products("")) == 1

#Test 3, Tests removing products and verifies the return value
def test_remove_product(inventory):
    # Add products
    inventory.add_product("A001", "Laptop", 5, 1200.00)
    inventory.add_product("A002", "Mouse", 20, 25.50)
    
    # Remove a product that exists, boolean true
    result = inventory.remove_product("A001")
    assert result is True #verifies true when successful 
    assert len(inventory.search_products("")) == 1 #Confirms that only one product remains in the inventory
    
    # Try to remove a product that doesn't exist, boolean false
    result = inventory.remove_product("A003")
    assert result is False 

#Test 4, Tests calculating the total inventory value
def test_get_inventory_value(inventory):
    # Empty inventory = zero value, empty list
    assert inventory.get_inventory_value() == 0
    
    # Add products
    inventory.add_product("A001", "Laptop", 5, 1200.00)
    inventory.add_product("A002", "Mouse", 20, 25.50)
    
    # Calculate expected value: (5 * 1200.00) + (20 * 25.50) = 6000 + 510 = 6510
    expected_value = 6000 + 510
    assert inventory.get_inventory_value() == expected_value #verify calculated correctly 

#Test 5, Tests searching for products by keyword
def test_search_products(inventory):
    # Add products
    inventory.add_product("A001", "Laptop", 5, 1200.00)
    inventory.add_product("A002", "Mouse", 20, 25.50)
    inventory.add_product("A003", "Keyboard", 15, 50.00)
    inventory.add_product("A004", "Monitor", 8, 300.00)
    
    # Search for products containing "mo"
    results = inventory.search_products("mo")
    assert len(results) == 2 #checking for two products matching the search term
    
    # Verify the results contain the expected products
    product_names = [product["name"] for product in results]  # Creates a list of just the product names from the search results

    assert "Mouse" in product_names
    assert "Monitor" in product_names
    
    # Search for a non-existent product
    results = inventory.search_products("tablet")
    assert len(results) == 0 #verify no products match search term.
    
    # Empty string should return all products
    results = inventory.search_products("")
    assert len(results) == 4 #verifies all products have been returned 

#Test 6, Tests that negative quantity or price raises an exception
def test_negative_values(inventory):
    # Test negative quantity
    with pytest.raises(Exception): #exception testing 
        inventory.add_product("A001", "Laptop", -5, 1200.00)
        
    # Test negative price
    with pytest.raises(Exception): #exception testing 
        inventory.add_product("A002", "Mouse", 20, -25.50)
        
    # Test both negative
    with pytest.raises(Exception): #exception testing 
        inventory.add_product("A003", "Keyboard", -15, -50.00)

#Test 7, Tests the specific example given in the problem statement
def test_example_from_problem(inventory):
    inventory.add_product("A001", "Laptop", 5, 1200.00)
    inventory.add_product("A002", "Mouse", 20, 25.50)
    
    # Test inventory value
    assert inventory.get_inventory_value() == 6110.00
    
    # Test search
    expected_result = [{"id": "A002", "name": "Mouse", "quantity": 20, "price": 25.50}]
    assert inventory.search_products("mo") == expected_result
    #verifies searching for "mo" returns the expected result for the specified mouse product

