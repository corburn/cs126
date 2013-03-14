import random

word_file = open("words.txt")
words = word_file.readlines()
word = random.choice(words).strip()

correct_guesses = []
incorrect_guesses = []

def print_word():
	s = ""
	for letter in word:
		if letter in correct_guesses:
			s += letter + " "
		else:
			s += "_ "
	print s

while len(incorrect_guesses) < 6:
	print_word()
	print "Please guess a letter."
	guess = raw_input()
	if guess in word:
		print "Correct! " + guess + " is in the word."
		correct_guesses.append(guess)
		user_wins = True
		for letter in word:
			if letter not in correct_guesses:
				user_wins = False
		if user_wins:
			print "You won!!"
			break
	else:
		incorrect_guesses.append(guess)
		print "Incorrect! You have " + \
				str(6 - len(incorrect_guesses)) + \
				" guesses left."
print "The word was " + word + "."
