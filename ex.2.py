school = {'1А': 20, "1Б": 23, "2А": 15, "2Б": 29, "3А": 26, "3Б": 14}
children = 0


# Ввод класс на русской раскладке!!


print(school)
print("Какое действие ? (Номер)")
print("1) изменение количества учащихся в одном из классов")
print("2) добавление нового класса (с количеством учеников)")
print("3) удаление класса из базы")
print("4) подсчет общего количества учащихся в школе")
chosen = int(input(">>>"))

while chosen > 4:
    print("Введите корректное число!")
    chosen = int(input(">>>"))

while chosen < 5:
    if chosen == 4:
        children = sum(school.values())
        print(children)
        break
    elif chosen == 3:
        rem_class = input("Какой класс удалить ?")
        school.pop(rem_class)
        print(school)
        break
    elif chosen == 2:
        new_calss = input("Какой класс добавить ? \n >>>")
        count_children = input("Сколько человек ? \n >>>")
        school[new_calss] = count_children
        print("Новый класс создан!")
        print(school)
        break
    elif chosen == 1:
        new_calss = input("Какой класс изменить ? \n >>>")
        count_children = input("Сколько человек ? \n >>>")
        if new_calss not in school:
            print("В школе нет такого класса !")
            break
        else:
            school[new_calss] = count_children
            print(" данные обновленны !")
            print(new_calss, count_children)
            break
