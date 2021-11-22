import random
number = random.randint(0, 9)
chances = 0

while chances < 0: 
#while loop start
    guess = input("")
    print(guess)
    if(number == guess):
        print("You guessed the number! Good Job!")
        break
        #if end

    elif(number < guess):
        print("Your number is too big, try a smaller number.")
        #elif end

    else:
        ("Your number is too small, try a larger number.")
        #else end

#while loop end

if not chances < 5:
    print("YOU LOST!!! The number was ", number)


