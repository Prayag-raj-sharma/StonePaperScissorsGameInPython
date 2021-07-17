print("Game of Stone(S), Paper(P) and Scissors($):-")
print("There will be only 5 chances given in this game:-")
import random
i=0
your_point=0
computer_point=0
Tie_point=0
while i<5:
    print()
    ch = input("Enter your choice from options ie. S,P or $:")
    list = ["S", "P", "$"]
    comp = random.choice(list)
    print("Computer choice",comp)
    if comp =="S":
        if ch =="S":
            print("Its a tie,no one gets any point!!!")
            Tie_point+=1
        elif ch =="P":
            print("You win,this point!!!")
            your_point+=1
        elif ch =="$":
            print("Computer win,this point!!!")
            computer_point+=1
    if comp == "$":
        if ch == "$":
            print("Its a tie,no one gets any point!!!")
            Tie_point +=1
        elif ch == "S":
            print("You win,this point!!!")
            your_point +=1
        elif ch == "P":
            print("Computer win,this point!!!")
            computer_point +=1
    if comp == "P":
        if ch == "P":
            print("Its a tie,no one gets any point!!!")
            Tie_point += 1
        elif ch == "$":
            print("You win,this point!!!")
            your_point += 1
        elif ch == "S":
            print("Computer win,this point!!!")
            computer_point +=1
            print()
    a=f"Till now you have won {your_point} points and computer have won {computer_point} points"
    print(a)
    i+=1

print()
if(your_point>computer_point):
        print("Congratulation!!! You Won The Game!!!")
elif(your_point==computer_point):
        print("Its A Draw..Try Again!!!")
else:
        print("Ohhh!!! You Lost This Game...Better Luck Next Time..")


        
