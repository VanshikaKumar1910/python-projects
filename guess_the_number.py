import random

def guess(x):
  """
  Plays a guessing game where the user tries to guess a random number between 1 and x.

  Args:
      x: Upper limit for the random number (inclusive).

  Returns:
      number_of_guesses: The number of guesses it took the user to find the random number.
  """
  random_number = random.randint(1, x)
  guess_count = 0
  guess = 0
  while random_number != guess:
    try:
      guess = int(input(f'Enter any number to guess between 1 and {x}: '))
      guess_count += 1
      if guess > random_number:
        print("Too high, guess again")
      elif guess < random_number:
        print("Too low, guess again")
      # conditional for hint
      if guess_count >= 3:
        hint_range = int(x / 2)
        print(f"Hint: The number is {('>=' if random_number >= hint_range else '<')}"
              f"{hint_range}")
    except ValueError:
      print("Invalid input. Please enter an integer.")
  print(f"Yay, correct guess! You took {guess_count} guesses.")
  return guess_count


number_of_guesses = guess(16)

play_again = input("Do you want to play again? (y/n): ")
if play_again.lower() == 'y':
  guess(16)  
else:
  print("Thanks for playing!")
