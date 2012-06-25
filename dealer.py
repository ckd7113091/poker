from random import randint,shuffle

class Dealer:
	deck
	community
	burned

	def __init__(self):
		self.shuffle()
		return

	def int2card(self,num):
		suits = ['C','S','H','D']
		return (num//4+1, suits[num%4])

	def shuffle():
		deck = range(51)
		shuffle(deck)
		return

	def deal(community):
		if len(community) == 0:
			burned.append(deck.pop())
			for i in range(3):
				community.append(deck.pop())
			return community

		if len(community) < 5:
			burned.append(deck.pop())
			community.append(deck.pop())
			return community

		return

	def showdown(players):
		ranks = []
		for player in players:
			ranks.append(player.getrank())

		winner = 0
		tie = []
		for i in range(len(ranks)):
			#Check the rank.
			if ranks[i][0] > ranks[winner][0]:
				winner = i
				tie = []
			elif ranks[i][0] == ranks[winner][0]:
				#If it's a straight flush or a straight, check the high card. 
				#If it's a flush, compare the hands.
				if ranks[i][0] == 10 or ranks[i] == 6:
					if ranks[i][1] > ranks[winner][1]:
						winner = i
						tie = []
					elif ranks[i][1] == ranks[winner][1]:
						tie.append(i)
			#If it's a full house, check the pair.
			elif ranks[i] == 8:
				if ranks[i][2][0] > ranks[winner][2][0]:
					winner = i
					tie = []
				elif ranks[i][2][0] == ransk[winner[2][0]:
					tie.append(i)
			#If it's not a straight, flush, or full house, then check the first card.
			elif ranks[i][1][0] > ranks[winner][1][0]:
				winner = i
				tie = []
			elif ranks[i][1][0] == ranks[winner][1][0]:
				#If the first hands are the same, and it's a four-of-a-kind, tie.
				if ranks[i] == 9:
					tie.append(i)
				#Otherwise, check the card/hand.
				elif ranks[i][1][1] > ranks[winner][1][1]:
					winner = i
					tie = []
				elif ranks[i][1][1] == ranks[winner][1][1]:
					tie.append(i)
