# CIG "Design a stack with getMIN()"


class Stack:

    def __init__(self, L: list):
        self.stack = list(L)
        self.min_stack = self._init_min_stack()

    def _init_min_stack(self):
        if(len(self.stack) == 0):
            return []
        cur_min = self.stack[0]
        min_stack = []
        for i in self.stack:
            cur_min = i if i < cur_min else cur_min
            min_stack.append(cur_min)
        return min_stack

    def push(self, item):
        self.stack.append(item)
        if(len(self.min_stack) == 0):
            self.min_stack.append(item)
        else:
            cur_min = self.min_stack[-1]
            self.min_stack.append(item if item < cur_min else cur_min)

    def pop(self):
        if(len(self.stack) == 0):
            return None
        top = self.stack.pop()
        self.min_stack.pop()
        return top

    def get_min(self):
        return None if len(self.min_stack) == 0 else self.min_stack[-1]

    def print(self):
        print(self.stack)


def main():
    ms = Stack([31, 2, 2, 4])
    ms.print()
    print(ms.min_stack)
    print(ms.get_min())

    ms.push(108)
    ms.print()
    print(ms.min_stack)
    print(ms.get_min())

    top = ms.pop()
    print(top)
    ms.print()
    print(ms.min_stack)
    print(ms.get_min())

    top = ms.pop()
    print(top)
    ms.print()
    print(ms.min_stack)
    print(ms.get_min())


if __name__ == '__main__':
    main()
