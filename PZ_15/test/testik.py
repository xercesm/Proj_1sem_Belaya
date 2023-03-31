import sqlite3 as sq

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS products (
        id_prod INTEGER PRIMARY KEY  ,
        name VARCHAR NEXN NOT NULL ,
        descript VARCHAR NOT NULL ,
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
        id_prod INTEGER NOT NULL,
        FOREIGN KEY (id_pro)  REFERENCES products (id_prod)
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS sructure (
        id_sructure INTEGER PRIMARY KEY ,
        id_requestt INTEGER ,
        id_pr INTEGER ,
        nmbr INTEGER NEXN NOT NULL ,
        FOREIGN KEY (id_requestt) REFERENCES requests (id_requests)
        FOREIGN KEY (id_pr) REFERENCES products (id_products)
    )""")