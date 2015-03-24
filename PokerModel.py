import operator
import random
import pygame

class Card:

	def __init__(self, rank, suit):

		self.rank = 0
		self.suit = ''
		self.image_path = ('img/'+str(rank) + str(suit) + '.png')
		self.selected = False

		#convert the rank to an integer so it's easier to compute the winner of a hand
		if rank == 'A':
			self.rank = 14
		elif rank == 'K':
			self.rank = 13
		elif rank == 'Q':
			self.rank = 12
		elif rank == 'J':
			self.rank = 11
		elif rank == 'T':
			self.rank = 10
		else:
			self.rank = int(rank)

		self.suit = suit

	def __str__(self):
		out = ""

		#convert rank back to a word so it's easier to read
		if self.rank == 14:
			out += "Ace"
		elif self.rank == 13:
			out += "King"
		elif self.rank == 12:
			out += "Queen"
		elif self.rank == 11:
			out += "Jack"
		else:
			out += str(self.rank)

		out += ' of '

		#convert the suit to a word so it's easier to read
		if self.suit == 'H':
			out += 'Hearts'
		elif self.suit == 'S':
			out += 'Spades'
		elif self.suit == 'C':
			out += 'Clubs'
		else:
			out += 'Diamonds'

		return out

#only exists for the __str__ function
class Hand:

	def __init__(self, hand):
		self.hand = hand

	def __str__(self):
		out = ""
		for card in self.hand:
			out += str(card) + ", "
		return out

	def __getitem__(self, index):
		return self.hand[index]

	def __len__(self):
		return len(self.hand)

class Deck:

	def __init__(self):
		self.deck = []

		for suit in ['H','S','C','D']:
			for rank in range(2,15):
				self.deck.append(Card(rank, suit))

	def __str__(self):
		out = ""
		for card in self.deck:
			out += str(card) + "\n"
		return out

	def __getitem__(self, index):
		return self.deck[index]

	#return a list a cards taken from the deck
	def deal(self, amount):
		cards = []

		#cap out the cards dealt
		if amount > len(self.deck):
			print "There are not enough cards!  I can only deal " + str(len(self.deck)) + " cards."
			amount = len(self.deck)

		#create and then return a list of cards taken randomly from the deck
		for i in range(amount):
			card = random.choice(self.deck)
			self.deck.remove(card)
			cards.append(card)
		return cards


class Poker:

	def __init__(self):
		self.deck = Deck()
		self.playerHand = Hand(self.deck.deal(5))
		self.comp1Hand = Hand(self.deck.deal(5))
		self.comp2Hand = Hand(self.deck.deal(5))
		self.comp3Hand = Hand(self.deck.deal(5))

	def replace(self, hand):
		count = 0
		for i in xrange(3):
			for card in hand:
				if card.selected:
					hand.hand.remove(card)
					count += 1

		hand.hand.extend(self.deck.deal(count))

	#plays a round of poker with 4 hands
	#winner is displayed and scores for each hand as well
	#the number of the winner is returned by the function
	def play_round(self, hand1, hand2, hand3, hand4):

		score1 = self.get_score(hand1)
		score2 = self.get_score(hand2)
		score3 = self.get_score(hand3)
		score4 = self.get_score(hand4)

		print "Score1: " + str(score1)
		print "Score2: " + str(score2)
		print "Score3: " + str(score3)
		print "Score4: " + str(score4)

		winner = max(score1, max(score2, max(score3, score4)))

		if winner == score1:
			print 'Player 1 Wins!'
			return 1

		elif winner == score2:
			print 'Player 2 Wins!'
			return 2

		elif winner == score3:
			print 'Player 3 Wins!'
			return 3

		elif winner == score4:
			print 'Player 4 Wins!'
			return 4

		return -1

	#returns an integer that represents a score given to the hand.  The first digits represents the type of hand and the rest represent the cards in the hands
	def get_score(self, hand):
		#make a dictionary containing the count of each each
		cardCount = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0}

		for card in hand.hand:
			cardCount[card.rank] += 1

		#count number of unique cards
		uniqueCount = 0
		for rankCount in cardCount.values():
			if rankCount > 0:
				uniqueCount += 1

		straight = self.is_straight(hand)
		flush = self.is_flush(hand)

		points = 0

		if straight and flush:
			points = max(points, 9) #straight flush
			print str(hand) + ": Straight flush"
		elif flush and not straight:
			points = max(points, 6) #flush
			print str(hand) + ": Flush"
		elif not flush and straight:
			points = max(points, 5) #straight
			print str(hand) + ": Straight"

		elif uniqueCount == 2:
			if max(cardCount.values()) == 4:
				points = 8 #four of a kind (2 uniques and 4 are the same)
				print str(hand) + ": Four of a kind"
			elif max(cardCount.values()) == 3:
				points = 7 #full house (2 unique and 3 are the same)
				print str(hand) + ": Full house"

		elif uniqueCount == 3:
			if max(cardCount.values()) == 3:
				points = 4 #three of a kind (3 unique and 3 are the same)
				print str(hand) + ": Three of a kind"
			elif max(cardCount.values()) == 2:
				points = 3 #two pair (3 uniques and 2 are the same)
				print str(hand) + ": Two pair"

		elif uniqueCount == 4:
			if max(cardCount.values()) == 2:
				points = 2 #one pair (4 uniques and 2 are the same)
				print str(hand) + ": One pair"

		elif uniqueCount == 5:
			points = 1 #high card 
			print str(hand) + ": High card"

		#print out the values of the cards in order from greatest to least with 2 digits for each card in order to generate a point value
		sorted_cardCount = sorted(cardCount.iteritems(), key=operator.itemgetter(1,0), reverse=True)
		for keyval in sorted_cardCount:
			if keyval[1] != 0:
				points = int(str(points) + (keyval[1] * str(keyval[0]).zfill(2)))

		return points

	def convert_score(self, score):

		return "Royal Flush"

	#a hand is a straight if, when sorted, the current card's rank + 1 is the same as the next card
	def is_straight(self,hand):
		values = []
		for card in hand.hand:
			values.append(card.rank)

		values.sort()

		for i in xrange(0,4):
			if values[i] + 1 != values[i + 1]:
				return False
		return True

	#a hand is a flush if all the cards are of the same suit
	def is_flush(self,hand):
		suit = hand.hand[0].suit
		for card in hand.hand:
			if card.suit != suit:
				return False
		return True