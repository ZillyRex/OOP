
# https://codereview.stackexchange.com/questions/194062/heap-sort-implementation-in-python
# https://www.programiz.com/dsa/heap-sort


def heapify(L:list):
    for i in reversed(range(1, len(L))):
        parent = (i - 1) // 2
        if L[i] < L[parent]:
            L[i], L[parent] = L[parent], L[i]


def heap_sort(L: list) -> list:
    res = []
    while L:
        heapify(L)
        res.append(L.pop(0))
    return res


if __name__ == '__main__':
    L = [1, 4, 2, 3.6, -1, 0, 25, -34, 8, 9, 1, 0]
    print(L)
    print(heap_sort(L))
