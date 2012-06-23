class Hand:
	hand = []
	Name = "Hand"
	def __init__(self, cards):
		self.hand = cards

	def rank(self,hand):
		if straight(hand) and flush(hand):
			return [10,max(hand)]
		if kind(4,hand):
			return [9,kind(4,hand)]
		if kind(3,hand) and kind(2,hand):
			return [8, kind(3,hand),kind(2,hand)]
		if flush(hand):
			return [7,hand]
		if straight(hand):
			return [6, max(hand)]
		if kind(3,hand):
			return [5, kind(3,hand)]
		if len(kind(2,hand)) == 3:
			return [4, kind(2,hand)]
		if kind(2,hand):
			return [3, kind(2,hand)]
		else:
			return max(hand)

	def straight(self,hand):
		vals = [i[0] for i in hand]
		for i in range(3):
			if vals[i] + 1 != vals[i+1]:
				return false
		return true

	def flush(self,hand):
		suits = [i[1] for i in hand]
		for suit in suits:
			if suit != suits[0]:
				return false
		return true

	def kind(self,of,hand):
		vals = [i[0] for i in hand]
		toret = []
		inc = [False]*5
		for i in range(5-of-1):
			start = True
			for j in range(i+1,i+of):
				if vals[j] != vals[i]:
					start = False
					break

			if start:
				toret.append(vals[i])
				inc[i:i+of] = [True]*of

		a = [vals[j] for j in range(of)]

		return [a for a in toret]
#, [vals[j] for j in range(of) if not inc[j]]]
