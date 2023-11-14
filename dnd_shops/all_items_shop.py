# all_items_shop.py

def all_items_shop(cursor):
    # Execute the SQL query to get all shop names
    shop_names_query = "SELECT name FROM Shops"
    cursor.execute(shop_names_query)

    # Fetch all results
    shop_names = [row.name for row in cursor.fetchall()]

    return shop_names
