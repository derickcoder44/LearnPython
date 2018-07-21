
# Convert percentage to grades
percentage = int( input("What is the percentage you got") )
if percentage < 0:
    print("invalid score")
elif percentage <= 59:
    print("You got an F")
elif percentage <= 69:
    print("You got a D")
elif percentage <= 79:
    print("You got a C")
elif percentage <= 89:
    print("You got a B")
elif percentage <= 100:
    print("Congradulations you got an A!")
