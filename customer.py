#Customer Details
from database import *
class Customer:

    def __init__(self, username: object, password: object, name: object, age: object, city: object, account_number: object) -> object:
        self.__username = username
        self.__password = password
        self.__name = name
        self.__age = age
        self.__city = city
        self.__account_number = account_number

    def createuser(self):
        db_query(f"INSERT INTO customers VALUES ('{self.__username}', '{self.__password}', '{self.__name}', '{self.__age}', '{self.__city}', '{self.__account_number}', 1  );")
        mydb.commit()