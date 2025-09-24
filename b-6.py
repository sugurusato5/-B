import random


dice_sur = int(input("サイコロの面の数は？： "))


num = int(input("何回振りますか?: "))

count = 0
while count <= num:
    dice = random.randint(1, dice_sur)
    print(dice, end=" ")
    count += 1
