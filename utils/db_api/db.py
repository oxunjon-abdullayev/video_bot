import sqlite3


class Category:
    def __init__(self):
        self.connection = sqlite3.connect("category")
        self.cursor = self.connection.cursor()
        self.create_category()

    def create_category(self):
        self.cursor.execute("""
            create table if not exists category(
            category_id integer primary key ,
            title varchar(100)
            )                       
        """)

    def add_category(self, title):
        self.cursor.execute("""
            insert into category (title)
            values (?)
        """, (title,))
        self.connection.commit()

    def all_category(self):
        self.cursor.execute(f"""
            SELECT * from category
        """)
        return self.cursor.fetchall()

    def delete_category(self, category_id):
        db = Database()
        db.delete_products_by_category(category_id)

        self.cursor.execute("""
            DELETE FROM category WHERE category_id=?
        """, (category_id,))
        self.connection.commit()

    def delete_category(self, category_id):
        self.cursor.execute("""
            DELETE FROM category WHERE category_id=?
        """, (category_id,))
        self.connection.commit()

    def get_category(self, category_id):
        self.cursor.execute("""
              select * from category where category_id=?
          """, (category_id,))
        return self.cursor.fetchone()


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("product")
        self.cursor = self.connection.cursor()
        self.create_product()

    def create_product(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS product(
            id INTEGER PRIMARY KEY,
            title VARCHAR(100),
            description VARCHAR(150),
            video VARCHAR,
            category_id INTEGER,
             FOREIGN KEY (category_id) REFERENCES category(category_id) ON DELETE CASCADE
            )     
        """)

    def add_product(self, title, description, video, category_id):
        self.cursor.execute("""
            insert into product (title,description,  video, category_id)
            values (?,?,?,?)
        """, (title, description, video, category_id))
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

    def delete_products_by_category(self, category_id):
        self.cursor.execute("""
            DELETE FROM product WHERE category_id=?
        """, (category_id,))
        self.connection.commit()

    def get_category_id_videos(self, category_id):
        self.cursor.execute("""
             select * from product where category_id = ?
        """, (category_id,))
        return self.cursor.fetchall()

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

    def update_product_video(self, id, video):
        self.cursor.execute("""
              update product set video=? where id=?
          """, (video, id))
        self.connection.commit()

    def update_product_category_id(self, id, category_id):
        self.cursor.execute("""
              update product set category_id=? where id=?
          """, (category_id, id))
        self.connection.commit()
