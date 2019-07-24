# CIG "生成窗口最大值函数"

from collections import deque


def max_window(arr: list, w: int):
    if(len(arr) == 0 or w < 1 or len(arr) < w):
        return None
    qmax = deque()
    res = []
    for i in range(len(arr)):
        while(len(qmax) != 0 and arr[qmax[-1]] <= arr[i]):
            qmax.pop()
        qmax.append(i)
        if(qmax[0] == i-w):
            qmax.popleft()
        if(i >= w-1):
            res.append(arr[qmax[0]])
    return res


def main():
    arr = [4, 3, 5, 4, 3, 3, 6, 7]
    w = 3
    print(max_window(arr, w))


if __name__ == '__main__':
    main()
