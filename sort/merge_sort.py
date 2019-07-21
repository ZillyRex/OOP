def merge(left: list, right: list) -> list:
    res = []
    while(left and right):
        res.append(left.pop(0) if left[0] < right[0] else right.pop(0))
    if(left):
        res += left
    if(right):
        res += right
    return res


def merge_sort(L: list) -> list:
    if(len(L) <= 1):
        return L
    mid = len(L)//2
    left = L[:mid]
    right = L[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


if __name__ == '__main__':
    L = [1, 4, 2, 3.6, -1, 0, 25, -34, 8, 9, 1, 0]
    print(L)
    print(merge_sort(L))