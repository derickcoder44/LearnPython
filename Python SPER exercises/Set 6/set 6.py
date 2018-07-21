import random
g = "Hello Will"
print([0],g[1],g[2])
print(g[-1])
print(g[0:3])
print(g[4:7])
print(g[:4])
print(g[4:])
print(g[:])
print(g[:3]+g[4:])
print(g[1]*3)
x=0
helloWill = "hello will"
while x < 10:
    print(helloWill[x], end="-")
    x= x+1
firstName = str( input("What is your first name?"))
lastNamr = str (input("What is your last name?"))
number = random.randint(1,100)
print("your user name is", firstName+lastNamr,number)
name = "DERICK MATHEWS"
print(name.capitalize())
print(name.title())
print(name.upper())
print(name.lower())
print(name.replace("E","e"))
helloWorld = "   Hello World    "
print(helloWorld.endswith("rld"))
print(helloWorld.isalpha())
print(helloWorld.isnumeric())
print(helloWorld.isupper())
print(helloWorld.islower())
dateStr = '12/12/2015'
Month, day, year = dateStr.split("/")
print(Month)
print(day)
print(year)
print(helloWorld.strip( ))
infile=open('infile.txt','r')
outFile=open('outfile.txt','w')
for lines in infile:
    randomNumber = random.randint(1,100)
    randomNumber = str(randomNumber)
    first,second=lines.split()
    uname=(first+"_"+second+randomNumber).lower()
    outFile.write(uname)
infile.close()
outFile.close()
x=1
while x==1:
    numberOfSides =  input("How many sides are there")
    total = (numberOfSides-2)*180
    eachMeasure = total/numberOfSides
    print(eachMeasure)


