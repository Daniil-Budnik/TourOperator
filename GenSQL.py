import os
import sqlite3 as SQL


# Создаем или открываем базу данных
DataBase = SQL.connect("MyDataBase.db")
SQLite = DataBase.cursor()

# Информация, для записи в базу данных
MyClietn = [
     [1,"Фам1","Имя1","Очт1","Адрес1",80000001],
     [2,"Фам2","Имя2","Очт2","Адрес2",80000002],
     [3,"Фам3","Имя3","Очт3","Адрес3",80000003]
     ]
 
MyRoute = [
     [1,"Рег1","Климат1","Длительность1","Отель1",100001],
     [2,"Рег2","Климат2","Длительность2","Отель2",100002],
     [3,"Рег3","Климат3","Длительность3","Отель3",100003]
     ]
 
MyVouchers = [
     [1,1,2,"Когда нить 1",21,11],
     [2,2,3,"Когда нить 2",22,12],
     [3,3,1,"Когда нить 3",23,13]
     ]

# Создаем таблицы, если они не созданы
SQLite.execute("""CREATE TABLE IF NOT EXISTS Client (ID INT, FName TEXT, NName TEXT, OName TEXT, Adr TEXT, Numer TEXT)""")
SQLite.execute("""CREATE TABLE IF NOT EXISTS Route (ID INT, Region TEXT, Climate TEXT, Long TEXT, Hotel TEXT, Money TEXT)""")
SQLite.execute("""CREATE TABLE IF NOT EXISTS Vouchers (ID INT, ObjRoute INT, ObjClient INT, Date TEXT, Count TEXT, Discount TEXT)""")

# Подтверждение
DataBase.commit()

# Заполняем таблицу данных
for ID in range(3):

    SQLite.execute(f"SELECT ID FROM Client WHERE ID = {MyClietn[ID][0]}")
    if SQLite.fetchone() is None:
        SQLite.execute(f"INSERT INTO Client VALUES ( {MyClietn[ID][0]}, '{MyClietn[ID][1]}', '{MyClietn[ID][2]}', '{MyClietn[ID][3]}', '{MyClietn[ID][4]}', '{MyClietn[ID][5]}')")
    DataBase.commit()

    SQLite.execute(f"SELECT ID FROM Route WHERE ID = {MyRoute[ID][0]}")
    if SQLite.fetchone() is None:
        SQLite.execute(f"INSERT INTO Route VALUES ( {MyRoute[ID][0]}, '{MyRoute[ID][1]}', '{MyRoute[ID][2]}', '{MyRoute[ID][3]}', '{MyRoute[ID][4]}', '{MyRoute[ID][5]}')")
    DataBase.commit()

    SQLite.execute(f"SELECT ID FROM Vouchers WHERE ID = {MyVouchers[ID][0]}")
    if SQLite.fetchone() is None:
        SQLite.execute(f"INSERT INTO Vouchers VALUES ( {MyVouchers[ID][0]}, {MyVouchers[ID][1]}, {MyVouchers[ID][2]}, '{MyVouchers[ID][3]}', '{MyVouchers[ID][4]}', '{MyVouchers[ID][5]}')")
    DataBase.commit()