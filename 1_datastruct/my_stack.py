class stack(object):
    def __init__(self,size=10):
        self.data=[]
        self.size=size
        self.top=-1
        
    def set_size(self,size):
        if self.top > size:
            raise Exception("Stack will over flow")
            return
        self.size=size

    def top(self):
        return self.data(self.top)

    def is_empty(self):
        return len(self.top==-1)

    def push(self,item):
        if self.top == self.size:
            raise Exception("Stack over flow")
            return
        else:
            self.data.append(item)
            self.top += 1

    def pop(self):
        if self.top == -1:
            raise Exception("Stack is empty")
            return
        else:
            return self.data.pop()
            
    def show(self):
        print self.data
data=stack()
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
data.push('e')
data.push('6')
data.show()
data.pop()
data.show()
