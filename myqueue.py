class myqueue:
    def __init__(self,size=10):
        self._content=[]
        self._size=size
        self._current=0
    def __del__(self):
        del self._content
    def setszie(self,size):
        if size<self._current:
            for i in range(size,self._current)[::-1]:
                del self._content[i]
            self._current=size
        self._size=size
    def put(self,v):
        if self._current<self._size:
            self._content.append(v)
            self._current=self._current+1
        else :
            print('full')
    def get(self):
        if self._content:
            self._current=self._current-1
            return self._content.pop(0)
        else :
            print('empty')
    def show(self):
        if self._content:
            print(self._content)
        else :
            print('empty')
    def empty(self):
        self._content=[]
        self._current=0
    def isempty(self):
        if not self._content:
            return 1
        else:
            return 0
    def isfull(self):
        if self._current==self._size:
            return 1
        else:
            return 0
if __name__=='__main__':
    print('queue')
