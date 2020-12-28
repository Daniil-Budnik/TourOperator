# --------------------------------------------------------------------------------------------------

import os
import sqlite3 as SQL
import TourOperator as Tour

# --------------------------------------------------------------------------------------------------

def Task_1(): 
    print("========================================================")
    print("\n\t >>> ЗАДАЧА 1 <<<")

    # Генерируем БД

    MyClietn = [
        Tour.Client(1,"Фам1","Имя1","Очт1","Адрес1",80000001),
        Tour.Client(2,"Фам2","Имя2","Очт2","Адрес2",80000002),
        Tour.Client(3,"Фам3","Имя3","Очт3","Адрес3",80000003)
        ]
    
    MyRoute = [
        Tour.Route(1,"Рег1","Климат1","Длительность1","Отель1",100001),
        Tour.Route(2,"Рег2","Климат2","Длительность2","Отель2",100002),
        Tour.Route(3,"Рег3","Климат3","Длительность3","Отель3",100003)
        ]
    
    MyVouchers = [
        Tour.Vouchers(1,MyRoute[1],MyClietn[2],"Когда нить 1",21,11),
        Tour.Vouchers(2,MyRoute[2],MyClietn[0],"Когда нить 1",22,12),
        Tour.Vouchers(3,MyRoute[0],MyClietn[1],"Когда нить 1",23,13)
        ]
    
    # Выводим всю информацию, загенерированную в БД

    print("\n\n\t>> Клиенты: <<\n")
    for Count in MyClietn: print(Count,'\n')
    
    print("\n\n\t>> Маршруты: <<\n")
    for Count in MyRoute: print(Count,'\n')
    
    print("\n\n\t>> Путёвки: <<\n")
    for Count in MyVouchers: print(Count,'\n')

# --------------------------------------------------------------------------------------------------

def Task_2():
    print("========================================================")
    print("\n\t >>> ЗАДАЧА 2 <<<")

    # Считываем БД с json
    BD = Tour.DataBase_JSON("Data.json")

    # Выводим всю информацию
    print("\n\n\t>> Клиенты: <<\n")
    for Count in BD.getClient(): print(Count,'\n')
    
    print("\n\n\t>> Маршруты: <<\n")
    for Count in BD.getRoute(): print(Count,'\n')
    
    print("\n\n\t>> Путёвки: <<\n")
    for Count in BD.getVouchers(): print(Count,'\n')

    print("========================================================")

    # Создаём новые данные
    Cl = Tour.Client(4,"G","B","D","S","48")
    Rl = Tour.Route(4,"d","B","D","S","5000")
    Vl = Tour.Vouchers(4,Rl,Cl,"D","S","48")

    # Добавляем
    BD.addClient(Cl)
    BD.addRoute(Rl)
    BD.addVouchers(Vl)

    # Записываем
    BD.WriteFile("New.json")

    # Чистим
    BD.Clear()

    # Читаем
    BD.ReadFile("New.json")

    # Выводим всю информацию
    print("\n\n\t>> Клиенты: <<\n")
    for Count in BD.getClient(): print(Count,'\n')
    
    print("\n\n\t>> Маршруты: <<\n")
    for Count in BD.getRoute(): print(Count,'\n')
    
    print("\n\n\t>> Путёвки: <<\n")
    for Count in BD.getVouchers(): print(Count,'\n')

# --------------------------------------------------------------------------------------------------

def Task_3(): 
    print("========================================================")
    print("\n\t >>> ЗАДАЧА 3 <<<")
    
    # Если база данных не создана, генерируем тестовые данные
    import GenSQL

    # Загружаем базу данных
    BD = Tour.DataBase_SQLite("MyDataBase.db")

    # Выводим всю информацию
    print("\n\n\t>> Клиенты: <<\n")
    for Count in BD.getClient(): print(Count,'\n')
    
    print("\n\n\t>> Маршруты: <<\n")
    for Count in BD.getRoute(): print(Count,'\n')
    
    print("\n\n\t>> Путёвки: <<\n")
    for Count in BD.getVouchers(): print(Count,'\n')
    
    print("========================================================")


     # Создаём новые данные
    Cl = Tour.Client(4,"G","B","D","S","48")
    Rl = Tour.Route(4,"d","B","D","S","5000")
    Vl = Tour.Vouchers(4,Rl,Cl,"D","S","48")

    # Добавляем
    BD.addClient(Cl)
    BD.addRoute(Rl)
    BD.addVouchers(Vl)

    # Удаляем один случайный элемент
    BD.removeVouchers(1)

    # Записываем
    BD.WriteFile("New.db")

    # Чистим
    BD.Clear()

    # Читаем
    BD.ReadFile("New.db")

    # Выводим всю информацию
    print("\n\n\t>> Клиенты: <<\n")
    for Count in BD.getClient(): print(Count,'\n')
    
    print("\n\n\t>> Маршруты: <<\n")
    for Count in BD.getRoute(): print(Count,'\n')
    
    print("\n\n\t>> Путёвки: <<\n")
    for Count in BD.getVouchers(): print(Count,'\n')


# --------------------------------------------------------------------------------------------------

def Main():

    #Task_1()
    #Task_2()
    Task_3()

# --------------------------------------------------------------------------------------------------

if __name__ == "__main__": Main()

# --------------------------------------------------------------------------------------------------
