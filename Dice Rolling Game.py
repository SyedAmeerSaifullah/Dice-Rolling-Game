import random
total_roll=int(input("Enter the number of times you want to roll the dice: "))
roll_count=1
a="Y"
while True:
    if a=="Y" or a=="y":
        if(roll_count<=total_roll):
            dice_roll_1=random.randint(1,6)
            dice_roll_2=random.randint(1,6)
            dice_roll=[dice_roll_1,dice_roll_2]
            print(f"Roll count :{roll_count}, Dice Roll: {dice_roll}")
            roll_count+=1
            print("Do you want to roll the dice again? Y/N: ") 
            a=str(input())
    if(a=="N" or a=="n"):
        break
    if (roll_count>total_roll):
        print("You can no more roll the dice ")
        break