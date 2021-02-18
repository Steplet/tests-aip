def task_1(two_dim_words):
    two_dim_words = [['art', 'common'], ['club', 'star'], ['nature', 'queen'], ['alpha', 'center', 'water']]
    list_2 = []
    for i in range(len(list_1)):
        if len(list_1[i]) > 1:
            for step in range(len(list_1[i])):
                list_2.append(list_1[i][step])
        else:
            list_2.append(list_1[i])

    list_2.sort()
    list_2.sort(key=len)
    list_2 = sorted_words
    #print(list_2)

    return sorted_words


def task_4_1(words):
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res.
        """

    return res


def task_4_2(words):  # можно сделать тесты
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res.
        """

    return res


def task_4_3(words):
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res.
        """

    return res


def task_5(lst1, lst2):
    """
        Здесь должен быть ваш код.
        Переменные lst1 и lst2 - два данных списка.
        Финальное значение должно быть помещено в переменную diff.
        """

    return diff


def task_6(lst):
    """
        Здесь должен быть ваш код.
        Переменная lst - ваш список.
        Финальное значение должно быть помещено в переменную res.
        """

    return res

