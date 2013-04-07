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

import random

class Player:
	cards = []
	
	def __init__(self):
		cards = []
		
	def hit(self, card):
		self.cards.append(card)
		
	def stand(self):
		pass
		
	def getCards(self):
		return self.cards

class Dealer:
	cards = []
	
	def __init__(self):
		cards = []
			
	def hit(self, card):
		self.cards.append(card)
		
	def getCards(self):
		return self.cards

class BlackJack:
	deck = []
	
	# Add players
	dealer = Dealer()
	player = Player()
	
	def __init__(self):
		# Create and shuffle the deck
		for s in ["Hearts", "Diamonds", "Clubs", "Spades"]:
			for n in range(1,14):
				self.deck.append([n,s])
		random.shuffle(self.deck)
		
		for i in range(2):
			self.player.hit(self.deck.pop())
		
		while(self.getScore(self.dealer.getCards()) < 17):
			self.dealer.hit(self.deck.pop())

	def getScore(self, cards):
		score = 0
		aces = 0
		# soft score
		for card in cards:
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

	def play(self):
		move = ""
		while move != "s" and self.getScore(self.player.getCards()) <= 21:
			print "Dealer: "
			self.printHand(self.dealer.getCards()[1:2])
			print "Player: "
			self.printHand(self.player.getCards())
			print "(h)it or (s)tand?"
			move = raw_input()
			if move == "h":
				self.player.hit(self.deck.pop())
			if move == "s":
				self.player.stand()

		print "Dealer: "
		self.printHand(self.dealer.getCards())
		print "Player: "
		self.printHand(self.player.getCards())
		dscore = self.getScore(self.dealer.getCards())
		pscore = self.getScore(self.player.getCards())
		# Push if both hands equal or both hands bust
		if dscore == pscore or (dscore > 21 and pscore > 21):
			print "Push!"
		# Lose if player busts or scores less than dealer
		elif pscore > 21 or (dscore > pscore and dscore <= 21):
			print "You lose!"
		else:
			print "You win!"

	def printHand(self, hand):
		s = ""
		for card in hand:
			if card[0] == 1:
				s += "[Ace of " + card[1] + "]"
			elif card[0] == 11:
				s += "[Jack of " + card[1] + "]"
			elif card[0] == 12:
				s += "[Queen of " + card[1] + "]"
			elif card[0] == 13:
				s += "[King of " + card[1] + "]"
			else:
				s += "[" + str(card[0]) + " of " + card[1] + "]"
			s += " "
		print s + str(self.getScore(hand))

blackjack = BlackJack()
blackjack.play()
