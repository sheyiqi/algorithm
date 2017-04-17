class Queue(object):
    def __init__(self,size):
        self.queue=[]
        self.size=size

    def queueLen(self):
        return len(self.queue)

    def is_empty(self):
        return self.queueLen == 0

    def is_full(self):
        return self.queueLen == self.size

    def insert(self, item):
        if self.is_full():
            raise Exception("queue is over flow")
            return
        else:
            return self.queue.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("queue is empty")
            return
        else:
            return self.queue.remove(self.queue[0])

    def show(self):
        print (self.queue)

data=Queue(5)
data.show()
data.insert(1)
data.show()
data.insert('a')
data.show()
data.insert(2)
data.show()
data.insert('b')
data.show()
data.insert(3)
data.show()
data.insert(4)
data.show()
data.insert(5)
data.show()

