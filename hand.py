class Hand:
	'''Each player has a hand, which consists of two hole or pocket cards. These cards are unknown to the other players, and can be used with the community cards to make the best hand possible. The hand class takes every combination of the seven possible cards and ranks it.'''
	hand = []
	Name = "Hand"

	def __init__(self, cards):
		'''Initialized with hole cards.'''
		self.hand = cards

	def combine(self, cards):
		'''This method takes up to 7 cards and returns every possible combination.'''
		combs = []
		lim = len(cards)
		for i in range(lim):
			for j in range(i+1,lim):
				for k in range(j+1,lim):
					for l in range(k+1,lim):
						for m in range(l+1,lim):
							combs.append(sorted([cards[i],cards[j],\
								cards[k],cards[l],cards[m]]))
		return combs

	def highest(self,community):
		'''Returns the highest possible hand.'''
		opts = self.combine(community+self.hand)
		possible = [opts[i] for i in range(len(opts))]
		return max(possible,key=self.rank)
		#ranks = sorted([rank(self.hand + opts[i]) for i in len(opts)])

	def rank(self,hand):
		'''Ranks hands, and then adds kickers or tiebreakers.'''
		if self.straight(hand) and self.flush(hand):
			return [10,max(hand)[0]]
		if self.kind(4,hand):
			return [9,self.kind(4,hand)]
		if self.kind(3,hand) and self.kind(2,hand):
			return [8, self.kind(3,hand)]
		if self.flush(hand):
			return [7,sorted([i[0] for i in hand],reverse=True)]
		if self.straight(hand):
			return [6, max(hand)[0]]
		if self.kind(3,hand):
			return [5, self.kind(3,hand)]
		if self.kind(2,hand) and len(self.kind(2,hand)) == 3:
			return [4, self.kind(2,hand)]
		if self.kind(2,hand):
			return [3, self.kind(2,hand)]
		else:
			return [2,max(hand)[0]]

	def straight(self,hand):
		'''Checks for a straight.'''
		vals = [i[0] for i in hand]
		for i in range(4):
			if vals[i] - 1 != vals[i+1]:
				return False
		return True

	def flush(self,hand):
		'''Checks the suits for a flush.'''
		suits = [i[1] for i in hand]
		for suit in suits:
			if suit != suits[0]:
				return False
		return True

	def kind(self,of,hand):
		'''Checks if there is any card of which there is exactly 'of' repetitions, and returns the rest of the hand. If there is more than one such card, it will include both.'''
		vals = [i[0] for i in hand]
		toret = []
		inc = [False]*5
		for i in range(5-of+1):
			if inc[i]: continue
			start = True
			for j in range(i+1,i+of):
				if vals[j] != vals[i] or inc[j]:
					start = False
					break

			if vals[i] == vals[i-1]: start = False
			elif i+of < 5 and vals[i] == vals[i+of]:
				start = False

			if start:
				toret.append(vals[i])
				inc[i:i+of] = [True]*of

		if len(toret) == 0: return

		return [a for a in toret] +\
			[[vals[j] for j in range(len(vals)) if not inc[j]]]

	def getcards(self):
		'''Getter method to be used only by player.'''
		return self.hand
