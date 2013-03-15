import random

word_file = open("words.txt")
words = word_file.readlines()
print len(words)

# Filter words that are not between 4 and 7 characters in length
words = [word.strip() for word in words if len(word.strip()) >= 4 and len(word.strip()) <= 7]
random_word = random.choice(words)
# Filter words that are not the length of the random word
words = [word for word in words if len(word) == len(random_word)]

# Create a list of words that have no duplicate letters
unique = ["".join(set(word)) for word in words]

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

"""while len(incorrect_guesses) < 6:
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
print "The word was " + word + "."""

#for word in unique:
	#print word

alphabet = "abcdefghijklmnopqrstuvwxyz"

for l in alphabet:
	count = 0
	for word in unique:
		if l in word:
			count += 1
	print l + ": " + str(count)
index = -1
size = 0
for i, word in enumerate(unique):
	if size < len(word):
		size = len(word)
		index = i
print size
print words[index]

count = 0
for word in unique:
	if 'a' in word:
		count += 1

print count

print "====="
for i in range(len(random_word)-1):
	count = 0
	for word in words:
		if 'a' in word[i]:
			count += 1
	print count
print "+++++++"
i_words = [i for i, word in enumerate(unique) if 'a' in word]
print len(i_words)
first = [i for i in i_words if words[i][0] == 'a']
print len(first)

def filter(letter, position):
	return [word for word in words if letter not in word[position]]
			
