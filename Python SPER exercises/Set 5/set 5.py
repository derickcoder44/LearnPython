import random
import family
import rectangle
import triangle
import circle
##def header():
##    print("This function just prints some text")
##    print("But it's cool becuause we could make it do anything")
##header()

##def mean(no1,no2,no3,no4):
##    mean = (no1+no2+no3+no4)/4
##    print(mean)
##mean (1,2,3,4)
##def greeting(name,age,address,state,zipCode):
##    print(name, "aged", age, "years live at", address,",",state,"," , zipCode,".")
##greeting("Derick",13,"2611 Turnstone Dr.","Ca",94566)

##def randomList(freind1, freind2,freind3,friend4,freind5):
##    friends = [freind1, freind2,freind3,friend4,freind5]
##    whichFriend = random.randint(1,4)
##    print(friends[whichFriend])
##randomList("Bob","Billy","Joe","Jake","Daniel")    
##
##def func(a,b,c):
##  print(a**(b**c))
##func(2,3,4)

##def change(dollarBills,quarter,dimes,nickles,cents):
##    total = (dollarBills*100) + (quarter*25) + (dimes*10) + (nickles*5) + (cents)
##    print(total, "cents")
##change(8,5,5,3,111)    

##def family(name,relation, city, state, color):
##    print("Name:", name)
##    print("Relation:", relation)
##    print("City:", city)
##    print("State:", state)
##    print("Favorite Color:", color)
family.family("Debbie", "Sister", "Pleasanton", "California", "Blue")
rectangle.rectangle(3,4)
triangle.triangle(4,4)
circle.circle(3)
