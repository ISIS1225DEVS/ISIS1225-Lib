from DISClib.ADT.lists import List
from DISClib.ADT.stack import Stack
from DISClib.ADT.lists import clone
from DISClib.ADT.lists import translate
from DISClib.ADT.queue import Queue
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
