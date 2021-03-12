class Empty(Exception):
    pass


class ArrayStack:
    def __init__(self):
        self.internal_list = []

    def __len__(self):
        return len(self.internal_list)

    def push(self, item):
        self.internal_list.append(item)

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        self.internal_list.pop()

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.internal_list[-1]

    def is_empty(self):
        return len(self.internal_list) == 0

AR = ArrayStack()
AR.push(1)
AR.pop()
AR.push(2)
print(AR.top())
AR.push(3)
AR.push(4)
print(AR.top())
print(len(AR))
