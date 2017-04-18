# print "Hello, World", "Again"

# print """How's
# it
# going?"""


# Variable - string, number, letters, any other stuff you can make with a keyboard
# and you want to stash something that's not fastinto something that's fast
# There is no declaration.
# In JS... var name = "Ian";
# Python is not heavily typed (like C#)

# #Arithmatic
# the_meaning_of_life = 40 + 2
# print the_meaning_of_life
# print the_meaning_of_life % 5

# Data types (variable types)
# - Strings - English type stuff for people (in yellow)
# - Numbers- something with digits and stuff that goes with digits (. -)
# - Floats, Integers
# - Booleans - True or False. 1 or 2. Yes or no. On or off.
# - Lists - list of variabels in one variable
# - Dictionary - variable of variables
# - Objectsdeal with it later

# Strings
# first_name = "Ian"
# last_name = "Booton"
# print "Hello, {} {}".format(first_name, last_name)
# # Placeholders
# print "Hello, %s %s for the %drd  time!" % (first_name, last_name, 3)

# FLoats 
# pi_float = 3.14 
# print pi_float
# print type(pi_float)
# make_int = int(pi_float)
# print make_int

# Booleans - true or false 
# truth = True
# print type(truth)

# Raw Input
# first_name = raw_input("First Name: ")
# last_name = raw_input("Last Name: ")

# Conditionals
# 1 = means you want to assign something
# 2 = means you want to compare what's on the left to the thing on the right

# if(first_name == last_name): 
# 	print "Your first name is the same as you last name?"

# age = raw_input("How old are you? ")
# age_int = int(age)
# if(age_int >= 21):
# 	print "You can buy beer."
# else:
# 	print "You are underage."

import random
random_num = random.randint(1, 10)

# Loop - keep going until told to stop
not_guessed = True
while not_guessed:
	guess_a_num = raw_input("Guess a number between 1 and 10. ")
	if (int(guess_a_num) == random_num):
		print "You guessed it!"
		not_guessed = False
	else:
		print "Sorry, you're wrong."
