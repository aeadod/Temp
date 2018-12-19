class a():
    def __init__(self):
        self.__private()
        self.public()

    def __private(self):
        print('__private')
    def public(self):
        print('public')
    def __test(self):#si you 
        print('__test')

class b(a):
    def __private(self):
        print('B__private')
    def public(self):
        print("bpublic")

    
class c(a):
    def __init__(self):
        self.__private()
        self.public()
    def __private(self):
        print("C  __prvivate")
    def public(self):
        print('public c')
        
