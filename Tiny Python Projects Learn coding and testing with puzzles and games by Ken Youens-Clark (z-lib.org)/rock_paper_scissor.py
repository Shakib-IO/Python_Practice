import random

#Print the Instruction
print("Rules of the game is :\nRock vs Paper = Paper wins\nRock vs scissor = Rock wins\nPaper vs scissor= scissor wins")

while True:
    print("\nEnter choice:\n1.Rock\n2.Paper\n3.Scissor\n")
    #Take input from user
    choice =  int(input("User input: "))

    while(choice>3 or choice<1):
        choice = int(input("enter valid input: "))

    #Set condition
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissor'

    #Print what user choice
    print("User choice is : " + choice_name)
    print("\nNow its computer turns.")

    #Now computer will any number between 1 ,2 ,3
    comp_choice = random.randint(1,3)

    #loop until the comp_choice is equal to the choice value
    while comp_choice == choice:
        comp_choice = random.randint(1,3)

    #setting condition on comp_choice
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name =' Paper'
    else:
        comp_choice_name ='Scissor'

    print("The computer choice is :" +comp_choice_name)

    print("\n"+choice_name+" vs "+comp_choice_name+"\n")

    #Condtion for wining
    if((choice == 1 and comp_choice == 2) or(choice == 2 and comp_choice == 1)):
        print("\nPaper wins" , end="")
        result = "Paper"
    elif((choice == 1 and comp_choice == 3)or choice == 3 and comp_choice == 1):
        print("\nRocks wins",end="")
        result = "Rock"
    else:
        print("\nScissor wins",ends="")
        result = "Scissor"
    
    #print who will win
    if result == choice_name:
        print("\nUser wins\n")
    else:
        print("\nComputer wins\n")

    print("Do you want to play again? (Y/N)")
    ans = input()

    if(ans =='n' or ans == 'N'):
        break

print("Thanks for playing")