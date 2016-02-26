from homework3_package import modul
print("-------Problem#1&2&5. Homework3-------")
x = int(input("Please write number from 1 to 9:"))
if x in range(0, 4):  # First condition and outcomes for problem 1
    print(modul.func1())
if x in range(3, 7):  # Second condition and outcomes for problem 1
    print(modul.func2(x))
if x in range(7, 10):  # Third condition and outcomes for problem 1
   print(modul.func3(x))
if x > 10:
    print("Error")
    
print("-----------Problem#3. Homework3--------")


def func():
    some = input("Please write some string:").strip(" ")
    b = some.split(" ")
    for c in b:
        print(c, len(c))
func()
