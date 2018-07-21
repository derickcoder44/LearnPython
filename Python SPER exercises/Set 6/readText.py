import time
import random
##line = 1
##linesOfCode = open("linesOfCode.txt",'r')
##print(linesOfCode.read())
##linesOfCode.close()
##linesOfCode = open("linesOfCode.txt",'r')
##for lines in linesOfCode:
##    print(line,lines)
##    line = line+1
##linesOfCode.close()    
count = 1
add = 0
OfCode = open("linesOfCode.txt", 'w')
for i in range(1000):
    var=random.randint(1,1000)
    print(var,file = OfCode)
    count = count+1s
OfCode.close()

OfCode = open("linesOfCode.txt","r")
for lines in OfCode:
    add = int(lines)+add
print(add)    
