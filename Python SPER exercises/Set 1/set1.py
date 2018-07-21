Python 3.5.1 (v3.5.1:37a07cee5969, Dec  5 2015, 21:12:44) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
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
SyntaxError: invalid syntax
>>> #ask the user for how many quarters, dimes, nickles and pennies to calculate the total. Find the total in pennies. Convert the pennies to dollars. Print the result in the format.
>>> pennies = int( input("How many pennies are there)
		     
SyntaxError: EOL while scanning string literal
>>> pennies = int( input("How many pennies are there") )
How many pennies are there10
>>> nickles = int( input("How many nickles are there") )
How many nickles are there3
>>> dimes = int( input("How many dimes are there") )
How many dimes are there40
>>> quarters = int( input("How many quarters are there") )
How many quarters are there3
>>> dollarBills = int( input("How many dollar bills are there") )
How many dollar bills are there2
>>> fiveDollarBills = int( input("How many fiveDollarBills") )
How many fiveDollarBills3
>>> fiveDollarBills = int( input("How many five dollar bills") )
How many five dollar bills3
>>> tenDollarBills = int( input("How many tenDollarBills") )
How many tenDollarBills2
>>> pennies = cents
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    pennies = cents
NameError: name 'cents' is not defined
>>> cents = pennies
>>> cents = cents+nickles(5)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    cents = cents+nickles(5)
TypeError: 'int' object is not callable
>>> cents = cents + cents*5
>>> cents = pennies
>>> cents = cents+nickles*5
>>> cents = cents + dime*10
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    cents = cents + dime*10
NameError: name 'dime' is not defined
>>> cents = cents + dimes*10
>>> cents = cents + dollarBills*100
>>> cents = cents + quarters*25
>>> cents = cents + fiveDollarBills*500
>>> cents = cents + tenDollarBills*1000
>>> print("the cents is,", cents)
the cents is, 4200
>>> dollars = cents/100
>>> cent = cents-dollars*100
>>> print("you have", dollars"dollars, and", cent "cents.")
SyntaxError: invalid syntax
>>> print("you have"+ dollars"dollars, and"+ cent "cents.")
SyntaxError: invalid syntax
>>> age = int( input("How old are you") )
How old are you29
>>> if age >= 16:
	print("you are eligible to drive")
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if age >= 16:
	print("you are eligible to drive")

	
you are eligible to drive
>>> if age >= 16:
	print("you are eligible to drive")
>>> else:
	
SyntaxError: invalid syntax
>>> if age >= 16:
	print("you are eligible to drive")
>>> else:print("You are not eligible to drive")
SyntaxError: invalid syntax
>>> if age >= 16:
	print("you are eligible to drive")
>>> else:print("You are not eligible to drive")
SyntaxError: invalid syntax
>>> if age >= 16:
	print("you are eligible to drive")
>>> else:print("You are not eligible to drive")
SyntaxError: invalid syntax
>>> if age >= 16:
	print("You are eligible to drive")
	else:
		
SyntaxError: invalid syntax
>>> lastName = int( input("How old are you") )
How old are you
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    lastName = int( input("How old are you") )
ValueError: invalid literal for int() with base 10: ''
>>> lastName = str( input("What is your last name") )
What is your last nameMathews
>>> gender = int( input("Are you a boy or a girl") )
Are you a boy or a girlboy
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    gender = int( input("Are you a boy or a girl") )
ValueError: invalid literal for int() with base 10: 'boy'
>>> gender = str( input("Are you a boy or a girl") )
Are you a boy or a girlboy
>>> if gender = boy:
	
SyntaxError: invalid syntax
>>> if gender = "boy":
	
SyntaxError: invalid syntax
>>> if gender == "boy":
	print("hello, Mr.", lastname)

	
Traceback (most recent call last):
  File "<pyshell#51>", line 2, in <module>
    print("hello, Mr.", lastname)
NameError: name 'lastname' is not defined
>>> if gender == "boy":
	print("hello, Mr.", lastName)

	
hello, Mr. Mathews
>>> if gender == "girl":
	print("hello, Mrs.", lastName)

	
>>> number = int( input("What is your number") )
What is your number13
>>> if number//2 == number/2:
	print("This number is even")

	
>>> if number//2 =! number/2:
	
SyntaxError: invalid syntax
>>> if number//2 != number/2:
	print("This number is odd")

	
This number is odd
>>> 
