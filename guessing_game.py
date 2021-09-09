secret_word = "giraffe"
guess = ""

# while guess != secret_word:
#     guess = input("Enter guess: ")

# print("You win")

i = 1

while i <= 3:
    guess = input("Enter guess: ")
    if guess == secret_word:
        print("You win!")
        break
    i += 1
