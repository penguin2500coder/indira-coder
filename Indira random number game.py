print("HI")

'''for i in range(10,20,2):
    print(i)


import random

for i in range(2,60,3):
    print(i)


for i in range(20):
    print(random.randint(1,100))'''


import random
'''print("welcome to the fortune teller")
print("your fortune is...")
random=random.randint(1,4)
if random==1:
    print("You will have a big suprise comming up")
if random==2:
    print("You will get your dream pet")
if random==3:
    print("You will go on a vacation soon")
if random==4:
    print("You will win a million dollars")'''


password="world"

guess=input("guess the pasword: ")
while guess!=password:
    guess=input("guess again:")

print("Welcome to the random number game")
number=random.randint(1,100)
score=1
guess=int(input("Guess the number 1-100"))

while guess!=number:
    score=score+1
    print("icorrect")
    if guess > number:
        print("You guessed too high")
    elif guess < number:
        print("You guessed to low")
    guess=int(input("Guess again"))
print("Good job, you got it. The number was",number)
print("It took you",score, "tries")










