class myarray:
    '''123456'''
    def __isnumber(self,n):
        if not isinstance(n,(int,float,complex)):
            return 0
        return 1
    def __init__(self,*args):
        if not args:
            self.__value=[]
        else:
            for i in args:
                if not self.__isnumber(i):
                    print('suo you shi shu zi')
                    return
            self.__value=list(args)
    def __del__(self):
        del self.__value
    def __add__(self,n):
        if self.__isnumber(n):
            b=myarray()
            b.__value=[item+n for item in self.__value]
            return b
        elif isinstance(n,myarray):
            if len(n.__value)==len(self.__value):
                c=myarray()
                c.__value=[i+j for i,j in zip(self.__value,n.__value)]
                return c
            else:
                print('fafa')
        else:
            print('bu zhi chi')
    def __sub__(self, n):
        if not self.__isnumber(n):
            print('not ok')
            return
        b=myarray()
        b.__value=[item-n for item in self.__value]
        return b
    def __mul__(self, n):
        if not self.__isnumber(n):
            print(250)
            return
        b=myarray()
        b.__value=[item*n for item in self.__value]
        return b
    def __truediv__(self, other):
        if not self.__isnumber(other):
            print('not ok')
            return
        b=myarray()
        b.__value=[items /other for items in self.__value ]
        return b
    def __floordiv__(self,n):
        if not isinstance(n,int):
            print('250')
            return
        b=myarray()
        b.__value=[item//n for item in self.__value]
        return b
    def __mod__(self, other):
        if not self.__isnumber(other):
            print('ss')
            return
        b=myarray()
        b.__value=[item %other for item in self.__value]
        return b
    def __pow__(self,n):
        if not self.__isnumber(n):
            print(250)
            return
        b=myarray()
        b.__value=[item**n for item in self.__value]
        return b
    def __len__(self):
        return len(self.__value)
    def __repr__(self):
        return repr(self.__value)
    def append(self,v):
        if not self.__isnumber(v):
            print(250)
            return
        self.__value.append(v)
    def __getitem__(self, index):
        length=len(self.__value)
        if isinstance(index,int)and 0<=index<length:
            return self.__value[index]
        elif isinstance(index,(list,tuple)):
            for i in index:
                if not (isinstance(i,int)and 0<=i<length):
                    return '555'
                result=[]
                for i in index:
                    result.append(self.__value[i])
                    return result
                else:
                    return '250'

    def __setitem__(self, key, value):
        length=len(self.__value)
        if isinstance(key,int)and 0<=key<length:
            self.__value[key]=value
        elif isinstance(key,(list,tuple)):
            for i in key:
                if not(isinstance(i,int)and 0<=i<length):
                    raise Exception('1234')
            if isinstance(value,(list,tuple)):
                if len(key)==len(value):
                    for i ,v in enumerate(key):
                        self.__value[v]=value[i]
                else:
                    raise Exception('113')
            elif isinstance(value,(int,float,complex)):
                for i in key:
                    self.__value[i]=value

            else:
                raise Exception('affaf')
        else:
            raise Exception('dadas')
    def __contains__(self, item):
        if item in self.__value:
            return 1
        return 0
    def dot(self,v):
        if not isinstance(v,myarray):
            print(v,'affafsafs')
            return
        if len(v)!=len(self.__value):
                print(134)
                return
        return sum([i*j for i , j in zip(self.__value,v.__value)])
    def __eq__(self, v):
        if not isinstance(v,myarray):
            print('afffd')
            return 0
        if self.__value==v.__value:
            return 1
        return 0
    def __lt__(self, v):
        if not isinstance(v,myarray):
            print('bdbg')
            return 0
        if self.__value<v.__value:
            return 1
        return 0
if __name__=='__main__':
    print("asffdasf")

