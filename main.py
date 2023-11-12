from DISClib.ADT.lists import List
import random
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
    imp = "ArrayList"   # "SingleLinked", "DoubleLinked", "ArrayList"
    print(f"Testing '{imp}' implementation of ADT List")
    test_lt_1 = List(implementation=imp)
    # test_lt_1 = List2.new(implementation="ArrayList")

    print("----------- config -----------")
    # test_lt_1 = test_lt_1.config()
    print(test_lt_1)
    print(type(test_lt_1))

    print("----------- int list -----------")
    test_data = (1, 2, 3, 4, 5)

    for i in test_data:
        test_lt_1.add_last(i)

    print(test_lt_1)
    test_lt_2 = List(implementation=imp,
                     io=test_data,
                     cmp_function=cmp_test)
    print(test_lt_2)
    print(type(test_lt_2))

    print("----------- dict list -----------")
    test_data = (
        {"testkey": 1, "testvalue": "one"},
        {"testkey": 2, "testvalue": "two"},
        {"testkey": 3, "testvalue": "three"},
        {"testkey": 4, "testvalue": "four"},
        {"testkey": 5, "testvalue": "five"},
    )

    test_lt_3 = List(implementation=imp,
                     io=test_data,
                     cmp_function=cmp_test)
    print(test_lt_3)
    print(type(test_lt_3))
    print("----------- config -----------")
    # test_lt_1 = test_lt_1.config()
    # print(test_lt_1)
    # print(type(test_lt_1))
    print("iterating ADT List")
    for d in test_lt_3:
        print(d)
    a = test_lt_3.sublist(0, 4)
    print("sublist created", a)

    print(test_lt_3._size)
    print(test_lt_3.size)

    print("----------- str list -----------")
    test_data = ("one", "two", "three", "four", "five")
    test_lt_4 = List(implementation=imp,
                     io=test_data,
                     cmp_function=cmp_test)
    print(test_lt_4)
    print(type(test_lt_4))

    test_len = len(test_lt_4.elements)
    i, j = random.choices(range(0, test_len), k=2)
    # sample(range(test_len*2, test_len*3), 2)
    print(f"i: {i}, j: {j}")
    sub = test_lt_4.sublist(0, 1)
    print(sub)

    print("----------- concat list -----------")
    test_data = (1, 2, 3, 4, 5)
    test_lt_5 = List(implementation=imp,
                     io=test_data,
                     cmp_function=cmp_test)

    test_data = (6, 7, 8, 9, 10)
    test_lt_6 = List(implementation=imp,
                     io=test_data,
                     cmp_function=cmp_test)

    test_lt_7 = test_lt_5.concat(test_lt_6)
    print(test_lt_7)
    print(type(test_lt_7))
    # test_lt_7 = test_lt_5 + test_lt_6
