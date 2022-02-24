import random


def guess(x):
		random_number = random.randint(1, x)
		guess = 0
		while guess != random_number:
			guess = int(input(f'guess a number between 1 and {x}: '))
			if guess < random_number:
				print('Sorry, guess again. too low')
			elif guess > random_number:
				print('Sorry, guess again. too high')
            elif guess = random_number:
                print('the number has duplicated')


		print(f'congratss!! you have guessed number {random_number} correctly!!!')
			

guess(10)
