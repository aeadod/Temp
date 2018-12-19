class person(object):
    def __init__(self,name='',age=20,sex='man'):
        self.setname(name)
        self.setage(age)
        self.setsex(sex)

    def setname(self,name):
        if not isinstance(name,str):
            print('afsf')
            self.__name=''
            return
        self.__name=name
    def setage(self,age):
        if type(age)!=int:
            print('gsasf')
            self.__age=20
            return
        self.__age=age

    def setsex(self,sex):
        if sex not in ('man','woman'):
            print('gdf')
            self.__sex='man'
            return
        self.__sex=sex
    def show(self):
        print(self.__name,self.__age,self.__sex)

class teacher(person):
    def __init__(self,name='',age=30,sex='man',department='Computer'):
        #super(teacher,self).__init__(name,age,sex)
        person.__init__(self,name,age,sex)
        self.setdepartment(department)
    def setdepartment(self, department):
        if type(department)!=str:
            print('sfs')
            self.__department='Computer'
            return
        self.__department=department

    def show(self):
        super(teacher,self).show()
        print(self.__department)
