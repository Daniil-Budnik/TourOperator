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

class DataBase_JSON:

    def __init__(self, FileName = ""):

        self.__Client =     ClientList()
        self.__Route =      RouteList()
        self.__Vouchers =   VouchersList()

        if FileName != "": self.ReadFile(FileName) 
        else: print("\t --- ВЫ НЕ ВВЕЛИ НАЗВАНИЕ ФАЙЛА!!!") 
    
    # ---------

    def ReadFile(self, FileName):
        try: 
            with open(FileName) as Files: Data = JS.load(Files)

            for item in Data["Clients"]:
                Cl = Client(item["ID"], item["Фамилия"], item["Имя"], item["Отчество"], item["Адрес"], item["Тел"])
                self.__Client.append(Cl)

            for item in Data["Routes"]:
                Cl = Route(item["ID"], item["Регион"], item["Климат"], item["Длительность"], item["Отель"], item["Стоимость"])
                self.__Route.append(Cl)

            for item in Data["Vouchers"]:
                Cl = Vouchers(item["ID"], self.__Route.getByID(item["Roure"]), self.__Client.getByID(item["Client"]),  item["Data"], item["Count"], item["Discount"])
                self.__Vouchers.append(Cl)

        except(FileNotFoundError):  print("\t --- ФАЙЛА НЕ СУЩЕСТВУЕТ!!!") 

    # ---------

    def WriteFile(self, FileName): 

        if FileName.endswith(".json"):

            L_Clients = []
            for item in self.__Client:
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
            for item in self.__Route:
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
            for item in self.__Vouchers:
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

    # ---------

    def Clear(self):
        self.__Client.clear()
        self.__Route.clear()
        self.__Vouchers.clear()

    # --------- ---------

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

class DataBase_SQLite:

    
    def __init__(self, FileName = ""):

        self.__Client =     ClientList()
        self.__Route =      RouteList()
        self.__Vouchers =   VouchersList()

        if FileName != "": self.ReadFile(FileName) 
        else: print("\t --- ВЫ НЕ ВВЕЛИ НАЗВАНИЕ ФАЙЛА!!!") 
    
    # ---------

    def ReadFile(self, FileName):
        DataBase = SQL.connect(FileName)
        SQLite = DataBase.cursor()

        for ITEM in SQLite.execute("SELECT * FROM Client"):     
            CL = Client(int(ITEM[0]),ITEM[1],ITEM[2],ITEM[3],ITEM[4],ITEM[5])
            self.__Client.append(CL)
        
        for ITEM in SQLite.execute("SELECT * FROM Route"):      
            CL = Route(int(ITEM[0]),ITEM[1],ITEM[2],ITEM[3],ITEM[4],ITEM[5])
            self.__Route.append(CL)
        
        for ITEM in SQLite.execute("SELECT * FROM Vouchers"):   
            CL = Vouchers(int(ITEM[0]),self.__Route.getByID(int(ITEM[1])),self.__Client.getByID(int(ITEM[2])),ITEM[3],ITEM[4],ITEM[5])
            self.__Vouchers.append(CL)

    # ---------

    def WriteFile(self, FileName): 

        DataBase = SQL.connect(FileName)
        SQLite = DataBase.cursor()

        SQLite.execute("""CREATE TABLE IF NOT EXISTS Client (ID INT, FName TEXT, NName TEXT, OName TEXT, Adr TEXT, Numer TEXT)""")
        SQLite.execute("""CREATE TABLE IF NOT EXISTS Route (ID INT, Region TEXT, Climate TEXT, Long TEXT, Hotel TEXT, Money TEXT)""")
        SQLite.execute("""CREATE TABLE IF NOT EXISTS Vouchers (ID INT, ObjRoute INT, ObjClient INT, Date TEXT, Count TEXT, Discount TEXT)""")

        DataBase.commit()

        MyClietn    = [ [
            self.__Client[I].getID(),
            self.__Client[I].getFName(),
            self.__Client[I].getNName(),
            self.__Client[I].getOName(), 
            self.__Client[I].getAdr(),
            self.__Client[I].getNumer()
            ] for I in range(len(self.__Client)) ]


        MyRoute     = [ [
            self.__Route[I].getID(),
            self.__Route[I].getRegion(),
            self.__Route[I].getClimate(),
            self.__Route[I].getLong(), 
            self.__Route[I].getHotel(),
            self.__Route[I].getMoney()
            ] for I in range(len(self.__Route)) ] 
        
        MyVouchers  = [ [
            self.__Vouchers[I].getID(),
            self.__Vouchers[I].getRoute().getID(),
            self.__Vouchers[I].getClient().getID(),
            self.__Vouchers[I].getDate(), 
            self.__Vouchers[I].getCount(),
            self.__Vouchers[I].getDiscount()
            ] for I in range(len(self.__Vouchers)) ]

        for ID in range(len(MyClietn)): 
            SQLite.execute(f"SELECT ID FROM Client WHERE ID = {MyClietn[ID][0]}")
            if SQLite.fetchone() is None:
                SQLite.execute(f"INSERT INTO Client VALUES ( {MyClietn[ID][0]}, '{MyClietn[ID][1]}', '{MyClietn[ID][2]}', '{MyClietn[ID][3]}', '{MyClietn[ID][4]}', '{MyClietn[ID][5]}')")
            DataBase.commit()

        for ID in range(len(MyRoute)): 
            SQLite.execute(f"SELECT ID FROM Route WHERE ID = {MyRoute[ID][0]}")
            if SQLite.fetchone() is None:
                SQLite.execute(f"INSERT INTO Route VALUES ( {MyRoute[ID][0]}, '{MyRoute[ID][1]}', '{MyRoute[ID][2]}', '{MyRoute[ID][3]}', '{MyRoute[ID][4]}', '{MyRoute[ID][5]}')")
            DataBase.commit()

        for ID in range(len(MyVouchers)):
            SQLite.execute(f"SELECT ID FROM Vouchers WHERE ID = {MyVouchers[ID][0]}")
            if SQLite.fetchone() is None:
                SQLite.execute(f"INSERT INTO Vouchers VALUES ( {MyVouchers[ID][0]}, {MyVouchers[ID][1]}, {MyVouchers[ID][2]}, '{MyVouchers[ID][3]}', '{MyVouchers[ID][4]}', '{MyVouchers[ID][5]}')")
            DataBase.commit()


    # ---------

    def Clear(self):
        self.__Client.clear()
        self.__Route.clear()
        self.__Vouchers.clear()

    # --------- ---------

    def setFName(self,value,ID):   self.__Client[ID].setFName(value)
    def setNName(self,value,ID):   self.__Client[ID].setNName(value)
    def setOName(self,value,ID):   self.__Client[ID].setOName(value)
    def setAdr(self,value,ID):     self.__Client[ID].setAdr(value)
    def setNumer(self,value,ID):   self.__Client[ID].setNumer(value)
    
    # ---------    
    
    def getFName(self,ID):         return self.__Client[ID].getFName()
    def getNName(self,ID):         return self.__Client[ID].getNName()
    def getOName(self,ID):         return self.__Client[ID].getOName()
    def getAdr(self,ID):           return self.__Client[ID].getAdr()
    def getNumer(self,ID):         return self.__Client[ID].getNumer()

    # --------- ---------
     
    def setRegion(self,value,ID):  self.__Route[ID].setRegion(value,ID)  
    def setClimate(self,value,ID): self.__Route[ID].setClimate(value,ID) 
    def setLong(self,value,ID):    self.__Route[ID].setLong(value,ID)   
    def setHotel(self,value,ID):   self.__Route[ID].setHotel(value,ID)  
    def setMoney(self,value,ID):   self.__Route[ID].setMoney(value,ID) 
     
    # ---------
  
    def getRegion(self,ID):        return self.__Route[ID].getRegion()
    def getClimate(self,ID):       return self.__Route[ID].getClimate()
    def getLong(self,ID):          return self.__Route[ID].getLong()  
    def getHotel(self,ID):         return self.__Route[ID].getHotel() 
    def getMoney(self,ID):         return self.__Route[ID].getMoney() 

    # --------- ---------
  
    def setRoute(self,ID,value):       self.Vouchers[ID].setRoute(ID,value)  
    def setClient(self,ID,value):      self.Vouchers[ID].setClient(ID,value) 
    def setDate(self,ID,value):        self.Vouchers[ID].setDate(ID,value)
    def setCount(self,ID,value):       self.Vouchers[ID].setCount(ID,value) 
    def setDiscount(self,ID,value):    self.Vouchers[ID].setDiscount(ID,value)
     
    # ---------
     
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
