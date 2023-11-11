from DISClib.ADT.lists import List
# from DISClib.ADT.lists import List2


def cmp_test(a, b):
    key = "testkey"
    ka = a.get(key)
    kb = b.get(key)
    if ka < kb:
        return -1
    elif ka > kb:
        return 1
    else:
        return 0


# main del ejercicio
if __name__ == "__main__":
    test_list = List(implementation="ArrayList")
    # test_list = List2.new(implementation="ArrayList")

    print(test_list)
    print(type(test_list))
    print("----------- config -----------")
    # test_list = test_list.config()
    print(test_list)
    print(type(test_list))

    test_data = [1, 2, 3, 4, 5]

    for i in test_data:
        test_list.add_last(i)

    print(test_list)

    test_data = [
        {"testkey": 1, "testvalue": "one"},
        {"testkey": 2, "testvalue": "two"},
        {"testkey": 3, "testvalue": "three"},
        {"testkey": 4, "testvalue": "four"},
        {"testkey": 5, "testvalue": "five"},
    ]

    test_list = List(implementation="ArrayList",
                     elements=test_data,
                     cmp_function=cmp_test)
    print(test_list)
    print(type(test_list))
    print("----------- config -----------")
    # test_list = test_list.config()
    # print(test_list)
    # print(type(test_list))
    print("iterating ADT List")
    for d in test_list:
        print(d)
    
    a = test_list.get_first()
    print(a)

    print(test_list.get_last())
