
import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("product")
        self.cursor = self.connection.cursor()
        self.create_product()

    def create_product(self):
        self.cursor.execute("""
            create table if not exists product(
            id integer primary key,
            title varchar(100),
            description varchar(150),
            price float ,
            photo varchar 
            )     
        """)


    def add_product(self,title, description, price,photo):
        self.cursor.execute("""
            insert into product (title,description, price, photo)
            values (?,?,?,?)
        """, (title,  description, price,photo))
        self.connection.commit()

    def all_product(self):
        self.cursor.execute(f"""
            SELECT * from product
        """)
        return self.cursor.fetchall()

    def delete_product(self, id):
        self.cursor.execute("""
            delete from product where id=?
        """, (id,))
        self.connection.commit()

    def get_product(self, id):
        self.cursor.execute("""
              select * from product where id=?
          """, (id,))
        return self.cursor.fetchone()

    def update_product_title(self, id, title):
        self.cursor.execute("""
              update product set title=? where id=?
          """, (title, id))
        self.connection.commit()

    def update_product_description(self, id, description):
        self.cursor.execute("""
              update product set description=? where id=?
          """, (description, id))
        self.connection.commit()

    def update_product_price(self, id, price):
        self.cursor.execute("""
              update product set price=? where id=?
          """, (price, id))
        self.connection.commit()

    def update_product_photo(self, id, photo):
        self.cursor.execute("""
              update product set photo=? where id=?
          """, (photo, id))
        self.connection.commit()







