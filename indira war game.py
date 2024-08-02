'''anything=["soccer",10,True,2.5,"code"]
print(anything[1])
anything.append("random")
print(anything)
anything.remove(True)
print(anything)'''


import random

print("Welcome to the war game")
myHand=[]
compHand=[]
for i in range(10):
    myHand.append(random.randint(1,100))
    compHand.append(random.randint(1,100))
print("Here is your updated hand")
print(myHand)
print("Here is the computer's hand")
print(compHand)

while len (myHand)!=0 or len (compHand)!=0:
    print(myHand)
    choice=int(input("What number would you like to play"))
    while choice not in myHand:
     Choice=int(input("What number would you like to play"))
    myHand.remove(choice)
    compChoice=random.choice(compHand)
    compHand.remove(compChoice)
    print("The computer chose",compChoice)

    if choice>compChoice:
        print("You won this round")
        myHand.append(choice)
        myHand.append(compChoice)
    
    elif choice<compChoice:
        print("You lost this round")
        myHand.append(choice)
        myHand.append(compChoice)

    else:
         print("Tie")
        
if len(myHand)>len(compHand):
    print("You won this war")

else:
    print("Computer won this war")
    
    

    
