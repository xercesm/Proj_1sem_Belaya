import sqlite3 as sq
import data_products
import data_shops
import data_requests
import data_nmbr_pr
import data_sclad
import data_sostav

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS products (
        id_prod INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR NEXN NOT NULL,
        descript VARCHAR NOT NULL,
        unit VARCHAR NOT NULL
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS shops (
        id_shops INTEGER PRIMARY KEY  ,
        name VARCHAR NEXN NOT NULL ,
        adress VARCHAR NOT NULL ,
        phone_number VARCHAR INTEGER 
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS requests (
        id_requests INTEGER PRIMARY KEY  ,
        id_shop INTEGER NOT NULL ,
        data DATE NEXN NOT NULL ,
        FOREIGN KEY (id_shop) REFERENCES shops (id_shops)
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS nmbr_pr (
        id_nmbr_pr INTEGER PRIMARY KEY ,
        id_pro INTEGER NOT NULL ,
        nmbr INTEGER NEXN NOT NULL ,
        FOREIGN KEY (id_pro)  REFERENCES products (id_prod)
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS sclad(
        id_sclada INTEGER PRIMARY KEY AUTOINCREMENT,
        id_shopa INTEGER NOT NULL,
        id_production INTEGER NOT NULL,
        kolvo_na_sclade INTEGER,
        FOREIGN KEY (id_shopa) REFERENCES shops(id_shops),
        FOREIGN KEY (id_production) REFERENCES products(id_prod)
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS sostav(
        id_sostav INTEGER PRIMARY KEY AUTOINCREMENT,
        id_rec INTEGER,
        id_produ INTEGER,
        kolichestvo INTEGER,
        FOREIGN KEY (id_produ) REFERENCES products (id_prod),
        FOREIGN KEY (id_rec) REFERENCES requests (id_requests)
    )""")





with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.executemany('INSERT INTO products VALUES (?, ?, ?, ?)', data_products.info_products)
    
with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.executemany('INSERT INTO shops VALUES (?, ?, ?, ?)', data_shops.info_shops)

with sq.connect('saper.db') as con:
     cur = con.cursor()
     cur.executemany('INSERT INTO requests VALUES (?, ?, ?)', data_requests.info_requests)
     
with sq.connect('saper.db') as con:
     cur = con.cursor()
     cur.executemany('INSERT INTO nmbr_pr VALUES (?, ?, ?)', data_nmbr_pr.info_nmbr_pr)

with sq.connect('saper.db') as con:
    cur = con.cursor()
    con.executemany("INSERT INTO sclad VALUES (?,?,?,?)", data_sclad.info_sclad)
    con.commit()

with sq.connect('saper.db') as con:
    cur = con.cursor()
    con.executemany("INSERT INTO sostav VALUES (?,?,?,?)", data_sostav.info_sostav)
    con.commit()
 




with sq.connect('saper.db') as con:
    cur = con.cursor()
    print('1. Вывести список всех товаров и их описания:')
    cur.execute("SELECT name, descript FROM products")
    res1 = cur.fetchall()
    print(res1)
    print('2. Вывести список всех магазинов и их адресов:')
    cur.execute("SELECT name, adress FROM shops")
    res2 = cur.fetchall()
    print(res2)
    print('3. Вывести список всех заявок магазинов и даты, на которые они были поданы:')
    cur.execute("SELECT id_requests, data FROM requests")
    res3 = cur.fetchall()
    print(res3)
    print('4. Вывести список товаров и количество их наличия на складе:')
    cur.execute("SELECT id_pro, nmbr FROM nmbr_pr")
    res4 = cur.fetchall()
    print(res4)
    print('5. Вывести список товаров и количество их наличия на складе в порядке убывания количества:')
    cur.execute("SELECT id_pro, nmbr FROM nmbr_pr ORDER BY nmbr DESC")
    res5 = cur.fetchall()
    print(res5)
    print('6. Вывести список всех заявок магазинов и товаров, которые были в них заказаны:')
    cur.execute("SELECT id_rec, id_produ FROM sostav") 
    res6 = cur.fetchall()
    print(res6)
    print('7. Вывести список всех товаров, у которых на складе количество меньше минимально допустимого(15):')
    cur.execute("SELECT id_pro, nmbr FROM nmbr_pr WHERE nmbr < 15")
    res7 = cur.fetchall()
    print(res7)
    print('8. Вывести список всех заявок магазинов, которые были сделаны в определенный период времени(2023.02.20-2023.03.29):')
    cur.execute("SELECT id_requests FROM requests WHERE data BETWEEN '2023-02-20' AND '2023-03-29'")
    res8 = cur.fetchall()
    print(res8)
    print('9. Вывести список всех магазинов, у которых суммарное количество товаров на складе меньше заданного значения(1000):')
    cur.execute("SELECT id_shopa FROM sclad WHERE kolvo_na_sclade < 1000")
    res9 = cur.fetchall()
    print(res9)


with sq.connect('saper.db') as con:
    cur = con.cursor()
    #1. Обновить количество товара на складе для конкретного товара
    cur.execute("UPDATE sclad SET kolvo_na_sclade = 12345 WHERE kolvo_na_sclade = 123")
    #2. Обновить название товара в заявке
    #3. Обновить количество товара в заявке
    # Задания 2 и 3 преподаватель разрешил не делать
    #4. Обновить адрес магазина, который подал заявку
    cur.execute("UPDATE shops SET adress='пл. Чехова, 47' WHERE id_shops=(SELECT id_shop FROM requests WHERE id_requests=31)")
    #5. Обновить дату заявки для конкретного магазина
    cur.execute("UPDATE requests SET data='2023.02.05' WHERE id_shop = 22")
    #6. Обновить количество товара на складе для нескольких товаров
    cur.execute("UPDATE sclad SET kolvo_na_sclade=656565 WHERE (id_production = 1) or (id_production = 5)")
    #7. Обновить описание товара и количество на складе для конкретного товара
    cur.execute("UPDATE products SET descript='мучное' WHERE id_prod = 5")
    cur.execute("UPDATE sclad SET kolvo_na_sclade=950 WHERE id_production = 5")
    #8. Обновление количества товаров на складе, учитывая выполненную заявку магазина
    cur.execute("UPDATE sclad SET kolvo_na_sclade=((SELECT kolvo_na_sclade FROM sclad WHERE id_production=(SELECT id_produ FROM sostav WHERE id_rec=31)) - (SELECT SUM(kolichestvo) FROM sostav WHERE id_produ=(SELECT id_produ FROM sostav WHERE id_rec=31))) WHERE id_production=(SELECT id_produ FROM sostav WHERE id_rec=31)")    
    #9. Обновление количества товаров на складе, учитывая выполненную заявку магазина с учетом конкретного товара
    cur.execute("UPDATE sclad SET kolvo_na_sclade=((SELECT kolvo_na_sclade FROM sclad WHERE id_production=1) - (SELECT SUM(kolichestvo) FROM sostav WHERE id_produ=1)) WHERE id_production=1")
    #10. Обновить название магазина, который подал заявку, и адрес магазина для конкретной заявки
    cur.execute("UPDATE shops SET name='Крупинка', adress='пр. Бубновый, д.33' WHERE id_shops=(SELECT id_shop FROM requests WHERE id_requests = 37)")
    #11. Обновить название магазина в заявке, которую подал конкретный магазин
    # Отказ от задания 11
    #12. Обновить адрес магазина и количество товара в заявке для конкретного товара
    cur.execute("UPDATE shops SET adress='пр. Петропаловский, 16' WHERE id_shops= (SELECT id_shop FROM requests WHERE id_requests=(SELECT id_rec FROM sostav WHERE id_produ=6))")
    cur.execute("UPDATE sostav SET kolichestvo=896 WHERE id_produ=10")
    #13. Обновить описание товара и количество на складе для нескольких товаров
    cur.execute("UPDATE products SET descript='Дерево' WHERE (id_prod = 2) or (id_prod=3)")
    cur.execute("UPDATE sclad SET kolvo_na_sclade=99999 WHERE (id_production = 2) or (id_production=3)")


# SQL-запросы на удаление данных из БД:
with sq.connect('saper.db') as con:
    cur = con.cursor()
    # 1. Удаление заявки магазина и соответствующих записей в таблице состава
    cur.execute("DELETE FROM requests WHERE id_requests=31")
    cur.execute("DELETE FROM sostav WHERE id_rec=31")
    # 2. Удалить из таблицы "Количество товаров на складе" записи, соответствующие товарам, не имеющим заявок в таблице "Состав"
    cur.execute("DELETE FROM sclad WHERE id_production NOT IN (SELECT id_produ FROM sostav)")
    # 3. Удалить из таблицы "Заявки магазинов" все заявки магазинов, адрес которых начинается на "ул. Ленина"
    cur.execute("DELETE FROM requests WHERE id_shop IN (SELECT id_shops FROM shops WHERE adress LIKE 'ул. Ленина%')")
    # 4. Удалить из таблицы "Состав" записи, соответствующие товарам, которых нет на складе (количество = 0)
    cur.execute("DELETE FROM sostav WHERE id_produ IN (SELECT id_production FROM sclad WHERE kolvo_na_sclade=0)")
    # 5. Удалить из таблицы "Магазины" магазины, в которых не было заявок в течение последнего месяца
    cur.execute("DELETE FROM shops WHERE id_shops NOT IN (SELECT id_shop FROM requests WHERE data BETWEEN '2023.02.05' AND '2023.04.07')")
    # 6. Удалить из таблицы "Товары" товары, которые не были заказаны ни разу
    cur.execute("DELETE FROM products WHERE id_prod NOT IN (SELECT id_produ FROM sostav)")
    # 7. Удалить из таблицы "Количество товаров на складе" записи, соответствующие товарам, которые не были заказаны ни разу
    cur.execute("DELETE FROM sclad WHERE id_production NOT IN (SELECT id_produ FROM sostav)")
    # 8. Удалить из таблицы "Состав" записи, соответствующие заявкам, которые были поданы более месяца назад
    cur.execute("DELETE FROM sostav WHERE id_rec IN (SELECT id_requests FROM requests WHERE data BETWEEN '2023-01-01' AND '2023-03-31')")