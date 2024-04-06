#Вариант 13. Приложение ТОВАРНЫЙ ЗАПАС для автоматизированного
#учёта товарных запасов на складе. БД должна содержать
#таблицу Товары со следующей структурой записи: Код
#товара, Торговая марка, Тип, Цена, Количество на складе,
#Минимальный запас
import sqlite3 as sq
from info_zapas import info_items
with sq.connect('zapas.db') as con:
    cur=con.cursor()
    cur.execute("DROP TABLE IF EXISTS items")
    cur.execute("CREATE TABLE IF NOT EXISTS items("
                "item_id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "brand TEXT NOT NULL,"
                "item_type TEXT NOT NULL,"
                "price INTEGER NOT NULL,"
                "quantity INTEGER NOT NULL,"
                "min_zapas INTEGER NOT NULL)")
with sq.connect('zapas.db') as con:
    cur=con.cursor()
    cur.executemany("INSERT INTO items VALUES(?,?,?,?,?,?)", info_items)
with sq.connect('zapas.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM items WHERE price>1000 AND quantity<1000")
    result_1=cur.fetchall()
    print(result_1)
with sq.connect('zapas.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM items WHERE brand LIKE 'N%'")
    result_2 = cur.fetchall()
    print(result_2)
with sq.connect('zapas.db') as con:
    cur = con.cursor()
    cur.execute("SELECT brand,price FROM items WHERE price<quantity")
    result_3 = cur.fetchall()
    print(result_3)
with sq.connect('zapas.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE items SET price=price+25 WHERE price<1000")
    cur.execute("SELECT * FROM items")
    result_4=cur.fetchall()
    print(f"\n{result_4}")
with sq.connect('zapas.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE items SET brand='Квас для вас' WHERE item_id=1")
    cur.execute("SELECT * FROM items WHERE item_id=1")
    result_5=cur.fetchall()
    print(result_5)
with sq.connect('zapas.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE items SET item_type='лягушка' WHERE price<1000 AND (min_zapas<1000 OR quantity>600)")
    cur.execute("SELECT * FROM items WHERE item_type='лягушка'")
    result_6=cur.fetchall()
    print(result_6)
with sq.connect('zapas.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM items WHERE item_id%2==0")
    cur.execute("SELECT * FROM items")
    result_7=cur.fetchall()
    print(f"\n{result_7}")
with sq.connect('zapas.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM items WHERE item_type LIKE 'т%'")
    cur.execute("SELECT * FROM items")
    result_8=cur.fetchall()
    print(result_8)
with sq.connect('zapas.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM items WHERE price>1000")
    cur.execute("SELECT * FROM items")
    result_9=cur.fetchall()
    print(result_9)

