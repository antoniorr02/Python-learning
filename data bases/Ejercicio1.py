import sqlite3

conexion = sqlite3.connect("productos.db")

cursor = conexion.cursor()
cursor.execute("CREATE TABLE PRODUCTOS (id INTEGRER, nombre TEXT, precio INTEGRER)")
conexion.commit()

lista_productos = [(1,'Impresora',300), (2,'Raton',20), (3,'Ordenador',600)]
cursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", lista_productos)
conexion.commit()

cursor.execute("SELECT * FROM PRODUCTOS")
elementos = cursor.fetchall()
for i in elementos:
    print(i)

conexion.close()
