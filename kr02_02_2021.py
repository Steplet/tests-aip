def task_1(two_dim_words):
    #two_dim_words = [['art', 'common'], ['club', 'star'], ['nature', 'queen'], ['alpha', 'center', 'water']]
    list_2 = []
    for i in range(len(two_dim_words)):
        if len(two_dim_words[i]) > 1:
            for step in range(len(two_dim_words[i])):
                list_2.append(two_dim_words[i][step])
        else:
            list_2.append(two_dim_words[i])

    list_2.sort()
    list_2.sort(key=len)
    sorted_words = list_2 
    #print(list_2)

    return sorted_words





def task_5(lst1, lst2):
    #list_1 = [1, 45, 78, 23242, 988]
    #list_2 = [23, 745, 99, 121, 66, 1, 45]
    set_1 = set(lst1)
    set_2 = set(lst2)
    set_1.difference_update(set_2)
    #print(set_1)
    diff = set_1

    return diff


def task_6(lst):
    a = set(lst)
    b = tuple(a)
    #print(b)
    res = tuple(sorted(b)
    
    return res

