class root:
    __total=0
    def __init__(self,value):
        self.__value=value
        root.__total+=1

    def show(self):
        print(self.__value)
        print(self.__total)
   # @classmethod
    def classshowtotal(cls):
        print(cls.__total)
  #  @staticmethod
    def staticshowtotal():
        print(root.__total)
  #  @property
 #   def value(self):
#        return self.__value

    def __set(self,v):
        self.__value=v
    def __get(self):
        return self.__value
    
    
    def __del(self):
        del self.__value
    value=property(__get,__set,__del)
