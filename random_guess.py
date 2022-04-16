import random

def guess_random_number(tries, start, stop):
    random_number = random.randint(start,stop)
    # Write a while loop that loops as long as tries is not equal to 0
    while tries != 0:
        print(f"Number of tries left: {tries}")
        print(f"Guess a number between {start} and {stop}: ")
        while True:
            try:
                guess = int(input())
                break
            except ValueError:
                print("Please enter a number")
        if guess == random_number:
            print("You guessed correctly!")
            break
        elif guess < random_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        tries -= 1
    else:
        print("You ran out of tries")
        
def guess_random_num_linear(tries, start, stop):
    random_number = random.randint(start,stop)
    print(f"The number for thr program to guess is:", random_number)
    for num in range(start, stop+1):
        if not tries:
            print("The program has failed to guess the correct number.")
            return
        print(f"Number of tries left: {tries}")
        print(f"The program is guessing...", num)
        if num == random_number:
            print("The program has guessed the correct number.")
            return

        tries -= 1

def guess_random_num_binary(tries, start, stop):
    random_number = random.randint(start,stop)
    print(f"Random number to find:", random_number)

    lower_bound = start
    upper_bound = stop
    
    while tries:
        pivot = (lower_bound + upper_bound) // 2
        if pivot == random_number:
            print("Found it! The answer is: ", random_number)
            return
        elif pivot > random_number:
            print("Guessing lower..")
            upper_bound = pivot - 1
        else:
            print("Guessing higher..")
            lower_bound = pivot + 1
        tries -= 1
    print("The program has failed to guess the correct number.")



#guess_random_number(9, 1, 10)
#guess_random_num_linear(5, 1, 10)
guess_random_num_binary(5, 1, 100)
