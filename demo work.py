from random import randint
random_numbers=randint(0,100)
lives = 3
while lives > 0:
    guess_number = int(input("guess the number "))
    if random_numbers == guess_number:
        print("you are correct")
        break
        lives -= 1
    print("game over!!")