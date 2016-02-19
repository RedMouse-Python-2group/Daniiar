
class A:
    x = int(input("Please write number from 1 to 9:"))
    def __init__(self):
        self.x = self.x
    def func(self):
        s = str(input("Please write something:"))
        n = int(input("Please write how many times you want your 'something' to be repeated:"))
        for _str_rep in range(0, n):
            _str_rep = s
            return print(_str_rep)
    def func1(self):
        m = int(input("Please write the degree you want your number to be put in:"))
        return print(self.x**m)
    def func2(self,x ):
        b = [x for x in range(x, x+10)]
        return print(b)
a = A()
if a.x in range(1, 4):
    print(a.func())
elif a.x in range(4, 7):
    print(a.func1())
elif a.x in range(7, 10):
    print(a.func2())
else:
    print("Error")

print("Problem#2")  # Second problem started
print("The society in the 21st century")
_age = int(input("Can you tell me your age,please?"))
class B():
    def __init__(self):
        self._age = _age
        if _age in range(0, 8):
            print(self.f())
        elif _age in range(7, 18):
            print(self.fu())
        elif _age in range(18, 26):
            print(self.fun())
        elif _age in range(25, 61):
            print(self.func())
        elif _age in range(60, 121):
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
b = B()
print(b._age)
