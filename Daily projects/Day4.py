import random

rock=('''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
''')
paper=('''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
''')
scissor=('''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
''')


       
user_choice= int(input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors. "))

print("You chose")
match user_choice:
    case 0:
        print(rock)
    case 1:
        print(paper)
    case 2:
        print(scissor)
        
sys_choice=random.randint(0,2)
print("The computer chose:")

match sys_choice:
    case 0:
        print(rock)
    case 1:
        print(paper)
    case 2:
        print(scissor)

if (user_choice==0 and sys_choice==1) or (user_choice==1 and sys_choice==2) or (user_choice==2 and sys_choice==0):
    print("You lose.Better luck next time")
elif user_choice==sys_choice:
    print("It's a draw")
else:
    print("You win!")