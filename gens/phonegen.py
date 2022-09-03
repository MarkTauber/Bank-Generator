import random
from random import randint
from random import choice

codes = ["925", "916", "920", "910", "980", "906", "902", "999"]

def Phone_Number(how_many):
    phones = []
    while how_many > 0:
        first = str(random.randint(100, 999))
        second = str(random.randint(10, 99))
        last = str(random.randint(10, 99))
        phone_range = "+7(" + choice(codes) + ")"+ '{}-{}-{}'.format(first, second, last) 
        if phone_range not in phones:
            phones.append(phone_range)
            how_many -= 1
        return phone_range
