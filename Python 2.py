#......................................................
from turtle import Turtle,speed,forward

# x = Turtle()
# x.speed(1)

# def square():
#     x.forward(50)

#     x.right(90)
#     x.forward(50)

#     x.right(90)
#     x.forward(50)

#     x.right(90)
#     x.forward(50)

# y = Turtle()
# y.speed(1)

# square()
# y.forward(100)

# x.forward(0)
# square()
# z = Turtle()
# z.speed(1)
# z.right(-90)
# z.forward(100)

# x.forward(0)
# square()
# w = Turtle()
# w.speed(2)
# w.right(180)
# w.backward(-100)

# x.forward(0)
# square()
# s = Turtle()
# s.speed(1)
# s.right(90)
# s.forward(100)

class tur:
    def __init__(self,spd,fwd,rt):
        self = Turtle()
        sp = spd
        fw = fwd
        r = rt

    def square(self,spd1,fwd1,rt1):
        self.forward(fwd1)
        self.speed(spd1)

        self.right(rt1)
        self.speed(spd1)
        self.forward(fwd1)

        self.right(rt1)
        self.speed(spd1)
        self.forward(fwd1)

        self.right(rt1)
        self.speed(spd1)
        self.forward(fwd1)

    square(sp,fw,r)


x = tur(1,100,0)
# y = tur(1,100,90)
# z = tur(2,100,180)
# d = tur(2,100,270)
"""x.process(1,100,0)
x.process(1,100,90)
x.process(2,100,180)
x.process(2,100,270)"""

#........................................................
"""import calendar

print(calendar.weekheader(3))#Prints the days of a week
print(calendar.weekheader(2))

print(calendar.firstweekday())#Prints the INDEX of the first day of the week

print(calendar.month(2021 , 1))#Prints the specified month

print(calendar.monthcalendar(2021 , 1))#Prints the specified month as a multidimentional Array

print(calendar.calendar(2021))#Prints the whole calendar

print(calendar.weekday(2021 , 1 , 2))#Prints the INDEX of the specified day of the week

print(calendar.isleap(2020))#Prints boolean for any year if it is Leap year or not
print(calendar.isleap(2021))"""

#.......................................................
"""from datetime import*

x = date(2021, 9, 12) #date(Year,Month,Day)
print(x)

x = time(10,10,10,10) #time(Hour,Minute,Secend,Microsecend)
print(x)

x = datetime(2021,9,12,10,10,10,10) #datetime(Year,Month,Day,Hour,Minute,Secend,Microsecend)
print(x)
print(datetime.now()) #Prints the current date and time as an object instead of manually printing.

y = date.today()
print(y)  #Printing today's date
print(y.day)  #Printing today's date(only day)
print(y.weekday())  #Printing today's weekday's Index(the Index of today in normal week)

#Indexes of all weekdays:
# Monday = 0, Tuesday = 1, Wednessday = 2, Thursday = 3, Friday = 4, Saturday = 5, Sunday = 6

x = date(2021, 9, 12) #date(Year,Month,Day)
print(x)

z = x - y
print(z) #Printing the subtracted date as an Object
print(z.days)  #Printing the subtracted date as a String

x = timedelta(days = 10)
print(x)
print(y - x)

x = timedelta(hours = 10)
print(x)
print(y - x)

a = date.today().strftime('%B %d,%Y') #strftime => String FORMATING time
print(a) #Prints Month_name(%B) Day(%d) ,Year(%Y)

b = datetime.strptime(a,'%B %d,%Y') #strptime => String PARSING Time
print(b)
print(repr(b))

d = datetime.strptime('March 08,2028','%B %d,%Y')
print(d) #Same output as the first one

"""
