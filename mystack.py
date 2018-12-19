class stack:
    def __init__(self,size=10):
        self._content=[]
        self._size=size
        self._current=0
    def __del__(self):
        del self._content
    def empty(self):
        self._content=[]
        self._current=0
    def isempty(self):
        return not self._content
    def setsize(self,size):
        if size<self._current:
            for i in range(size,self._current)[::-1]:
                del self._content[i]
            self._current=size
        self._size=size
    def isfull(self):
        return self._current==self._size
    def push(self,v):
        if self._current<self._size:
            self._content.append(v)
            self._current+=1
        else:
            print('full')
    def pop(self):
        if self._content:
            self._current=self._current-1
            return self._content.pop()
        else:
            print('empty')
    def show(self):
        print(self._content)
    def showremainderspace(self):
        print('stack can still push',self._size-self._current,'elements')
if __name__=='__main__':
    print('aaaaa')
