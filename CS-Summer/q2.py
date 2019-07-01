# Write a Python program to guess a number between 1 to 9.  
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.
while True:
    a=int(input("Guess a number between 1-9 "))
    if (a==9):
        print("Well done correctly guessed")
        break
    