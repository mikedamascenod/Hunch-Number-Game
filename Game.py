from random import randint

name = input("Please Enter Your Name: ")
print("Welcome to my Number Game, " + name)


def game():
    rand_number = randint(0, 100)
    print("\nI have selected a number between 1 to 100...")
    print("You have 6 chances to guess that number...")
    i = 1
    r = 1
    while i < 7:
        user_number = int(input('Enter Your Number: '))
        if user_number < rand_number:
            print("\n" + name + ", My number is greater than your guessed number")
            print("You now have " + str(6 - i) + "  chances left ")
            i = i + 1
        elif user_number > rand_number:
            print("\n" + name + ", My Number is less than  your guessed number")
            print("You now have" + str(6 - i) + " Chances left ")
            i = i + 1
        elif user_number == rand_number:
            print("\nCongratulations" + name +
                  " !! You have guessed the correct number !")
            r = 0
            break
        else:
            print("This is an invalid number. Please try again")
            print("You now have" + str(6 - i) + " Chances left ")
            continue
    if r == 1:
        print("Sorry you lost the game!!")
        print("My number was = " + str(rand_number))


def main():
    game()
    while True:
        another_game = input("Do you want to play again ? (y/n): ")
        if another_game == "y":
            game()
        else:
            break


main()
print("\nEnd of the Game! Thank you for playing")
