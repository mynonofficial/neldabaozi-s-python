class Stack:
    def __init__(self):
        self.list = []

    def push(self, i):
        self.list.append(i)

    def pop(self):
        return self.list.pop()

    def printStack(self):
        print self.list

print __name__
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.printStack()
    print stack.pop()
    stack.printStack()
