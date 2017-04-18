import random
random_num = random.randint(1, 10)

print "I'm thinking of a number between 1 and 10, can you guess it? "

not_guessed = True
while not_guessed:
	guess_a_num = raw_input()
	if(int(guess_a_num) == random_num):
		print "You got it right!"
		not_guessed = False
	if(int(guess_a_num) > 10):
		print guess_a_num + " is an invalid number."
	elif(int(guess_a_num) < random_num):
		print guess_a_num + " is too low."
	elif(int(guess_a_num) > random_num):
		print guess_a_num + " is too high."
	else:
		print "Sorry, guess again. "