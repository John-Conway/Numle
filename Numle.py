import random

while True:
    random_number = ''.join(random.sample('0123456789', 4))
    while True:
        if (user_number := input("Guess a 4-digit number or type 'give up' to show the number: ").lower()) == "give up":
            print("The number was:", random_number)
            break
        elif not user_number.isdigit() or len(user_number) != 4:
            print("Enter a valid 4-digit number or type 'give up' to show the number.")
        else:
            correct_digits = "".join(["T" if user_number[i] == random_number[i] else "V" if user_number[i] in random_number else "" for i in range(4)])
            num_correct_digits = correct_digits.count("T")
            num_correct_digits_without_position = len(correct_digits) - num_correct_digits
            if num_correct_digits == 4:
                print("Congratulations, you guessed the number!")
                break
            elif num_correct_digits or num_correct_digits_without_position:
                print(f"Hints: {num_correct_digits}T {num_correct_digits_without_position}V")
            else:
                print("There are no correct digits. Keep trying.")
    if (play_again := input("Do you want to play again? (Y/N): ").upper()) == "N":
        break