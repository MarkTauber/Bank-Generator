import re
import random

def cards(how_many: int):
    card_nums = []
    while how_many >= 1:
        card = str(random.randint(1111111111111111, 9999999999999999))
        combocard = re.sub('([^ ]{4})', r'\1 ', (card[:4] + '*' * 8 + card[-4:]))
        if combocard not in card_nums:
            card_nums.append(combocard)
            how_many -= 1
        return combocard