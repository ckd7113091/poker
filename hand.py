class Hand:
	hand = []
	Name = "Hand"
	def __init__(self, cards):
		self.hand = cards

	def combine(self, cards):
		combs = []
		for i in range(7):
			for j in range(i+1,7):
				for k in range(j+1,7):
					for l in range(j+1,7):
						for m in range(l+1,7):
							combs.append(sorted([cards[i],cards[j],\
								cards[k],cards[l],cards[m]]))
		return combs

	def highest(self,community):
		opts = self.combine(community+self.hand)
		possible = [opts[i] for i in range(len(opts))]
		return max(possible,key=self.rank)
		#ranks = sorted([rank(self.hand + opts[i]) for i in len(opts)])

	def rank(self,hand):
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
		vals = [i[0] for i in hand]
		for i in range(4):
			if vals[i] - 1 != vals[i+1]:
				return False
		return True

	def flush(self,hand):
		suits = [i[1] for i in hand]
		for suit in suits:
			if suit != suits[0]:
				return False
		return True

	def kind(self,of,hand):
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

		return [a for a in toret] + [[vals[j] for j in range(len(vals)) if not inc[j]]]
