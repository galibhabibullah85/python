"""
type() => Prints the Data type;

print() => Prints Data;

len() => Prints the length of any data;

input() => Same as prompt() in Javascript;

zip(X1,X2,...Xn) => Zips all the 'X' Variables by their Values.Example starts at line 568;

.split("anything"/" "/EMPTY) => To split any joined data type by "anything" or " "{space} or by Comma{EMPTY};

#.....................................................
.join("anything"/" ") => To join any split data type by "anything" or only " "{space};
#......................................................

range(Num Value1 , Num Value2 , Num Value3) => Outputs Numbers from Num Value1 to Num Value2 by the difference of Num Value3 in a Dictionary data type;By default Num value1 is ZERO;

#.........................Data casting...............#
int() => Turns any data type into Integer data type;
float() => Turns any data type into Float data type;
str() => Turns any data type into String data type;
tuple() => Turns any data type into Tuple data type;
list() => Turns any data type into a List data type;
set() => Turns any data type into Set data type;
dict() => Turns any data type into Dictionary data type;

#...........Function in PYTHON............#
def function name(Parameter):
	code.....
function name(Parameter) #Function call

#.............Lambda Functions in PYTHON............#
Variable = lambda Parameter/Argument:Code/Expression...
print(Variable(Parameter/Argument))

// filter(Lambda Function with Condition as a first Parameter,Variable of any data type or only any data type as a second Parameter) => Checks all the values of the Variable with the condition of Lambda Function and then Prints it.**Must be in the same method of the data type of the Variable**;

// map(Lambda Function with or without Condition as a first Parameter,Variable of any data type or only any data type as a Parameter as many as times) => Checks all the values of the Variable with the condition of Lambda Function and then Prints only BOOLEN or any Expression.**Must be in the same method of the data type of the Variable**;

// reduce(Lambda Function with or without Condition as a first Parameter,Variable of any data type or only any data type as a second Parameter) => Returns only one single Value after applying the Expression of the Lambda Function.**Always have to import{from functools import*} for using this method**;

#.................Condition in PYTHON.........#
if Condition:
	Code....
		elif Condition:
			Code....
				else:
					Code...
					break

#...............Looping in PYTHON............#
for x in Variable/Range of Variable:
	print(x)


for x in range(m,n):  #Loops from the specified								  Number 'm' to the rest of 							  'n';Mathematical operations can be 						applied here;
	print(x)


i = 0 #Must needed for Condition
while Condition{i < len(v)}:
	Code.....
	{
	print(v[i])
	i = i + 1   #i += 1
	}

#........................Turnury Expression...............
num1 = m
num2 = n
x = num1 if num1{Any Condition}num2 else num2

"""


"""...............Number Data type......................"""  #Same as comment

x = 10
print(type(x)) #integer


x = 10.223
print(type(x)) #float


x = 10j 
print(type(x)) #complex


x = 1 < 10     #boolen
print(type(x))
print(x)       #True


x = 1 > 10     #boolen
print(type(x))
print(x)       #False

""".............Mathemetical operator"""
# + , - , * , / , %
# // => Returns the rounded figure of /(Division);
# ** => To the power;
#{x'Mathemetical operator'= Value} => {x = x 'Mathemetical operator' Value};

""".............Logical Operators"""
# == , != , < , > , <= , >=
#Condition "and" Condition
#Condition "or" Condition
#"not"(Condition and Condition)
#"not"(Condition or Condition)

"""..............Membership Operator"""
# in => Prints Boolen if there exists or not exists the same value in the specified Variable;{ x in y => Means 'x' is inside of 'y' where 'x' and 'y' can be any data type};

# not in => Opposite of "in";


"""...............String Data type....................."""

"""
**x[n] => Accesses any specified INDEX 'n' of any String  data type named 'x';
if(n > 0){Starts counting INDEX from first};
elseif(n > 0){Starts counting INDEX from last};

**x[m:n] => Accesses String data type from the specified
INDEX 'm' to the rest of INDEX 'n';There may cause wirred result when 'm' or 'n' or both are Nagetive;

.upper() => Transform everything to UPPERCASE of **'String'**;

.lower() => Transform everything to lowecase of **'String'**;
"""

x = "Galib"
y = 'Mostofa'
print(type(x))
print(type(y))

print(len(x))
print(len(y))

print(x[0])  #For printing the string with specific INDEX
print(y[5])  #Can't change any string with specific INDEX 				like this, y[5] = "d"

print(x[-1])
print(y[-5]) #Starts counting INDEX from last

print(x[1:3])
print(y[0:5])

print(x[3:-1])
print(y[-5:-3])


"""...............List(means Array) Data type....................."""

#Basic structure of List:
# Name = [Num Value,"String Value",'String Value',[List]]

"""
**x[n] => Accesses any specified INDEX 'n' of any List(means Array) data type named 'x';
if(n > 0){Starts counting INDEX from first};
elseif(n > 0){Starts counting INDEX from last};

**x[m][n] => For accessing and adding value in a List inside of any List;

**x[m:n:o] => Accesses List data type from the specified
INDEX 'm' to the rest of INDEX 'n' by the difference of "o";There may cause wirred result when 'm' or 'n' or both are Nagetive;

.append("String"/Num) => Inserts value from last in any List;

.extend([Values more than one]) => Inserts multiple Values in the last of any List;

.insert('n' , "String"/Num) => Inserts value in the 'n'th INDEX in any List;

.pop(n) => Removes the 'n'th INDEXED Valuse of any List data type;When 'n = NOTHING' it removes Value from the last;

.reverse() => For printing values reversely of any List;
.sort()/sorted() => For printing Number values by sorting of any List;

.remove('Value available in the List') => Removes the value from the List that is argumented in the Parametre of this function;

x = y.copy() => Copies all the Values of 'y' to 'x' as a List;

.clear() => Clears everything from any List;
"""

x = ["in","bd",'as',5,2]
print(x)
print(x[4])#Prints 2
print(x[-2])#Prints 5
print(x[0:3])#Prints ["in","bd",'as']
print(x[0:-3])#Prints ["in","bd"]
print(x[1:-2])#Prints ["bd",'as']
print(x[-2:-1])#Prints [5]

x = [0,1,2,3,4,5,5,6]
print(x[0:7:1])#Prints [0, 1, 2, 3, 4, 5, 5]
print(x[0:7:-1])#Prints [5, 5, 4, 3, 2, 1, 0]
print(x[0:7:2])#Prints [0, 2, 4, 5]
#.....Prints from Index 0(Value 0) to the rest of Index 7(Value 5) but not the 7th Indexed Value by the difference of 1 & 2

x[2]="Ss"  #For updating List value
print(x[2])


x.append(123)
print(x)

x.extend([129 , 293])
print(x)

x.insert(1 , 596)
print(x)

x.insert(-3 , "str")
print(x)

x.pop()
print(x)
print(x.pop())

x.pop(3)
print(x)
print(x.pop(3))

"""...............Dictionary(means Object) Data type....................."""

"""...................Basic structure of Dictionary:"""
# Name = {
# 	"Key":"Value" ,
# 	"Key":"Value" , 
# 	"Key":["Value", "Value"] , 
# }

"""
# **Nota Bene**Keys and Values can be String or Num but Keys have to be UNIQUE.#


#....................Adding item in any Dictionary:

Variable with Dictionary data type["Key{different from the keys of the Dictionary that already exixts}"] = "Value"
"""


"""
#....................Updating item in any Dictionary:

Variable with Dictionary data type["Key{the key that already exixts in the Dictionary}"] = "Value"
"""


"""
.get("Key")/x["Key"] => For accessing the Value by the Key;
.keys() => Accesses all the Keys of any Dictionary;
.values() => Accesses all the Values of any Dictionary;
.items() => Accesses all the Keys along with Values of any Dictionary;

.pop("Key") => Removes the specified Key of any Dictionary data type;When there is no parametre,it removes the last Key;

.popitem() => Removes the last Key along with the Value of any Dictionary;

del Dictionary name['Key'] => Deletes the specified Key along with the Value of any Dictionary;

.clear() => Clears everything from any Dictionary;
"""


x = {
		  1:256,
		  2:"Galib",
	"third":"Mostofa"
}
print(x)

"""For accessing any Value by Key"""
print(x.get(2))
print(x[2])


x["third"] = "Value" #For updating Dictionary Value
print(x)

x['four'] = "BAC" #For adding Dictionary Value with Key
print(x)


"""........................Nested Dictionaries"""
Company_info = {"Employees":
				{'Galib':{'Job_type':"Student",'ID':123}
				,'Khadija':{'Job_type':"Student",'ID':123}}
				}
print(Company_info)
print(Company_info.items())



"""...............Tuple Data type....................."""

#Basic structure of Tuple:
# Name = (Num Value,"String Value",'String Value')

"""
**The Values of TUPLE can not be changed**
"""

#x[n] => Accesses any Value by INDEX
#x[m:n] => Accesses any Value from INDEX 'm' to the rest of INDEX 'n';In both the cases {-Infinity < m,n < Infinity} but Recommendation is to use Positive togetherly;

#x.count("Value") => Counts how many Values are available similar to the Values of any TUPLE named "x"; 

x = (10 , 20 , "Ami" , 20)

print(x)
print(x[2])
print(x[0:2])

print(x.count(20))
print(x.count("20"))
print(x.count("ami"))

x = (
	('a','b','c'),
	("abc","bcd","cde"),
	(1,2,3))

print(x)
print(x[2])
print(x[:2])
print(x[2:])
print(x[0:2])

"""...............Set(same as Higher Math's SET) Data type....................."""

#Basic structure of Tuple:
# Name = {Num Value,"String Value",'String Value'}

#**Set data type can not be called like this "x[INDEX]" because they don't have INDEXes and so the Values can not be changed.Set data type don't except DUPLICATED Values.Set data types are ordered randomly.**#

"""
.add(Num Value,"String Value",'String Value') => Adds value at the last of any Set data type;

.remove(Num Value,"String Value",'String Value') => Removes the argumented/specified value of any Set data type;

.union(Variable with Set data type) => Combines 2 Set data types;

.intersection(Variable with Set data type) => Intersects 2 Set data types;

.difference(Variable with Set data type) => For getting the difference between 2 Set data types;
"""
Name = {23,"asis",'fana'}
print(Name)


print(range(11))
print(list(range(10,12)))

"""Set Concatination"""
x = {3,4,56,7,7}
y = {'a','s','v'}
z = x , y
print(z)

x = {1,2,3,4}
y = set([3,4,5,6])
print(x | y) #Prints {x U y}(UNION)
print(x & y) #Prints {x /\ y}(INTERSECT)
print(x - y) #Prints {x / y}(MINUS the same values of 'y' from 'x')


"""
The difference between LIST & ARRAY is that LIST can contain all data types togetherly.But ARRAY can only contain a specified data type.So Mathmetical Operators can not be appiled in LIST but can be appiled in ARRAY.For using ARRAY,A MODULE needs to be imported.
""" 

"""
The MODULES insertion for ARRAY =>

import array
import array as arr(Most common and appropiate)
from array import*(Most easy)

"""

#Basic structure of Array:
# Name = array.array/arr.array/array('Data type',[Num Value,"String Value",'String Value'])

"""
**x[n] => Accesses any specified INDEX 'n' of any Array data type named 'x';
if(n > 0){Starts counting INDEX from first};elseif(n > 0){Starts counting INDEX from last};

**x[m:n] => Accesses Array data type from the specified
INDEX 'm' to the rest of INDEX 'n';There may cause wirred result when 'm' or 'n' or both are Nagetive;

.append("String"/Num) => Inserts only one value in the last of any Array;

.extend([Values more than one]) => Inserts multiple Values in the last of any Array;

.insert('n' , "String"/Num) => Inserts value/values in the 'n'th INDEX of any Array;

.pop(n) => Removes the 'n'th INDEXED Valuse of any Array data type;When 'n = NOTHING' it removes Value from the last;

.remove('Value available in the Array') => Removes the value from the Array that is argumented in the Parametre of this function;
"""
from array import*

x = array('i',[12,3,4,56,7,8])
print(x)
print(x[2])
print(x[-3])
print(x[0:3])
print(x[-2:-1])

print(len(x))

x.append(12569)
print(x)

x.extend([129 , 293])
print(x)

x.insert(3 , 1569)
print(x)

x.pop()
print(x)
print(x.pop())

x.pop(3)
print(x)
print(x.pop(3))

x.remove(4)
print(x)

""".............Array Concatination................"""
a = array('d',[12,3,4,5,78])  #Here 'd' for DECIMAL 
b = array("d",[1,2,33,5,7,4])
c = array('d')

c = a + b
print(c)

""".............Array Looping............."""
j = array("i",[1,2,33,5,7,4])

"""i = 0
while i >= 0:  #Infinite Looping
	print(j)
	i = i + 1"""

for x in range(1,10):
	print(x)

w = 19
for x in range(180,w*10):
	print(x)

for x in j:
	print(x)

for y in j[2:-1]:
	print(y)


v = array("f",[1,2,33,5,7,4])
i = 0
while i < len(v):
	print(v[i])
	i = i + 1 #i += 1

#...........................................................
from random import* #For using all Functions from random Package

c = 20 * random()  #random() => Generates Float Numbers from 0 to 1
print(int(c) + 1)  #For printing Random number from 0 to 					20 but not the 0

x = randint(1,6) #randint(x,y) => Generates Integer from x to y
print(x)


""".............File handling............."""

"""
**For handling file,we have to import "os" module

import os
"""

"""
open("filename with extension" , mode) => File handling;
Here >>
mode = 'r'(for reading only but returns error if the file does not exist),
'w'(for writing only but creates a new file if it does not exist;this mode will replace all the existing texts with the new one),
'a'(for appanding or adding any file at the end of another but creates a new file if it does not exist;this mode does not replace the existing texts with the new one rather it adds everything at the last),
'x'(creates a new file but returns error if the file already exists),
't'(Text mode),

File containing Variable name.read() => Reads any file with 'r'mode;

File containing Variable name.read(n) => Reads only 'n' characters of any file with 'r'mode;

File containing Variable name.readline() => Reads by the line of any file with 'r'mode;

File containing Variable name.readline(n) => Reads only 'n' line of any file with 'r'mode;

File containing Variable name.write("Texts wanted to be written") => Writes texts in any file with 'a' or 'w'mode;

os.path.exists("Path or File name") => For checking existance of any file;

os.remove("File name") => Removes any File;

os.rmdir("Folder name") => Removes any Folder;
"""

#......Function in PYTHON.........#
def abc(w,t,u):
 d = w + t + u
 print(d) 
abc(1,61,1)

def greeding(name):
	print("Hello "+name)
greeding("Mostofa")


"""............Lambda Function in PYTHON........."""
x = lambda a: a*a
print(x(9))

x = lambda a,b: a*b
print(x(9,3))

#.........Lambda function in another Function
def A(x):
	return(lambda y: x * y)
B = A(4)
print(B(3))

#.........filter() method in Lambda Function
x = [1,2,3,4,5,6]
new_x = list(filter(lambda a:(a/3==2),x))
print(new_x)

new = list(filter(lambda a:(a/3==2) , [1,2,3,4,5,6]))
print(new)  #Same result as before


#.........map() method in Lambda Function
x = [1,2,3,4,5,6]
new_x = list(map(lambda a:(a/3==2),x))
print(new_x)

new = map(lambda a:(a/3==2) , [1,2,3,4,5,6])
print(list(new))  #Same result as before

set_var = set(map(lambda x,y:x*y,{1,2,3,4,5},{5,4,3,2,1}))
print(set_var)

#.........reduce() method in Lambda Function
from functools import*

x = [1,2,3,4,5,6]
new_x = reduce(lambda a,b:a+b,x)
print(new_x)

new = reduce(lambda a,b:a+b , [1,2,3,4,5,6])
print(new)  #Same result as before


#....................................................
c = map(lambda x:x+x,filter(lambda a:(a/3==2) , [1,2,3,4,5,6]))
print(set(c))

c = filter(lambda x:(x<12),map(lambda a:a*3 , [1,2,3,4,5,6]))
print(set(c))

c = reduce(lambda x,y:x+y,filter(lambda x:(x<12),map(lambda a:a*3 , [1,2,3,4,5,6])))
print(c)

c = reduce(lambda x,y:x+y,map(lambda x:x+x,filter(lambda a:(a/3==2) , [1,2,3,4,5,6])))
print(c)


#....................................................

x = "I am Galib"
y = x.split(" ")
print(list(y))

x = "I_am_Galib"
y = x.split("_")
print(list(y))


"""...............zip Function...................."""

x = [1,2,3]
y = ['one','two','three']
z = set(zip(x,y))
print(z)

x = [1,2,3,4]
y = ['one','two','three']
z = set(zip(x,y))
print(z)

x = [1,2,3]
y = ['one','two','three','four']
z = set(zip(x,y))
print(z)

c = set(zip(*z)) #For unziping
print(c)

x = int(input("Please put a number here: "))
print("You have put ",x)