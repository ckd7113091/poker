class Pot:
	bets = []
	state = []

	def __init__(self,players,blind):
		state = [0]*len(players)
		bets = [0]*len(players)
		bets[0] = blind/2
		bets[1] = blind
		return

	def fold(self,players,index):
		players[index].fold()
		state[index] = 2

	def cc(self,players,index):
		bets[index] = bets[index-1]
		return

	def raise(self,players,index,value):
		low = []
		plow = []
		i = 0

		while i < len(players):
			if players[i].getmoney() < bets[i] + value:
				plow.append(players.pop(i))
				low.append(bets.pop(i))
			else: i += 1

			
