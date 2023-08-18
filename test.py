print("Welcome!Today we are going to take a math quiz")
print("Let's start!")
s = 0

a = int(input("How much is 3+4?"))
if a == 7:
    print("Correct, you got one point.")
    s += 1

else:
    print("Wrong, it is 7.")

b = int(input("How much is 10+5?"))
if b == 15:
    print("Correct!")
    s += 1

else:
    print("Wrong, it is 15.")

c = int(input("How much is 20+20?"))
if c == 40:
    print("Correct!")
    s += 1

else:
    print("Wrong, it is 40.")

print("")
print("You got "+str(s)+" out of 3 points.")
