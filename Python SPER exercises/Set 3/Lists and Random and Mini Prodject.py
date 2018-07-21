import random
randomListOfWords = ["This", "random", "list", "of", "words"]

x = random.choice(randomListOfWords)
y = list(x)
z = len(x)
a=['_']*z
print(a)
chances = z+3
while chances >  0:
    chances = chances - 1 
    guess = input(str("What is your first guess"))
    for i in range(z):
        if guess==y[i]:
            a[i]=guess
    print(a)
    if y==a:
        print("you won")
        break
if chances==0:
    print("You are out of chances")


