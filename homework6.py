from abc import ABCMeta
class abc():
    __metaclass__ = ABCMeta
    x = 0



class A(abc):

    x = int(input("Please write number from 1 to 9:"))

    def __init__(self):

        if A.x in range(1, 4):
            print(self.func())
        elif A.x in range(4, 7):
            print(self.func1())
        elif A.x in range(7, 10):
            print(self.func2(self.x))
        else:
            print("Error")

    def func(self):
        s = str(input("Please write something:"))
        n = int(input("Please write how many times you want your 'something' to be repeated:"))
        for _str_rep in range(0, n):
            _str_rep = s
            print(_str_rep)
    def func1(self):
        m = int(input("Please write the degree you want your number to be put in:"))
        return print(self.x**m)
    def func2(self,x ):
        b = [x for x in range(x, x+10)]
        return print(b)

class Child(A):
    def __init__(self):
        super(Child, self).__init__()

c = Child()


# print("Problem#2")  # Second problem started
# print("The society in the 21st century")

class B(object):

    age = int(input("Can you tell me your age,please?"))

    def __init__(self):
        if B.age in range(0, 8):
            print(self.f())
        elif B.age in range(7, 18):
            print(self.fu())
        elif B.age in range(18, 26):
            print(self.fun())
        elif B.age in range(25, 61):
            print(self.func())
        elif B.age in range(60, 121):
            print(self.funct())
        else:
            print(self.functi())

    def f(self):
        print("Kinder-garden, I am sorry")

    def fu(self):
        print("School,dude")

    def fun(self):
        print("College, dude. Though, you can start dating")

    def func(self):
        print("Gotta work hard for it")

    def funct(self):
        print("Retirement awaits, and death too")

    def functi(self):
        for _er in range(0, 5):
            _er = "Error"
            print(_er)
        print("I am sorry, because of our policy aliens can not use this program. \
        Though, you can always try ageforaliens.py")

class Child(B):
    def __init__(self):
        super(Child, self).__init__()

d = Child()
