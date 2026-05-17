def find_product(menu, product_name):
    """
    Search for a product inside the menu and return its name and price.
    Case-insensitive.
    """
    for category in menu.values():
        for name, price in category.items():
            if name.lower() == product_name.lower():
                return name, price
    return None


def calculate_item_total(price, quantity):
    """
    Calculate total price for a given item.
    """
    return price * quantity