Python 3.5.1 (v3.5.1:37a07cee5969, Dec  5 2015, 21:12:44) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> 
>>> 22+44
66
>>> 12+112.5
124.5
>>> 12+12.5
24.5
>>> 30-13
17
>>> 4*5
20
>>> 4.0*5
20.0
>>> 22/11
2.0
>>> 5/2
2.5
>>> 7//2%
SyntaxError: invalid syntax
>>> 7//2
3
>>> %7//2
SyntaxError: invalid syntax
>>> 7//2
3
>>> %
SyntaxError: invalid syntax
>>> 7//%2
SyntaxError: invalid syntax
>>> 7//2
3
>>> Hello+world
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    Hello+world
NameError: name 'Hello' is not defined
>>> 2^44
46
>>> teacher="Vishal"
>>> print teacher
SyntaxError: Missing parentheses in call to 'print'
>>> print(teacher)
Vishal
>>> print("Hello")
Hello
>>> print('Hello'+20)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print('Hello'+20)
TypeError: Can't convert 'int' object to str implicitly
>>> print('Hello'+'World')
HelloWorld
>>> print('Hello','World')
Hello World
>>> teacher == 'Vishal'
True
>>> teacher == 'vishal'
False
>>> 1==1
True
>>> teacher!= "hello"
True
>>> 100>1
True
>>> "Batman" == "Superman"
False
>>> (15/2) <= (45+12-27)
True
>>> 1111 >= 2222/2
True
>>> 7%2 <=5
True
>>> type(teacher)
<class 'str'>
>>> len(teacher)
6
>>> x=5
>>> y=6
>>> z=5+6
>>> print(z)
11
>>> age = int( input("What's your age ?") )
What's your age ?13
>>> print(age)
13
>>> name = int( inpu("What's your name?") )
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    name = int( inpu("What's your name?") )
NameError: name 'inpu' is not defined
>>> name = int( input("What's your name?") )
What's your name?Derick
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    name = int( input("What's your name?") )
ValueError: invalid literal for int() with base 10: 'Derick'
>>> name = str( input("What's your name?") )
What's your name?Derick
>>> print("Hi,", name);
Hi, Derick
>>> #name = str( input("What's your name?") )
>>> #Exrcise 10
>>> #Ask the user for 4 numbers. Add all the numbers and store the result in a variable calles total. Print("The total is,total)
>>> firstNumber = int( input("What is the first number") )
What is the first number1
>>> secondNumber = int( input("What is the second number") )
What is the second number2
>>> thirdNumber = int( input("What is the third number") )
What is the third number3
>>> fourthNumber = int( input("What is the fourth number") )
What is the fourth number4
>>> fifthNumber = int( input("What is the fifth number") )
What is the fifth number5
>>> total = firstNumber + secondNumber + thirdNumber + fourthNumber + fifthNumber
>>> print("The total is,", total)
The total is, 15
>>> # ask the user for his or her name. Use the input function to get the name and store it in a variable. Print("Hello ,name entered by user")
>>> name = str( input("What's your name") )
What's your nameDerick
>>> print("Hello,", name)
Hello, Derick
>>> name = str( input("What's your name") )
What's your nameMathews
>>> print("hello,", name)
hello, Mathews
>>> #write a program that converts Farenheit to Celsius.
>>> farenhiet = int( input("What is the temperature in farenhiet") )
What is the temperature in farenhiet99.3
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    farenhiet = int( input("What is the temperature in farenhiet") )
ValueError: invalid literal for int() with base 10: '99.3'
>>> farenhiet = float( input("What is the temperature in farenhiet") )
What is the temperature in farenhiet96
>>> celcius = 5/9*(farenhiet-32)
>>> print
<built-in function print>
>>> print(celcius)
35.55555555555556
>>> 
>>> 
>>> pwd
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    pwd
NameError: name 'pwd' is not defined
>>> 
>>> 
>>> 
