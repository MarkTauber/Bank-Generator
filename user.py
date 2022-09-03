import random
import sqlite3
from sys import argv
from gens import namegen, phonegen, hash_key, cardgen
from gens.transaction import trans_creation

firstofall = argv
if firstofall[1].isdigit() == False:
    print("Разрешены только числовые значения. Будет сгенерировано 50 записей")
    user_how_many = 50
else:
    user_how_many = int(firstofall[1])
    if user_how_many <= 0:
        print("Разрешены только значения выше нуля. Будет сгенерировано 50 записей")
        user_how_many = 50

conn = sqlite3.connect('Users.db')
c = conn.cursor()

class User:
    def __init__(self, nums):
        self.nums = nums
        self.user = namegen
        self.phone = phonegen
        self.hash = hash_key
        self.creditcards = cardgen

    def new_user(self):
        num = self.nums
        user_list = []
        if num <= 0:
            print("Неа.")

        while num >= 1:
            transfer = trans_creation(num)
            user_list.append({
                "user": self.user.gen_unique_names(how_many=num),
                "phone": self.phone.Phone_Number(num),
                "password": self.hash.key(":$aL7_12345", num),
                "transfer_amount": transfer[0],
                "transfer_type": transfer[1],
                "transfer_client": transfer[2],
                "transfer": transfer[3],
                "card": self.creditcards.cards(num),
            })
            num -= 1
        return user_list

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, "
              "fio TEXT, phone TEXT, password TEXT, transfer_amount TEXT, "
              "transfer_type TEXT, transfer_client TEXT, transfer TEXT, cc TEXT)")

def data_entry():
    i = 1

        
    user_create = User(user_how_many)
    count = user_create.new_user()
    for item in count:
        print("Работаем над номером",i, end='... ')
        c.execute(
            "INSERT INTO Users(fio, phone, password, transfer_amount, transfer_type, transfer_client, transfer, cc) "
            "VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (item.get("user"),
                                            item.get("phone"),
                                            item.get("password"),
                                            item.get("transfer_amount"),
                                            item.get("transfer_type"),
                                            item.get("transfer_client"),
                                            item.get("transfer"),
                                            item.get("card"),
                                            ))
        conn.commit()
        print("Готово!")
        
        i = i+1




create_table()
data_entry()
c.close()
conn.close()
