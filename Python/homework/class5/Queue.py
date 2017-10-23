class Queue:
    def __init__(self):
        self.list = []

    def push(self, i):
        self.list.append(i)

    def pop(self):
        return self.list.pop(0)

    def printQueue(self):
        print self.list

if __name__ == "__main__":
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.printQueue()
    print queue.pop()
    queue.printQueue()
