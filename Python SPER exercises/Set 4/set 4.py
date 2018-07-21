import time
import random
##classMark = ['Math', 'Writing','History','Science']
##billMarks = [86,      80,       78,       94] #list one
##tomMarks = [65,       78,       79,       87] #list two
##mikeMarks = [89,      76,       87,       75] #list three
##print(classMark, billMarks, tomMarks, mikeMarks)
##person = str( input("Whose marks do you want to see? If you want to see subjects type Subjects") )
##if person != "Bill" or "Tom" or "Mike" or "Subjects":
##    print("that is not a valid person")
##else:
##    subject = str( input("What subject do you want to see?"))
##    if person == "Bill":
##        if subject == "Math":
##            print(billMarks[0])
##        elif subject == "Writing":
##            print(billMarks[1])
##        elif subject == "History":
##            print(billMarks[2])
##        elif subject == "Science":
##            print(billMarks[3])
##        else:
##            print("that is not a vald subject")
##    elif person == "Tom":
##        if subject == "Math":
##            print(tomMarks[0])
##        elif subject == "Writing":
##            print(tomMarks[1])
##        elif subject == "History":
##            print(tomMarks[2])
##        elif subject == "Science":
##            print(tomMarks[3])
##        else:
##            print("that is not a vald subject")
##    elif person == "Mike":
##        if subject == "Math":
##            print(mikeMarks[0])
##        elif subject == "Writing":
##            print(mikeMarks[1])
##        elif subject == "History":
##            print(mikeMarks[2])
##        elif subject == "Science":
##            print(mikeMarks[3])
##        else:
##            print("that is not a vald subject")
##    elif person == "Subjects":
##        Average  = str( input("Do you want to see the average?") )
##        if Average == "yes":
##            if subject == "Math":
##                average = (billMarks[0]+tomMarks[0]+mikeMarks[0])/3
##                print("the average is:", average) 
##            elif subject == "Writing":
##                average = (billMarks[1]+tomMarks[1]+mikeMarks[1])/3
##                print("the average is:", average)
##            elif subject == "History":
##                average = (billMarks[2] + tomMarks[2] + mikeMarks[2])/3
##                print("the average is:", average)
##            elif subject == "Science":
##                average = (billMarks[3] + tomMarks[3] + mikeMarks[3])/3
##            print("the average is:", average)
##        else:
##            if subject == "Math":
##                print("bill's grade:",billMarks[0],"tom's grade:", tomMarks[0], "mike's grade:", mikeMarks[0])  
##            elif subject == "Writing":
##                print("bill's grade:",billMarks[1],"tom's grade:", tomMarks[1], "mike's grade:", mikeMarks[1])  
##            elif subject == "History":
##                print("bill's grade:",billMarks[2],"tom's grade:", tomMarks[2], "mike's grade:", mikeMarks[2])  
##            elif subject == "Science":
##                print("bill's grade:",billMarks[3],"tom's grade:", tomMarks[3], "mike's grade:", mikeMarks[3])  
##familyMembersName = ["Dennis", "Mathews", "Rima", "Dennis", "Debbie", "Mathews", "Derick", "Mathews"]
##count = familyMembersName.count("Dennis")
##print(count)


##originalNumber = random.randint(20,30)
##print(originalNumber)
##incorectTries = []
##missed = False
##while originalNumber != 0:
##    guessedNumber = int( input("What is your guess?") )
##    if originalNumber != guessedNumber:
##        print("that is incorect")
##        incorectTries.append(guessedNumber)
##        missed = True
##    else:
##        print("That is corect good job!")
##        if missed == True :
##            print("The incorect tries were:", incorectTries)
##        else:
##            print("Nice, you got it on your first try!")
##    
##        break
##eng2sp   = {"one" : "uno", "two" : "dos", "three" : "tres"}
##eng2sp['four'] = 'cuatro'
##print(eng2sp.keys())

##products = {'fidget spinner':'$5', 'apple':'$3','banana':'$3', 'pear':'$3'}
##print(products.keys())
##chosenProduct = str( input("Which product would you like to buy"))
##if chosenProduct in products.keys():
##    print("that product costs", products[chosenProduct])
##else:
##    print("We don't have that product. Check somewhere else.")
a=1
x = 1
xa=0
xb=0
xc=0
xd=0
xe=0
xf=0
xg=0
xh=0
xi=0
ya=0
yb=2
yc=4
yd=5
ye=4
yf=3
yg=4
yh=5
yi=4
xOrO = 'X'
symbolOn = True
ticTacToe = {1:0 , 2:0 , 3:0 ,4:0 ,5:0 ,6:0 ,7:0 ,8:0, 9:0}
while a == 1:
    if xOrO == 'X':
        xOrO = 'O'
    elif xOrO == 'O':
        xOrO = 'X'
    numberChosen  = int( input("What number do you choose") )
    if numberChosen == 1 and symbolOn == True:
        ticTacToe[1] = xOrO
        print(ticTacToe)
        if xOrO == 'X':
            xa=1
        else:
            oa=1
    if numberChosen == 2 and symbolOn == True:
        ticTacToe[2] = xOrO
        print(ticTacToe)
        if xOrO == 'X':
            xb=1
        else:
            ob=1
    if numberChosen == 3 and symbolOn == True:
        ticTacToe[3] = xOrO
        print(ticTacToe)
        if xOrO == 'X':
            xc=1
        else:
            oc=1
    if numberChosen == 4 and symbolOn == True:
        ticTacToe[4] = xOrO
        print(ticTacToe)
        if xOrO == 'X':
            xd=1
        else:
            od=1
    if numberChosen == 5 and symbolOn == True:
        ticTacToe[5] = xOrO
        print(ticTacToe)
        if xOrO == 'X':
            xe=1
        else:
            oe=1
    if numberChosen == 6 and symbolOn == True:
        ticTacToe[6] = xOrO
        print(ticTacToe)
        if xOrO == 'X':
            xf=1
        else:
            of=1
    if numberChosen == 7 and symbolOn == True:
        ticTacToe[7] = xOrO
        print(ticTacToe)
        if xOrO == 'X':
            xg=1
        else:
            og=1
    if numberChosen == 8 and symbolOn == True:
        ticTacToe[8] = xOrO
        print(ticTacToe)
        if xOrO == 'X':
            xh=1
        else:
            oh=1
    if numberChosen == 9 and symbolOn == True:
        ticTacToe[9] = xOrO
        print(ticTacToe)
        if xOrO == 'X':
            xi=1
        else:
            oi=1
    if (xa==1 and xb==1 and xc==1) or (xa==1 and xd==1 and xg==1) or (xa==1 and xe==1 and xf==1) or (xb==1 and xe==1 and xh==1) or (xc==1 and xf==1 and xi==1) or (xd==1 and xe==1 and xf==1) or (xg==1 and xh==1 and xi==1):
        print('x won')
        break
        
    if (ya==1 and yb==1 and yc==1) or (ya==1 and yd==1 and yg==1) or (ya==1 and ye==1 and yf==1) or (yb==1 and ye==1 and yh==1) or (yc==1 and yf==1 and yi==1) or (yd==1 and ye==1 and yf==1) or (yg==1 and yh==1 and yi==1):
        print('O won')
        break
