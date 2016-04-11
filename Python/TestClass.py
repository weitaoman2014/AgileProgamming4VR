nation = 'China'

class Person:
    #member data:
    name = 'zh3'
    age = '123'
    sex = 'male'

    #member function:
    def __init__(self):
        pass

    def setName(self,name):
        self.name = name

    '''
    def __init__(self, name, age, sex):
        #print('hh')
        self.name = name
        self.age = age
        self.sex = sex
    '''

    def printName(self):
        print(self.name)
        print(self.age)
        print(self.sex)
        print(nation)

#object
'''
zhang3 = Person('1','2','3')
zhang3.printName() #printName(zhang3)

li4 = Person('li4','232','233')
li4.printName()
'''
zhang3 = Person()
zhang3.setName('setname')
zhang3.printName()

