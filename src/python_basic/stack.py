class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


class AnotherStack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


# s= Stack()
#
# print(s.is_empty())
# s.push(4)
# s.push('dog')
#
# print(s.peek())
# print(s.size())
#
#
# s2 = AnotherStack()
# s2.push('hello')
# s2.push('true')
# print(s2.pop())

m = Stack()
m.push('x')
m.push('y')
m.push('z')
while not m.is_empty():
    m.pop()
    # m.pop()

print(m.size())
