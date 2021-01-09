# --------------------------------------------------------------------------------------------------

import os.path as PH
import json as JS
import os
import sqlite3 as SQL

# --------------------------------------------------------------------------------------------------

# Клиент
class Client:

    def __init__(self, ID, FName, NName, OName, Adr, Numer):
        self.setID(ID)     
        self.setFName(FName)
        self.setNName(NName)
        self.setOName(OName)   
        self.setAdr(Adr) 
        self.setNumer(Numer)

    # ---------

    def setID(self,value):      self.__ID = value
    def setFName(self,value):   self.__FName = value
    def setNName(self,value):   self.__NName = value
    def setOName(self,value):   self.__OName = value
    def setAdr(self,value):     self.__Adr = value
    def setNumer(self,value):   self.__Numer = value
    
    # ---------    
    
    def getID(self):            return self.__ID
    def getFName(self):         return self.__FName 
    def getNName(self):         return self.__NName
    def getOName(self):         return self.__OName
    def getAdr(self):           return self.__Adr
    def getNumer(self):         return self.__Numer

    # ---------

    def __str__(self):
        return "ID: {}\nФамилия: {}\nИмя: {}\nОтчество: {}\nАдрес: {}\nНомер тел.: {} ".format(
            self.__ID, self.__FName, self.__NName, self.__OName, self.__Adr, self.__Numer )

# --------------------------------------------------------------------------------------------------

class ClientList(list):
  def getByID(self, id):
        for item in self:
              if item.getID() == id: return item
        else: return None 

# --------------------------------------------------------------------------------------------------

# Маршрут
class Route:

    def __init__(self, ID, Region, Climate, Long, Hotel, Money):
        self.setID(ID)     
        self.setRegion(Region)
        self.setClimate(Climate)
        self.setLong(Long)   
        self.setHotel(Hotel) 
        self.setMoney(Money)

    # ---------

    def setID(self,value):      self.__ID = value
    def setRegion(self,value):  self.__Region = value
    def setClimate(self,value): self.__Climate = value
    def setLong(self,value):    self.__Long = value
    def setHotel(self,value):   self.__Hotel = value
    def setMoney(self,value):   self.__Money = value
     
    # ---------

    def getID(self):            return self.__ID
    def getRegion(self):        return self.__Region 
    def getClimate(self):       return self.__Climate
    def getLong(self):          return self.__Long
    def getHotel(self):         return self.__Hotel
    def getMoney(self):         return self.__Money
    
    # ---------

    def __str__(self):
        return "ID: {}\nРегион: {}\nКлимат: {}\nДлительность: {}\nОтель: {}\nСтоимость: {} ".format(
            self.__ID, self.__Region, self.__Climate, self.__Long, self.__Hotel, self.__Money )

# --------------------------------------------------------------------------------------------------

class RouteList(list):
  def getByID(self, id):
        for item in self:
              if item.getID() == id: return item
        else: return None 

# --------------------------------------------------------------------------------------------------

# Путёвка
class Vouchers:

    # ---------

    __ID = int
    __Route = Route
    __Client = Client
    __Date = str
    __Count = int
    __Discount = int

    # ---------

    def __init__(self, ID, ObjRoute, ObjClient, Date, Count, Discount):
        self.setID(ID)     
        self.setRoute(ObjRoute)
        self.setClient(ObjClient)
        self.setDate(Date)   
        self.setCount(Count) 
        self.setDiscount(Discount)

    # ---------

    def setID(self,value):          self.__ID = value
    def setRoute(self,value):       self.__Route = value
    def setClient(self,value):      self.__Client = value
    def setDate(self,value):        self.__Date = value
    def setCount(self,value):       self.__Count = value
    def setDiscount(self,value):    self.__Discount = value
     
    # ---------

    def getID(self):                return self.__ID
    def getRoute(self):             return self.__Route
    def getClient(self):            return self.__Client
    def getDate(self):              return self.__Date
    def getCount(self):             return self.__Count
    def getDiscount(self):          return self.__Discount

    def __str__(self):
        return "ID: {}\nМаршрут: {}\nКлиент: {}\nДата: {}\nКол-во человек: {}\nСкидка: {} ".format(
            self.__ID, self.__Route, self.__Client, self.__Date, self.__Count, self.__Discount )

# --------------------------------------------------------------------------------------------------

class VouchersList(list):
  def getByID(self, id):
        for item in self:
              if item.getID() == id: return item
        else: return None 

# --------------------------------------------------------------------------------------------------

# Класс, отвечающий за базовые методы базы данных
class DataBase:

    def __init__(self):
        self.__Client =     ClientList()
        self.__Route =      RouteList()
        self.__Vouchers =   VouchersList()

     # --------- 

    def Clear(self):
        self.__Client.clear()
        self.__Route.clear()
        self.__Vouchers.clear()

    # --------- 

    # Метод для импорта базы данных из класса работы с JSON 
    # в класс работы с SQL, и на оборот. 
    # Для этого необходимо в метод из под одного экземпляра
    # как аргумент передать экземпляр другого класса.

    # Пример: 
    #   есть экземпляр с данными - DataJSON
    #   необходимо его данные импортировать в другой экземпляр - DataSQL
    #   для этого воспользуемся данной конструкцией - DataSQL.ImportDataBase(DataJSON)

    def ImportDataBase(self,DataBaseExemplar):
        NewDataBase = DataBaseExemplar.getDataBase()
        self.setDataBase(NewDataBase)

    def getDataBase(self): return {"Client" : self.__Client, "Route" : self.__Route, "Vouchers" : self.__Vouchers}

    def setDataBase(self,DataBaseArr):
        self.__Client =     DataBaseArr["Client"]
        self.__Route =      DataBaseArr["Route"]
        self.__Vouchers =   DataBaseArr["Vouchers"]

    # ---------

    def setClientDataBase(self, value):     self.__Client = value
    def setRouteDataBase(self, value):      self.__Route = value
    def setVouchersDataBase(self, value):   self.__Vouchers = value

    def getClientDataBase(self):     return self.__Client
    def getRouteDataBase(self):      return self.__Route
    def getVouchersDataBase(self):   return self.__Vouchers

     # --------- 

    def setID(self,value,ID):      self.__Client[ID].setID(value)
    def setFName(self,value,ID):   self.__Client[ID].setFName(value)
    def setNName(self,value,ID):   self.__Client[ID].setNName(value)
    def setOName(self,value,ID):   self.__Client[ID].setOName(value)
    def setAdr(self,value,ID):     self.__Client[ID].setAdr(value)
    def setNumer(self,value,ID):   self.__Client[ID].setNumer(value)
    
    # ---------    
    
    def getID(self,ID):            return self.__Client[ID].getID()
    def getFName(self,ID):         return self.__Client[ID].getFName()
    def getNName(self,ID):         return self.__Client[ID].getNName()
    def getOName(self,ID):         return self.__Client[ID].getOName()
    def getAdr(self,ID):           return self.__Client[ID].getAdr()
    def getNumer(self,ID):         return self.__Client[ID].getNumer()

    # --------- ---------

    def setID(self,value,ID):      self.__Route[ID].setID(value,ID)      
    def setRegion(self,value,ID):  self.__Route[ID].setRegion(value,ID)  
    def setClimate(self,value,ID): self.__Route[ID].setClimate(value,ID) 
    def setLong(self,value,ID):    self.__Route[ID].setLong(value,ID)   
    def setHotel(self,value,ID):   self.__Route[ID].setHotel(value,ID)  
    def setMoney(self,value,ID):   self.__Route[ID].setMoney(value,ID) 
     
    # ---------

    def getID(self,ID):            return self.__Route[ID].getID()   
    def getRegion(self,ID):        return self.__Route[ID].getRegion()
    def getClimate(self,ID):       return self.__Route[ID].getClimate()
    def getLong(self,ID):          return self.__Route[ID].getLong()  
    def getHotel(self,ID):         return self.__Route[ID].getHotel() 
    def getMoney(self,ID):         return self.__Route[ID].getMoney() 

    # --------- ---------

    def setID(self,ID,value):          self.Vouchers[ID].setID(ID,value)    
    def setRoute(self,ID,value):       self.Vouchers[ID].setRoute(ID,value)  
    def setClient(self,ID,value):      self.Vouchers[ID].setClient(ID,value) 
    def setDate(self,ID,value):        self.Vouchers[ID].setDate(ID,value)
    def setCount(self,ID,value):       self.Vouchers[ID].setCount(ID,value) 
    def setDiscount(self,ID,value):    self.Vouchers[ID].setDiscount(ID,value)
     
    # ---------

    def getID(self,ID):                return self.Vouchers[ID].getID()       
    def getRoute(self,ID):             return self.Vouchers[ID].getRoute()   
    def getClient(self,ID):            return self.Vouchers[ID].getClient() 
    def getDate(self,ID):              return self.Vouchers[ID].getDate()     
    def getCount(self,ID):             return self.Vouchers[ID].getCount()   
    def getDiscount(self,ID):          return self.Vouchers[ID].getDiscount() 

    # --------- ---------

    def addClient(self,ObjClient): 
       for ITEM in self.__Client:
           if(ITEM.getID() == ObjClient.getID()) : return 0
       self.__Client.append(ObjClient)

    def addRoute(self,ObjRoute): 
        for ITEM in self.__Route:
           if(ITEM.getID() == ObjRoute.getID()) : return 0
        self.__Route.append(ObjRoute)

    def addVouchers(self, ObjVouchers): 
        for ITEM in self.__Vouchers:
           if(ITEM.getID() == ObjVouchers.getID()) : return 0
        self.__Vouchers.append(ObjVouchers)

    # ---------

    def removeClient(self,ID): 
        N = 0
        for ITEM in self.__Client:
            if(ITEM.getID() == ID): 
                for I in self.__Vouchers:
                    if(I.getClient() == ITEM):
                        print("ERROR: Ошибка удаления")
                        return 0
                self.__Client.pop(N)
                return 0
            N+=1
       
    def removeRoute(self,ID): 
        N = 0
        for ITEM in self.__Route:
            if(ITEM.getID() == ID):
                for I in self.__Vouchers:
                    if(I.getRoute() == ITEM):
                        print("ERROR: Ошибка удаления")
                        return 0
                self.__Route.pop(N)
                return 0
            N+=1

    def removeVouchers(self, ID): 
        N = 0
        for ITEM in self.__Vouchers:
            if(ITEM.getID() == ID): 
                self.__Vouchers.pop(N)
                return 0
            N+=1

    # ---------

    def getClient(self):    return self.__Client
    def getRoute(self):     return self.__Route
    def getVouchers(self):  return self.__Vouchers 

# --------------------------------------------------------------------------------------------------

# Класс работы с JSON файлами
class DataBase_JSON(DataBase):

    def ReadFile(self, FileName):

        if FileName == "": print("\t --- ВЫ НЕ ВВЕЛИ НАЗВАНИЕ ФАЙЛА!!!"); return 0

        try: 
            with open(FileName) as Files: Data = JS.load(Files)

            for item in Data["Clients"]:
                Cl = Client(item["ID"], item["Фамилия"], item["Имя"], item["Отчество"], item["Адрес"], item["Тел"])
                self._DataBase__Client.append(Cl)

            for item in Data["Routes"]:
                Cl = Route(item["ID"], item["Регион"], item["Климат"], item["Длительность"], item["Отель"], item["Стоимость"])
                self._DataBase__Route.append(Cl)

            for item in Data["Vouchers"]:
                Cl = Vouchers(item["ID"], self._DataBase__Route.getByID(item["Roure"]), self._DataBase__Client.getByID(item["Client"]),  item["Data"], item["Count"], item["Discount"])
                self._DataBase__Vouchers.append(Cl)

        except(FileNotFoundError):  print("\t --- ФАЙЛА НЕ СУЩЕСТВУЕТ!!!") 

    # ---------

    def WriteFile(self, FileName): 

        if FileName == "": print("\t --- ВЫ НЕ ВВЕЛИ НАЗВАНИЕ ФАЙЛА!!!"); return 0 

        if FileName.endswith(".json"):

            L_Clients = []
            for item in self._DataBase__Client:
                CL = {
                    "ID": item.getID(),
                    "Фамилия": item.getFName(),
                    "Имя": item.getNName() ,
                    "Отчество": item.getOName(),
                    "Адрес": item.getAdr(),
                    "Тел": item.getNumer()
                }
                L_Clients.append(CL)

            L_Routes = []
            for item in self._DataBase__Route:
                CL = {
                    "ID": item.getID(),
                    "Регион": item.getRegion(),
                    "Климат": item.getClimate() ,          
                    "Длительность": item.getLong(),        
                    "Отель": item.getHotel(),              
                    "Стоимость": item.getMoney()           
                }                                          
                L_Routes.append(CL)

            L_Vouchers = []
            for item in self._DataBase__Vouchers:
                CL = {
                    "ID": item.getID(),                           
                    "Roure": item.getRoute().getID(),             
                    "Client": item.getClient().getID(),           
                    "Data": item.getDate(),                     
                    "Count": item.getCount(),                     
                    "Discount": item.getDiscount()                
                }                                                 
                L_Vouchers.append(CL)


            Data = {
                "Clients": L_Clients,
                "Routes": L_Routes,
                "Vouchers": L_Vouchers
            }

            with open(FileName, "w") as Output: JS.dump(Data, Output)

# --------------------------------------------------------------------------------------------------

# Класс работы с данными SQL 
class DataBase_SQLite(DataBase):

    def ReadFile(self, FileName):

        if FileName == "": print("\t --- ВЫ НЕ ВВЕЛИ НАЗВАНИЕ ФАЙЛА!!!"); return 0 

        MyDataBase = SQL.connect(FileName)
        SQLite = MyDataBase.cursor()

        for ITEM in SQLite.execute("SELECT * FROM Client"):     
            CL = Client(int(ITEM[0]),ITEM[1],ITEM[2],ITEM[3],ITEM[4],ITEM[5])
            self._DataBase__Client.append(CL)
        
        for ITEM in SQLite.execute("SELECT * FROM Route"):      
            CL = Route(int(ITEM[0]),ITEM[1],ITEM[2],ITEM[3],ITEM[4],ITEM[5])
            self._DataBase__Route.append(CL)
        
        for ITEM in SQLite.execute("SELECT * FROM Vouchers"):   
            CL = Vouchers(int(ITEM[0]),self._DataBase__Route.getByID(int(ITEM[1])),self._DataBase__Client.getByID(int(ITEM[2])),ITEM[3],ITEM[4],ITEM[5])
            self._DataBase__Vouchers.append(CL)

    # ---------

    def WriteFile(self, FileName): 

        if FileName == "": print("\t --- ВЫ НЕ ВВЕЛИ НАЗВАНИЕ ФАЙЛА!!!"); return 0 

        MyDataBase = SQL.connect(FileName)
        SQLite = MyDataBase.cursor()

        SQLite.execute("""CREATE TABLE IF NOT EXISTS Client (ID INT, FName TEXT, NName TEXT, OName TEXT, Adr TEXT, Numer TEXT)""")
        SQLite.execute("""CREATE TABLE IF NOT EXISTS Route (ID INT, Region TEXT, Climate TEXT, Long TEXT, Hotel TEXT, Money TEXT)""")
        SQLite.execute("""CREATE TABLE IF NOT EXISTS Vouchers (ID INT, ObjRoute INT, ObjClient INT, Date TEXT, Count TEXT, Discount TEXT)""")

        MyDataBase.commit()

        MyClietn    = [ [
            self._DataBase__Client[I].getID(),
            self._DataBase__Client[I].getFName(),
            self._DataBase__Client[I].getNName(),
            self._DataBase__Client[I].getOName(), 
            self._DataBase__Client[I].getAdr(),
            self._DataBase__Client[I].getNumer()
            ] for I in range(len(self._DataBase__Client)) ]


        MyRoute     = [ [
            self._DataBase__Route[I].getID(),
            self._DataBase__Route[I].getRegion(),
            self._DataBase__Route[I].getClimate(),
            self._DataBase__Route[I].getLong(), 
            self._DataBase__Route[I].getHotel(),
            self._DataBase__Route[I].getMoney()
            ] for I in range(len(self._DataBase__Route)) ] 
        
        MyVouchers  = [ [
            self._DataBase__Vouchers[I].getID(),
            self._DataBase__Vouchers[I].getRoute().getID(),
            self._DataBase__Vouchers[I].getClient().getID(),
            self._DataBase__Vouchers[I].getDate(), 
            self._DataBase__Vouchers[I].getCount(),
            self._DataBase__Vouchers[I].getDiscount()
            ] for I in range(len(self._DataBase__Vouchers)) ]

        for ID in range(len(MyClietn)): 
            SQLite.execute(f"SELECT ID FROM Client WHERE ID = {MyClietn[ID][0]}")
            if SQLite.fetchone() is None:
                SQLite.execute(f"INSERT INTO Client VALUES ( {MyClietn[ID][0]}, '{MyClietn[ID][1]}', '{MyClietn[ID][2]}', '{MyClietn[ID][3]}', '{MyClietn[ID][4]}', '{MyClietn[ID][5]}')")
            MyDataBase.commit()

        for ID in range(len(MyRoute)): 
            SQLite.execute(f"SELECT ID FROM Route WHERE ID = {MyRoute[ID][0]}")
            if SQLite.fetchone() is None:
                SQLite.execute(f"INSERT INTO Route VALUES ( {MyRoute[ID][0]}, '{MyRoute[ID][1]}', '{MyRoute[ID][2]}', '{MyRoute[ID][3]}', '{MyRoute[ID][4]}', '{MyRoute[ID][5]}')")
            MyDataBase.commit()

        for ID in range(len(MyVouchers)):
            SQLite.execute(f"SELECT ID FROM Vouchers WHERE ID = {MyVouchers[ID][0]}")
            if SQLite.fetchone() is None:
                SQLite.execute(f"INSERT INTO Vouchers VALUES ( {MyVouchers[ID][0]}, {MyVouchers[ID][1]}, {MyVouchers[ID][2]}, '{MyVouchers[ID][3]}', '{MyVouchers[ID][4]}', '{MyVouchers[ID][5]}')")
            MyDataBase.commit()
    
    
# --------------------------------------------------------------------------------------------------