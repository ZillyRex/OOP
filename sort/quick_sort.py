# Wikipedia


def partition(L: list, left: int, right: int) -> int:
    pivot = left
    for i in range(left, right):
        if(L[i] < L[right]):
            L[i], L[pivot] = L[pivot], L[i]
            pivot += 1
    L[pivot], L[right] = L[right], L[pivot]
    return pivot


def quick_sort(L: list, left: int, right: int):
    left = left % len(L) if left < 0 else left
    right = right % len(L) if right < 0 else right
    if(left >= right):
        return
    pivot = partition(L, left, right)
    quick_sort(L, left, pivot-1)
    quick_sort(L, pivot+1, right)


if __name__ == '__main__':
    L = [1, 4, 2, 3.6, -1, 0, 25, -34, 8, 9, 1, 0]
    print(L)
    quick_sort(L, 0, -1)
    print(L)
