class stack(object):
    def __init__(self,size):
        self.data=[[]]*size
        self.size=size
        self.top=-1
        
    def top(self):
        return self.data(self.top)

    def is_empty(self):
        return len(self.top==-1)

    def push(self,item):
        if self.top == self.size:
            raise Exception("Stack over flow")
            return
        else:
            self.top += 1
            self.data[self.top]=item

    def pop(self):
        if self.top == -1:
            raise Exception("Stack is empty")
            return
        else:
            X=self.data[self.top]
            self.top-=1

    def show(self):
        print (self.data)
data=stack(10)
data.push(1)
data.show()
data.push('a')
data.push('2')
data.push('b')
data.push('3')
data.push('c')
data.push('4')
data.push('d')
data.push('5')
data.show()
data.pop()
data.show()
