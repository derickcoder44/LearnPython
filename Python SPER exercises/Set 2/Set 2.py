'''
import time
count = 1
for loop_var in range(1,100,1):
    count = count+1
    print("Derick", count)
    
number = 0    
for loop_var in range(1,20,1):
    number = number + 1
    print(number)
    if number%2 == 1:
        print("odd")
    else:
        print("even")
timeLeft = 6
for loop_var in range (0,5,1):
    timeLeft = timeLeft - 1
    print(timeLeft)
    time.sleep(1)
print("blastoff!")

multiplyBy = 0
for loop_var in range (0,12,1):
    print("5 times",multiplyBy,"is equal to", 5*multiplyBy)
    multiplyBy = multiplyBy + 1

multiplyBy = int( input("What's the number you wanted to multiply") )
print("5 times",multiplyBy,"is equal to", 5*multiplyBy)

counter = 0
for loop_var in range (0,5,1):
    for v_var in range (0,5,1):
        print("*", end = '')
    print('')
for x_var in range(1,5,1):
    for y_var in range(1,5,1):
        print(y_var,end='')
    print('')

for x in range (0,5,1):
    for y in range (0,x,1):
        print('*', end='')
    print('')

for z in range (1,51,1):
    print(z)

counter = 21
while counter >= 1:
    counter = counter-1
    print(counter)
counter = 0
while counter <= 34:
    counter = counter+1
    print(counter)
    
counter = -17
while counter <= 25:
    counter = counter+1
    print(counter)
while counter >= 9:
    counter = counter-1
    print(counter)
print("bing!")

1 !=0 and 2 == 1
"test" != "testing"
"test" == 1
True and False
1 == 1 and 0!=1
not (10==1 or 1000 == 1000)
not (1 != 10 or not(3 == 4))
not ("testing" == "testing" and "Zed" == "Cool Guy")
"chunky" == "peanut" and (not(3==4 or 3 == 3))
1==1 and (not("testing" == 1 or 1==0))


price = float( input("What is the price of your item?") )
if price <= 10.00:
    finalPrice = price-(price*0.10)
else:
    finalPrice = price-(price*0.20)
print("$",finalPrice)


grade = int( input("What grade are you in?"))
age = int( input("What is your age") ) 
if age >= 8 and grade >= 3:
    print("you are eligible to play the game")
else:
    print("you are not eligble to play the game")
    
state = str( input("What state do you live in"))
if state == "California" or "Oregon" or "Washington":
    print("We suggest you go on a costal drive")
else:
    print("You my be better off skiing")
    
vacation = bool( input("Do you have a vation coming up?") )
grade = int( input("What grade are you in")

if vacation == true and grade!=12:             
        print("great time to study for SAT")
elif vacation == false:
        print("have a great summer")
else:
        print("ohh that sucks")

for x in range (1,101,2):
    print(x)
    
for x in range (100,0,-3):
    if x>20 and x<30:
        print("tick")
    else:
        print(x)
'''
import random
import time
var = random.randint(1,10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)        
print(var)

x=1
while x<100:
    y=random.random()
    print(y)

