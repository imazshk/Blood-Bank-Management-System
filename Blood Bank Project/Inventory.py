from database import *

class Inventory:

    @staticmethod
    def add_blood(blood_type, quantity=1):
        query = f'SELECT quantity FROM inventory WHERE blood_type = "{blood_type}";'
        result = db_query(query)
        if result:
            current_quantity = result[0][0]
            updated_quantity = current_quantity + quantity
            query = f'UPDATE inventory SET quantity = {updated_quantity} WHERE blood_type = "{blood_type}";'
        else:
            query = f'INSERT INTO inventory (blood_type, quantity) VALUES ("{blood_type}", {quantity});'
        db_query(query)
        mydb.commit()

    @staticmethod
    def deduct_blood(blood_type, quantity=1):
        query = f'SELECT quantity FROM inventory WHERE blood_type = "{blood_type}";'
        result = db_query(query)
        if result:
            current_quantity = result[0][0]
            if current_quantity < quantity:
                print(f"Sorry, not enough {blood_type} blood available.")
            else:
                updated_quantity = current_quantity - quantity
                query = f'UPDATE inventory SET quantity = {updated_quantity} WHERE blood_type = "{blood_type}";'
                db_query(query)
                mydb.commit()
        else:
            print(f"No inventory found for blood type {blood_type}.")