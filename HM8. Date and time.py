from datetime import datetime
print("Problem#1")
x = 20160305
x = str(x)
dt = datetime.strptime(x, '%Y%m%d')
print(dt)
print("Problem#2")
day = '25'
month = '2'
year = '2016'
dat = datetime.strptime(day+month+year, '%d%m%Y')
print(dat)
print('Problem#3')
st = '01/05/2016'
datestr = datetime.strptime(st, '%d/%m/%Y')
print(datestr)
print('Problem#4')
today = datetime.today()
print(today)
a = today.replace(year=(today.year+1), month=(today.month-1))
print(a)
c = a.replace(month=1, day=1)
print(c)
b = (a-c)
print(b)

