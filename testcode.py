from MyQuickSort import QuickSort
from random import randint


result = set()
for i in range(100):
    size = randint(1, 1000)
    lst =  []
    for i in range(size):
        lst.append(randint(0, 40000))
    if i % 2 == 0:
        print(lst)
    before = lst[:]
    QuickSort(lst)
    before.sort()
    result.add(lst == before)

print(result)