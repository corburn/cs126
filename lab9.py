# Your game should play a single hand of black jack (which may involve several
# turns). You should print the cards that the dealer is holding and the cards
# that the player is holding.
#
# You should create a full deck of cards and store them in a list to represent
# the deck. Then use random's shuffle to shuffle the deck. Remove cards from the
# deck to put them in the player or dealer's hand.
#
# You will also need to devise a way for the user to input your moves. In this
# version of the game you only need to implement "hit" (take another card from
# the dealer) or "stand" (take no more cards):
#
# Your game should correctly detect if either the player or the dealer busts to
# determine the winner.

#from __future__ import print_function
import random
import sys

class BlackJack:
	deck = []
	dealer = []
	player = []

	def __init__(self):
		# Create and shuffle the deck
		for s in ["Hearts", "Diamonds", "Clubs", "Spades"]:
			for n in range(1,13):
				self.deck.append([n,s])
		random.shuffle(self.deck)

		# Deal two cards to each player
		for n in range(2):
			self.player.append(self.deck.pop())
			self.dealer.append(self.deck.pop())

	def getScore(self, player):
		score = 0
		aces = 0
		# soft score
		for card in player:
			# count aces
			if card[0] == 1:
				score += 11
				aces += 1
			elif card[0] > 9:
				score += 10
			else:
				score += card[0]

		# hard score
		for n in range(aces):
			if score > 21:
				score -= 10
		return score

	def hit(self):
		self.player.append(self.deck.pop())
		return self.getScore(self.player)

	def play(self):
		move = ""
		while move != "s" and self.getScore(self.player) <= 21:
			sys.stdout.write("Dealer: ")
			self.printHand(self.dealer)
			sys.stdout.write("Player: ")
			self.printHand(self.player)
			print "(h)it or (s)tand?"
			move = raw_input()
			if move == "h":
				blackjack.hit()
			if move == "s":
				blackjack.stand()

		dscore = self.getScore(self.dealer)
		pscore = self.getScore(self.player)
		# Push if both hands equal or both hands bust
		if dscore == pscore or (dscore > 21 and pscore > 21):
			print "Push!"
		# Lose if player busts or scores less than dealer
		elif pscore > 21 or dscore > pscore:
			print "You lose!"
		else:
			print "You win!"

	def printHand(self, hand):
		s = ""
		for card in hand:
			if card[0] == 1:
				s += "[Ace of " + card[1] + "]"
			elif card[0] == 10:
				s += "[Jack of " + card[1] + "]"
			elif card[0] == 11:
				s += "[Queen of " + card[1] + "]"
			elif card[0] == 12:
				s += "[King of " + card[1] + "]"
			else:
				s += "[" + str(card[0]) + " of " + card[1] + "]"
			s += " "
		print s

	def stand(self):
		# Dealer draws until their score is greater than or equal to 17
		while self.getScore(self.dealer) < 17:
			self.dealer.append(self.deck.pop())
		sys.stdout.write("Dealer: ")
		self.printHand(self.dealer)

blackjack = BlackJack()
blackjack.play()
