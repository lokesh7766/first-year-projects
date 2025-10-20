"""
workflow 
user choice = rps
comp choice = rrps
cases
1 tie 
2 rock paper
rock scissor 
3 paper rock
  paper scissor 
4 scissor rock
  scissor paper
"""
import random
item_list = ["Rock" , "Paper" , "scissor"]
user_choice = input("Enter ur move :  ")
comp_choice = random.choice(item_list)
print(f"user choice is {user_choice}")
print(f"computer choice is {comp_choice}")
if user_choice == comp_choice :
   print("both of them are same : so tie")
   print("TIED")
elif user_choice == "Rock":
    if comp_choice == "Paper":
      print("Computer won as paper smashes rock")
    elif comp_choice  == "scissor":
        print("user won ")   
elif user_choice == "paper":
    if comp_choice == "rock":
      print("user won ")
    elif comp_choice == "scissor":
        print("computer Won")
elif user_choice == "scissor":
     if comp_choice == "paper":
        print("User won")
     elif comp_choice == "Rock":
         print("computer won")
