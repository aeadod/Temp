class bitree:
    def __init__(self,value):
        self.__left=None
        self.__right=None
        self.__data=value
    def __del__(self):
        del self.__data
    def insertleftchild(self,value):
        if self.__left:
            print('left already ')
        else:
            self.__left=bitree(value)
            return self.__left
    def insertrightchild(self,value):
        if self.__right:
            print('right already')
        else:
            self.__right=bitree(value)
            return self.__right
    def show(self):
        print(self.__data)
    def preorder(self):
        print(self.__data)
        if self.__left:
            self.__left.preorder()
        if self.__right:
            self.__right.preorder()
    def postorder(self):
        if self.__left:
            self.__left.postorder()
        if self.__right:
            self.__right.postorder()
        print(self.__data)
    def inorder(self):
        if self.__left:
            self.__left.inorder()
        print(self.__data)
        if self.__right:
            self.__right.inorder()
if __name__=='__main__':
    print('ok')
