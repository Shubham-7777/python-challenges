"""
Question 1
Level 1
Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
Consider use range(#begin, #end) method
"""
from builtins import int

"""
list_1 = []
for i in range(2000,3201):
    if (i % 7 == 0) and (i % 5 != 0):
        list_1.append(i)
print(list_1)
"""
"""
Question 2
Level 1
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
"""
num = int(input("Enter the value to factorize:- "))
factorial = 1
if num <= 0:
    print("Unable the factorize coz the value is 0 or negative")
elif num > 0:
    for i in range(1, num + 1):
        factorial = factorial * i
print(f"The factorial of {num} is {factorial}")"""
"""
Question 3
Level 1
Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral
number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
Consider use dict()
"""
"""
num = int(input("Enter the value "))
d = {}
print(type(d))
for i in range(1 , num + 1):
    d[i] = i * i
print(d)
"""
"""
Question 4
Level 1
Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which 
contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple
"""
"""
values = input("Enter the numbers:- ")
list_1 = values.split(',')
print(list(list_1))
print(tuple(list_1))
"""
"""
Question 5
Level 1
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
"""
"""
class Print():
    def __init__(self,a):
        self.a = a
    def get_string(self):
        self.a = input("Enter the string:- ")
        print(self.a)
    def print_string(self):
        print(self.a.upper())
obj_1 = Print(a = "nouse")
obj_1.get_string()
obj_1.print_string()
"""
"""
Question 6
Level 2

Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24

Hints:
If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output 
received is 26.0, it should be printed as 26)
In case of input data being supplied to the question, it should be assumed to be a console input. 
"""
"""def practice():
    C = 50
    H = 30
    Q = 0
    values = input("Enter the values:--  ")
    l = values.split(",")
    for i in range(0, len(l)):
        l[i] = int(l[i])
    print(l)
    for i in range(0,len(l)):
        ans_1 = (2 * C * l[i])
        print(type(ans_1))
    Q = Square root of [(2 * C * D)/H]
practice()"""
"""def practice():
    C = 50
    H = 30
    Q = 0
    b = []
    ans = 0
    
    values = (input("Enter the values:-- "))
    a = values.split(",")
    for i in range(0, len(a)):
        a[i] = int(a[i])
    print(a)
    for i in range(0,len(a)):
        Q = (2 * C * a[i]) / H
practice()
#Solution
import math
c=50
h=30
value = []
items=[x for x in raw_input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print ','.join(value)
"""
"""
Question 7
Level 2

Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a 
console input in a comma-separated form.
"""
"""value_1 = input("Enter the values:- ")
a = value_1.split(",")
row = a[0]
column = a[1]
max_list = []"""
"""input_str = input("Enter teh value:-- ")
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = []"""
#Solution
"""
values_1 = input("Enter the value:-- ")
a = [int(i) for i in values_1.split(",")]
rownum = a[0]
columnnum = a[1]
multilist = [[0 for col in range(columnnum)] for row in range(rownum)]

for row in range(rownum):
    for col in range(columnnum):
        multilist[row][col] = row*col

print(multilist)
"""
"""
Question 8
Level 2
Question:
Write a program that accepts a comma separated sequence of words as input and
prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
"""
def function():
    list_1 = [x for x in input("Enter the list of strings:-- ").split(",")]
    list_1.sort()
    print(list_1)
    new_list = ",".join(list_1)
    print(new_list)
function()
"""
"""
Question 9
Level 2

Question£º
Write a program that accepts sequence of lines as input and prints the lines after making all 
characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
"""def input_lines():
    no_of_lines = 3
    for i in range(no_of_lines):
        a = input("Enter")
        print(a.upper())
input_lines()
"""
"""
Question 10
Level 2

Question:
Write a program that accepts a sequence of whitespace separated words as input and 
prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.
"""
"""
def function_1():
    s = {}
    list_2 = []
    list_3 = []
    str_1 = input("Enter the values:-- ")
    list_1 = (str_1.split(" "))
    s = set(list_1)
    list_2 = list(s)
    list_2.sort()
    print(list_2)
    join_1 = " "
    list_3 = join_1.join(list_2)
    print(list_3)
function_1()
"""
"""
Question 11
Level 2

Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether 
they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001e
Then the output should be:
1010
Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
"""#123,456,978
def list_numbers():
    list_1 = [int(i) for i in input("Enter the list strings== ").split(",")]
    for j in list_1:
        print(type(list_1[j]))
list_numbers()"""
"""
Question 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the 
number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
"""list_1 = []
for i in range(1000,3001):
    if i % 2 == 0:
      s = str(i)
      list_1.append(s)
    else:
        pass
print(",".join(list_1))
"""
"""
Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
    """
"""def function_1():
    list_1 =[]
    d = {}
    int_1 = 0
    letters = 0
    blankspace = 0
    data = input("Enter the data:== ")
    for i in data:
        if i.isnumeric():
            int_1 += 1
        elif i.isalpha():
            letters += 1
        elif i.isspace():
            blankspace += 1
        else:
            print("Invalid input")
    print("Numbers", int_1)
    print("Letters", letters)
    print("blankspace", blankspace)

function_1()"""
"""
Question 14
Level 2

Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
"""def function_1():
    d = {"Upper Case":0,"Lower Case":0}
    data = input("Enter the data:-- ")
    for i in data:
        if i.isupper():
            d["Upper Case"]+=1
        elif i.islower():
            d["Lower Case"]+=1
    print(d)
    print("UpperCase", d["Upper Case"])
    print("LowerCase", d["Lower Case"])
function_1()
"""
"""
Question 15
Level 2

Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
"""
def function_1():
    a = int(input("Enter the value:- "))
    val_1 = int("%s"% a)
    val_2 = int("%s%s"%(a,a) )
    val_3 = int("%s%s%s"%(a,a,a) )
    val_4 = int("%s%s%s%s"%(a,a,a,a) )
    ans = val_1 + val_2 + val_3 + val_4
    print(ans)
function_1()
"""
"""
Question 16
Level 2

Question:
Use a list comprehension to square each odd number in a list. 
The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
"""
def function_1():
    a = input("Enter the value")
    list_1 = [(i) for i in a.split(",") if int(i) % 2 != 0]
    print(",".join(list_1))
function_1()
"""
"""
Question 17
Level 2

Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The 
transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
"""
def function_1():
    d = 0
    while True:
        a = input("Select the Choice:-- D/d to deposit, W/w to withdraw or exit e :-- ")
        if a == "D" or a == "d":
            deposit = int(input("Deposit:-- "))
            d = d + deposit
        elif a == "W" or a == "w":
            withdraw = int(input("Withdraw:-- "))
            d = d - withdraw
        elif a == "E" or a == "e":
            print("Exiting")
            break
    print("balance",d)
function_1()
"""
"""
def function_1():
    amount = 0
    values = 0
    while True:
        input_1 = input("Enter the value or exit press e:-- ")
        if input_1 == "":
            break
        else:
            data = input_1.split(" ")
            task = data[0]
            values = int(data[1])
        if  task == "d" or task == "D":
            amount += values
        elif task == "w" or task == "W":
            amount -= values
    print("Balance",amount)

function_1()
"""
"""
Question 18
Level 3

Question:
A website requires the users to input username and password to register. 
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. 
Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1

Hints:
In case of input data being supplied to the question, it should be assumed to be a console in+put.
"""
"""
import re
def function_1():
    a = input("Enter the password:-- ")
    passwords = a.split(",")
    print(passwords)
    list_1 = []
    for i in passwords:
        if len(i) < 6 or len(i) > 12:
            continue
        elif not re.search("[a-z]",i):
            continue
        elif not re.search("[0-9]",i):
            continue
        elif not re.search("[A-Z]",i):
            continue
        elif not re.search("[$#@]",i):
            continue
        list_1.append(i)

    a = ",".join(list_1)
    print("Valid passwords",a)
function_1()
"""
"""
Question 19
Level 3
Question:
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, 
age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use itemgetter to enable multiple sort keys.
"""
"""
from operator import itemgetter, attrgetter
l = []
input_1 = input("Enter the input:-- ")
while True:
    if not input_1:
        break
    l.append(tuple(input_1.split(",")))
print(sorted(l, key=itemgetter(0,1,2)))
"""
"""
Question 20
Level 3

Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield
"""
"""
def function_1():
    a = int(input("Enter the range:-- "))
    b = int(input("Enter the value ned to divide:-- "))
    for i in range(0,a):
        if i % b == 0:
            yield i

for ans in function_1():
    print(ans)
"""
"""
Question 21
Level 3

Question£º
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT 
with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position 
after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
"""
import math
pos = [0,0]
while True:
    s = input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="u":
        pos[0]+=steps
    elif direction=="d":
        pos[0]-=steps
    elif direction=="l":
        pos[1]-=steps
    elif direction=="r":
        pos[1]+=steps
    else:
        pass

print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))
"""
"""
Question 22
Level 3

Question:
Write a program to compute the frequency of the words from the input. 
The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

Hints
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
"""
freq = {}

input_1 = input("Enter the statement:-- ")
list_1 = [i for i in input_1.split(" ")]
print(list_1)
for key in list_1:
    freq[key] = freq.get(key,0)+1
key = freq.keys()

for v in key:
    print((v,freq[v]))
print(freq)
"""
"""
Question 23
level 1

Question:
    Write a method which can calculate square value of number

Hints:
    Using the ** operator
"""
"""
import math
def function_1():
    ans_1 = 0
    ans_1_1 = 0
    input_1 = int(input("Enter the integer:-- "))
    for i in range(input_1):
        if i * i == input_1:
            ans_1 = i
        else:
            pass
    ans_2 = input_1**2
    print("Square_root using math",math.sqrt(input_1))
    print("Square_root",ans_1)
    print("Square",ans_2)
function_1()
"""
"""
Question 24
Level 1

Question:
Python has many built - in functions, and if you do not know how to use it, you can read document online or 
find some books. But Python has a built- in document function for every built- in functions.
Please write a program to print some Python built - in functions documents, such as abs(), int(), raw_input()
And add document for your own function

Hints:
The built - in document method is __doc__
"""
"""
print(input.__doc__)
print(int.__doc__)
print(str.__doc__)
def square():
    ans = 0
    input_1 = int(input("Enter the value:--  "))
    ans =  input_1**2
    print("ans")


print(square.__doc__)
print(print.__doc__)
square()
"""
"""
Question 25
Level 1

Question:
Define a class, which have a class parameter and have a same instance parameter.

Hints:
Define a instance parameter, need add it in __init__ method
You can init a object with construct parameter or set the value later
"""
"""
class School():
    city = "city_1"

    def __init__(self,school_name):
        self.school_name = school_name


    def teacher_details(self):
        list_1 = [i for i in input("Enter the Teachers name:-- ").split(",")]
        print(list_1)
        a = " "
        a = a.join(list_1)
        print(a)
        teachers = []
        for i in list_1:

            teachers.append(",".join(i))
            print(teachers)
            #print (f"Teachers name is {i}")
    def students_details(self):
        list_2 = [i for i in input("Enter the Students name:-- ").split(",")]
        print(list_2)
        b = " "
        b = b.join(list_2)
        print(b)
        students = []
        for i in list_2:
            students.append(" ".join(i))
            print(students)
            #print (f"Students name is {i}")
obj1 = School(school_name="ABC")
print("Name is ", obj1.school_name)
print("City is ",obj1.city)
obj1.teacher_details()
obj1.students_details()
"""
"""
a = "a bccxd ef"
split_1 = (a.split(" "))
print(split_1)
print(type(split_1))
s = ","
s = s.join(split_1)
print(s)
print(type(s))
"""
"""
Question:
Define a function which can compute the sum of two numbers.

Hints:
Define a function with two numbers as arguments. You can compute the sum in the function and return the value.
"""
"""
def function_1():
    input_1 = int(input("Enter value1:-- "))
    input_2 = int(input("Enter value2:-- "))
    ans = input_1 + input_2
    return ans
print(function_1())
"""
"""
Question:
Define a function that can convert a integer into a string and print it in console.

Hints:

Use str() to convert a number to string.
"""
"""
def function_1():
    input_1 = int(input("Enter int:-- "))
    print(input_1)
    print(type(input_1))
    a = str(input_1)
    print(a)
    print(type(a))
function_1()
"""
"""
Question:
Define a function that can receive two integral numbers in string form and compute their sum and then 
print it in console.

Hints:

Use int() to convert a string to integer.
"""
"""
def function_1():
    ans = 0
    input_1 = list(input("Enter the values:-- ").split(","))
    print("values",input_1)
    for i in range(len(input_1)):
        ans += int(input_1[i])
    print(ans)
function_1()
"""
#Extras till 893
"""
a = "asdfsa"
b = ",".join(a)
print(b)
print(type(b))
c = (list(b))
print(c)"""
"""

#Taking multiple inputs from user in Python
def function_1():
    x = list(map(int,input("Enter values :-- ").split(",")))
    print("values ",x)
function_1()
"""
#map example
"""
def function_2():
    for i in list_1:
       if i % 2 == 0:
           yie1d i
list_1 = [1,2,3,4,5,6,7,8,9]
for ans in function_2():
    print(ans)
result = (map(function_2,list_1))

print(function_2())
"""
"""
def addition(i):
    for i in list_1:
        if i % 2 == 0:
            yield i
for ans in addition(i):
    print(ans)

# We double all numbers using map()
list_1 = [1,2,3,4,5,6,7,8,9]
result = map(addition,list_1)
print(list(result))
"""
"""
Question:
Define a function that can accept two strings as input and concatenate them and then print it in console.

Hints:

Use + to concatenate the strings
"""
"""
def function_1():
    ans = 0
    input_1 = list(input("Enter values:-- ").split(","))
    print("values", input_1)
    for i in range(len(input_1)):
        ans += str(input_1[i])
    print(ans)
function_1()
"""
"""
def function_1():
    input_1 = input("Enter values:-- ")
    input_2 = input("Enter values:-- ")
    ans = input_1 + input_2
    print(ans)
function_1()
"""
"""
Question:
Define a function that can accept two strings as input and print the string with maximum length in console. 
If two strings have the same length, then the function should print al l strings line by line.

Hints:

Use len() function to get the length of a string
"""
"""
def function_1():
    input_1 = input("Enter string_1:-- ")
    input_2 = input("Enter string_2:-- ")
    if len(input_1) > len(input_2):
        print("largest string",input_1)
    elif len(input_1) < len(input_2):
        print("largest string",input_2)
    else:
        print("Both largest string",input_1)
        print("Both largest string",input_2)
function_1()
"""
"""
Question:
Define a function that can accept an integer number as input and print the "It is an even number" if 
the number is even, otherwise print "It is an odd number".

Hints:

Use % operator to check if a number is even or odd.
"""
"""
def function_1():
    input_1 = int(input("Enter value:-- "))
    if input_1 % 2 == 0:
        print("Even Number")
    elif input_1 % 2 != 0:
        print("ODD Number")
    else:
        print("Invalid number")
function_1()
"""
"""
Question:
Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) 
and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
"""
"""
dic = {}
a = input("Enter the values:-- ").split(",")
list_1 = [int(i) for i in a]
print(list_1)
for i in list_1:
    dic[i] = i**2
print(dic)
"""
"""
map(int,a)
print(type(a[1]))
"""
"""
Question:
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) 
and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
"""
"""
def function_1():
    dic = {}
    for i in range(0,21):
        dic[i] = i**2
    print(dic)
    print(type(dic))
function_1()
"""
"""
Question:
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) 
and the values are square of keys. The function should just print the values only.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.
"""
"""
def function_1():
    dic = {}
    for i in range(0,21):
        dic[i] = i**2
    print(dic.keys())
    print(dic.values())
    print(dic.items())
    print(dic)
    print((type(dic.keys())))
    print(type(dic.values()))
    print(type(dic.items()))
    print(type(dic))
function_1()
"""
"""
Question:
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included)
and the values are square of keys. The function should just print the keys only.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.
"""
"""
def fucntion_1():
    dic = {}
    for i in range(0,21):
        dic[i] = i**2
    print(dic.keys())
    print(type(dic.keys()))
    print(type(dic))
fucntion_1()
"""
"""
Question:
Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
"""
"""
def function_1():
    list_1 = []
    input_1 = int(input("Enter the range from o to :-- "))
    for i in range(input_1):
        list_1.append(i**2)
    print(list_1)
function_1()
"""
"""
Question:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print the first 5 elements in the list.

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list
"""
"""
def function_1():
    list_1 = []
    var_1 = 0
    var_2 = 0
    a = input("Enter the values:-- ").split(",")
    input_1 = [int(i) for i in a]
    var_1,var_2 = input_1[0],input_1[1]
    for i in range(var_1,var_2):
        list_1.append(i**2)
    print(list_1[0:6])
    print(list_1)
function_1()
"""
"""
Question:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print the last 5 elements in the list.

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list
"""
"""
def function_1():
    var_1 = 0
    var_2 = 0
    a = input("Enter range:-- ").split(",")
    list_1 = [int(i) for i in a]
    var_1,var_2 = list_1[0],list_1[1]
    for i in range(var_1,var_2):
        list_1.append(i ** 2)
    print(list_1[0:6])
    print(list_1)

    for i in range(0,21):
        list_1.append(i**2)
    a = list_1[0:6]
    print(a)
    print(list_1)

function_1()
"""
"""
Question:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print all values except the first 5 elements in the list.

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list
"""
"""
def function_1():
    list_1 = []
    for i in range(0,21):
        list_1.append(i**2)
    print(list_1)
    print(list_1[0:6])
function_1()
"""
"""
Question:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list 
"""
"""
def function_1():
    list_1 = []
    for i in range(0,21):
        list_1.append(i**2)
    print(list_1)
    print(list_1[-6:])
function_1()
"""
"""
Question:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print all values except the first 5 elements in the list.

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list
"""
"""
def function_1():
    list_1 = []
    for i in range(0,21):
        list_1.append(i**2)
   
    print(list_1[5:])
function_1()
"""
"""
Question:
Define a function which can generate and print a tuple where the value are square of numbers 
between 1 and 20 (both included). 

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use tuple() to get a tuple from a list.
"""
"""
def function_1():
    list_1 = []
    t = tuple()
    for i in range(0,21):
        list_1.append(i**2)
        t = tuple(list_1)
    print(t)
    print(type(t))
function_1()
"""
"""
Question:
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line 
and the last half values in one line. 

Hints:

Use [n1:n2] notation to get a slice from a tuple.
"""
"""
def function_1():
    t = tuple()
    list_1 = []
    for i in range(0,10):
        list_1.append(i**2)
        t = tuple(list_1)
    print(t)
    b = (t[:5])
    print(b)
    a = (t[5:])
    print(a)
function_1()
"""
"""
Question:
Write a program to generate and print another tuple whose values are even numbers in the given 
tuple (1,2,3,4,5,6,7,8,9,10). 

Hints:

Use "for" to iterate the tuple
Use tuple() to generate a tuple from a list.
"""
"""
def function_1():
    list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_2 = []
    for i in list_1:
        if i % 2 == 0:
            list_2.append(i)
    t = (tuple(list_2))
    print(t)
    print(type(t))
function_1()
"""
"""
Question:
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", 
otherwise print "No". 

Hints:

Use if statement to judge condition.
"""
"""
def function_1():
    input_1 = str(input("Enter string:-- "))
    if input_1 == "yes" or  input_1 == "YES" or input_1 == "Yes":
        print("Yes")
    else:
        print("No")
function_1()
"""
"""
Question:
Write a program which can filter even numbers in a list by using filter function. 
The list is: [1,2,3,4,5,6,7,8,9,10].

Hints:

Use filter() to filter some elements in a list.
Use lambda to define anonymous functions.
"""
"""
def function_1():
    list_1 = [1,2,3,4,5,6,7,8,9,10]
    even_numbers = filter(lambda x : x%2==0, list_1)
    print(even_numbers)
function_1()

"""

