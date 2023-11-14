import pyodbc
import json
import re
from all_items_shop import *

# Set up the connection parameters
server = 'LAPTOP-SR\CBDB'
database = 'test'
username = 'sa'
password = '12345'
driver = 'ODBC Driver 17 for SQL Server'

# Establish a connection to the database
connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
connection = pyodbc.connect(connection_string)

# Create a cursor
cursor = connection.cursor()

print(all_items_shop(cursor))

query = """
DECLARE @target_shop_id INT = 1; -- Replace with the desired shop_id

SELECT
    item_id
FROM
    Shop_Inventory
WHERE
    shop_id = @target_shop_id;


"""
cursor.execute(query)

# Fetch the results
item_ids = [row.item_id for row in cursor.fetchall()]
for item_id in item_ids:
    item_name_query = f"""
        SELECT name
        FROM Items
        WHERE item_id = {item_id};
    """
    cursor.execute(item_name_query)
    item_name = cursor.fetchone().name
    
    item_materials_query = f"""
        SELECT
            STRING_AGG(M.name + ' (' + CAST(IM.percentage AS NVARCHAR(10)) + '%' + ' - ' + LM.rarity + ')', ', ') AS material_info
        FROM
            Item_Materials IM
        LEFT JOIN
            Materials M ON IM.material_id = M.material_id
        LEFT JOIN
            Location_Materials LM ON LM.location_id = location_id AND LM.material_id = IM.material_id
        WHERE
            IM.item_id = {item_id}
        GROUP BY
            IM.item_id;
    """
    cursor.execute(item_materials_query)
    result = cursor.fetchone()

    base_cost_query = f"SELECT CAST(base_cost AS FLOAT) AS base_cost FROM Items WHERE item_id = {item_id}"
    cursor.execute(base_cost_query)

    base_cost = cursor.fetchone().base_cost
    # Access the material_info directly
    material_info = result.material_info
    pattern = r'(\d+\.\d+)% - (\w+)'
    matches = re.findall(pattern, material_info)
    total_value = 0.0
    for percentage, rarity in matches:
        percentage = float(percentage)
        if rarity == 'Very_Rare':
            total_value += percentage * 1.5 * base_cost
        elif rarity == 'Rare':
            total_value += percentage * 1.2 * base_cost
        elif rarity == 'Average':
            total_value += percentage * 1.0 * base_cost
        elif rarity == 'Abundant':
            total_value += percentage * 0.8 * base_cost
    # Process or print the material_info for the current item
    print(f"Item Name: {item_name}, Material Info: {material_info}, base cost: {base_cost}, final shop cost: {total_value}")



# Close the cursor and connection
cursor.close()
connection.close()
