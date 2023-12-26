from DISClib.ADT.lists import List
from DISClib.ADT.stack import Stack
from DISClib.ADT.lists import clone
from DISClib.ADT.lists import translate
from DISClib.ADT.queue import Queue
from DISClib.ADT.maps import Map
import random
# from DISClib.ADT.lists import List2
from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


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


def cmp_test2(ka, eb):
    kb = eb.get_key()
    if type(ka) is not type(kb):
        err_msg = f"Invalid comparison between {type(ka)} and "
        err_msg += f"{type(kb)} keys"
        raise TypeError(err_msg)
    if (ka == kb):
        return 0
    elif (ka > kb):
        return 1
    return -1


# main del ejercicio
if __name__ == "__main__":
    imp = "DoubleLinked"   # "SingleLinked", "DoubleLinked", "ArrayList"
    print(f"Testing '{imp}' ds_config of ADT List")
    test_lt_1 = List(dstruct=imp)
    # test_lt_1 = List2.new(dstruct="ArrayList")

    print("----------- config -----------")
    # test_lt_1 = test_lt_1.config()
    print(test_lt_1)
    print(type(test_lt_1))

    print("----------- int list -----------")
    test_data = (1, 2, 3, 4, 5)
    test_data2 = [1, 2, 3, 4, 5]
    test_data3 = {1, 2, 3, 4, 5}

    for i in test_data:
        test_lt_1.add_last(i)

    print(test_lt_1)
    test_lt_2 = List(dstruct=imp,
                     iodata=test_data2,
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

    test_lt_3 = List(dstruct=imp,
                     iodata=test_data,
                     cmp_function=cmp_test)
    print(test_lt_3)
    print(type(test_lt_3))
    print("----------- config -----------")
    print("iterating ADT List")
    print("from head to tail")
    for d in test_lt_3:
        print(d)
    print("from tail to head")
    for d in reversed(test_lt_3):
        print(d)

    print("----------- concat list -----------")
    test_data = (1, 2, 3, 4, 5)
    test_lt_5 = List(dstruct=imp,
                     iodata=test_data,
                     cmp_function=cmp_test)

    test_data = (6, 7, 8, 9, 10)
    test_lt_6 = List(dstruct=imp,
                     iodata=test_data,
                     cmp_function=cmp_test)

    test_lt_7 = test_lt_5.concat(test_lt_6)
    print(test_lt_5)
    print(test_lt_6)
    print(type(test_lt_6))
    print(test_lt_7)
    print(type(test_lt_7))
    # test_lt_7 = test_lt_5 + test_lt_6

    start = 1
    end = 1
    a = (start, end)
    MIN = 0
    MAX = 5
    test = (MIN <= start <= end <= MAX)
    print(test)

    a = test_lt_3.sublist(1, 3)
    print("sublist created", a)

    print(test_lt_3._size)
    print(test_lt_3.size)

    print("----------- str list -----------")
    test_data = ("one", "two", "three", "four", "five")
    test_lt_4 = List(dstruct=imp,
                     iodata=test_data,
                     cmp_function=cmp_test)
    print(test_lt_4)
    print(type(test_lt_4))

    test_len = test_lt_4.size()
    i, j = random.choices(range(0, test_len), k=2)
    # sample(range(test_len*2, test_len*3), 2)
    print(f"i: {i}, j: {j}")
    sub = test_lt_4.sublist(1, 1)
    print(sub)

    print("changing info")
    print(test_lt_2)
    test_lt_2.exchange(i, j)
    print(test_lt_2)
    print(len(test_lt_2))

    for i in reversed(test_lt_2):
        print(i)
    trans = translate(test_lt_2, "SingleLinked")
    bb = Queue(cmp_function=cmp_test)
    bbb = Queue(cmp_function=cmp_test)
    bbb.enqueue(22)
    bbb.enqueue(33)
    bb.enqueue(1)
    print(bb)
    print(type(bb))
    print(bb.is_empty())
    print(bb.size())
    bb.enqueue(2)
    # bb.enqueue("value")

    dddd = Queue()
    # dddd.peek()

    for a in bb:
        print(a)

    bb = bb.concat(bbb)
    print(bb)

    aaaa = clone(bb)
    print(aaaa)
    print(trans)

    TEST_STR_LT = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
    ]

    test_data = (
        {"testkey": 1, "testvalue": "one"},
        {"testkey": 2, "testvalue": "two"},
        {"testkey": 3, "testvalue": "three"},
        {"testkey": 4, "testvalue": "four"},
        {"testkey": 5, "testvalue": "five"},
    )

    print("----------- Maps -----------")
    m = Map(dstruct="SeparateChaining",   # "LinearProbing", "SeparateChaining"
            iodata=test_data,
            nentries=2,
            min_alpha=0,
            max_alpha=4,
            rehashable=True,
            key="testkey",)
            # cmp_function=cmp_test2)
    print(m.mcapacity)
    print(m.nentries)
    print(m.size())
    print(m.hash_table)
    print(m._key_type, m._value_type)
    print(m._cur_alpha)
    keys = m.keys()
    print(keys.size(), type(keys), len(keys))
    values = m.values()
    print(values.size(), type(values), len(values))

    # test_data = (
    #     {"testkey": 1, "testvalue": "one"},
    #     {"testkey": 2, "testvalue": "two"},
    #     {"testkey": 3, "testvalue": "three"},
    #     {"testkey": 4, "testvalue": "four"},
    #     {"testkey": 5, "testvalue": "five"},
    # )
    # print(type(m))
    # # print(type(type(m)))
    # print(m.is_empty())
    # print(m.size())
    # # print("\nadding data 1")
    # # m.put(1, 1)
    # print(m.hash_table)
    # # print("\nadding data 2")
    # # m.put(2, 2)
    # # print(m.hash_table)

    # # # print(m)
    # # print("\nadding data 11")
    # # m.put(11, 11)
    # # print(m.hash_table)
    # # print("\nchecking data 9")
    # # print(m.contains(9))
    # # print("\nchecking data 11")
    # print(m.contains(11))

    # print(m)
    # m.put(1, {"testkey": 1, "testvalue": "two"})
    # m.put(2, {"testkey": 2, "testvalue": "one"})
    # m.put(3, {"testkey": 3, "testvalue": "one"})
    # m.put(4, {"testkey": 4, "testvalue": "one"})
    # m.put(5, {"testkey": 5, "testvalue": "one"})
    # m.put(6, {"testkey": 6, "testvalue": "one"})
    # m.put(7, {"testkey": 7, "testvalue": "one"})
    # m.put(8, {"testkey": 8, "testvalue": "one"})
    # m.put(9, {"testkey": 9, "testvalue": "one"})
    # m.put(10, {"testkey": 10, "testvalue": "one"})
    # m.put(11, {"testkey": 11, "testvalue": "one"})
    # # print(isinstance(m, (T)))

    # for a in test_data:
    #     # print(a)
    #     k = a.get("testkey")
    #     # print(k, a)
    #     m.put(k, a)
    # #     # m.put(k, v)
    # print(m)
    # print(m.size())
    # print(m.hash_table.size())
    # print(m.values())
    # print(m.keys())
    # print(m.entries())

    # for a in test_data:
    #     k = a.get("testkey")
    #     print(m.remove(k))

    # # print(m.mcapacity)
    # print(f"m.size(): {m.size()}")
    # # print(m.nentries)
    # # print(m.hash_table.size())
    # print(m.values())
    # print(m.keys())
    # print(m.entries())
    print(m._value_type, m._key_type)
    print(m)

    TEST_SET_LT = [
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9},
        {10, 11, 12},
        {13, 14, 15},
        {16, 17, 18},
        {19, 20, 21},
        {22, 23, 24},
        {25, 26, 27},
        {28, 29, 30},
        {31, 32, 33},
        {34, 35, 36},
    ]

    t_data = {1, 2, 3}
    print(t_data, type(t_data))

    test_lt = list(TEST_SET_LT)
    idx = -1
    i = 0
    for elm in TEST_SET_LT:
        print(elm)
        if elm == t_data:
            idx = i
        i += 1
    print(idx)
    print(len(TEST_SET_LT))
    # print(t_data in test_lt)

    # # Define a list of sets
    # list_of_sets = [
    #     {1, 2, 3},
    #     {4, 5, 6},
    #     {7, 8, 9},
    # ]

    # # Print the list of sets
    # for s in list_of_sets:
    #     print(s, type(s))
    #     if s == t_data:
    #         print("found")

    # Define a list of sets
    list_of_sets = [
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9},
    ]

    # Define the set you're looking for
    target_set = {4, 5, 6}

    # Use list comprehension to find the set
    found_sets = [s for s in list_of_sets if s == target_set]

    # Print the found sets
    print(found_sets[0], type(found_sets[0]))

    test_list = [
        {'Course': "C++", 'Author': "Jerry"},
        {'Course': "Python", 'Author': "Mark"},
        {'Course': "Java", 'Author': "Paul"}]

    def search(name, test_list):
        return [element for element in test_list if element['Author'] == name]

    res = search("Paul", test_list)
    print(res)
