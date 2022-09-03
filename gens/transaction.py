import random
from random import choice

types = [{"банки": ["Сбербанк", "Тинькофф", "Райффайзен", "Альфа-Банк", "Почта Банк", "Совкомбанк", "МТС банк", "Русский стандарт",
                    "Россельхозбанк", "Банк Открытие", "Росбанк"],
          "магазины": ["Красное и Белое", "Дикси", "Магнит", "Перекресток", "Пятерочка", "ДНС", "Лента", "Верный", "Вкусвилл",
                     "ДеливериКлаб", "МТС", "Яндекс.Маркет", "Ситилинк", "Эльдорадо", "Мвидео"],
          "Тип": ["Банк", "Магазин", "Клиент"],
          "Операция": ["Исходящий", "Входящий"]
          }]

mnames = ["Глеб", "Василий", "Дмитрий", "Геннадий", "Алексей", "Владислав", "Владимир", "Георгий", "Александр",
         "Максим", "Петр", "Николай", "Андрей", "Яков", "Серафим", "Евгений", "Михаил", "Артем", "Даниил"]
msurnames = [ "Маркин", "Черкашев", "Таубер", "Каменцев", "Городецкий", "Верный", "Любовец",
            "Петров", "Иванов", "Фролов", "Романов", "Воробьёв", "Сорокин", "Белов", "Жуков", "Крылов"]
mmiddlename = [ "Алексеевич", "Валентинович", "Александрович", "Викторович", "Гавриилович", "Егорович", "Нефёдович",
            "Рюрикович", "Степанович", "Федорович", "Якович", "Ульянович", "Прохорович", "Петрович", "Павлович", "Львович"]

fnames = ["Алина", "Максим", "Александра", "Елена", "Ирина", "Валентина", "Кира", "Полина", "Лана",
         "Диана", "Эмилия", "Любовь", "Юлия", "Ульяна", "Виктория", "Кристина", "Софья", "Маргарита", "Лилия"]
fsurnames = [ "Добрынина", "Цветова", "Есенина", "Бондаренко", "Зайцева", "Грушина", "Кожевникова",
            "Глебова", "Булгакова", "Миронова", "Белая", "Кузнецова", "Медведева", "Конева", "Зимина", "Краснова"]
fmiddlename = [ "Акимовна", "Артёмовна", "Валентиновна", "Георгиевна", "Данииловна", "Евдокимовна", "Елисеевна",
            "Игнатьевна", "Исааковна", "Иванова", "Климовна", "Марковна", "Остаповна", "Петровна", "Рюриковна", "Юрьевна"]

def trans_creation(how_many: int):
    bank_trans = []
    while how_many >= 1:
        for item in types:
            bank = item.get("банки")
            stores = item.get("магазины")
            type = item.get("Тип")
            via = item.get("Операция")
            trans_type = choice(type)
            via_type = choice(via)
            
            if trans_type == "Банк":
                bank_choice = choice(bank)
                bank_sum = random.randint(500, 100000)
                str_sum = str(bank_sum)+" Руб."
                if bank_choice not in bank_trans:
                    bank_trans.append(str_sum)
                    bank_trans.append(via_type)
                    bank_trans.append(trans_type)
                    bank_trans.append(bank_choice)
                    how_many -= 1

            elif trans_type == "Магазин":
                store_choice = choice(stores)
                store_sum = random.randint(40, 20000)
                str_s = str(store_sum)+" Руб."
                if store_choice not in bank_trans:
                    bank_trans.append(str_s)
                    bank_trans.append(via[0])
                    bank_trans.append(trans_type)
                    bank_trans.append(store_choice)
                    how_many -= 1
            else:
                
                sex = ["m","f"]
                user_sex = choice(sex)
                if  user_sex == "m":
                    human_choice = choice(msurnames) + ' ' + choice(mnames) + ' ' + choice(mmiddlename)
                if  user_sex == "f":
                    human_choice = choice(fsurnames) + ' ' + choice(fnames) + ' ' + choice(fmiddlename)
                human_sum = random.randint(100, 19999)
                human_str = str(human_sum)+" Руб."
                if human_choice not in bank_trans:
                    bank_trans.append(human_str)
                    bank_trans.append(via_type)
                    bank_trans.append(trans_type)
                    bank_trans.append(human_choice)
                    how_many -= 1
        return bank_trans
