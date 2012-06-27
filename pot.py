class Pot:
	pots = []
	sides = 0
	stake = 10
	state = []

	def __init__(self,players,blind):
		self.state = [0]*len(players)
		self.pots = [0]
		players[0].bet(blind/2)
		players[1].bet(blind)
		return

	def fold(self,players,index):
		players[index].fold()
		return

	def cc(self,players,index):
		if self.sides == 0:
			self.pots[self.state[index]] += players[index].bet(self.stake)	
		return

	def raisepot(self,players,index,value):
		self.stake += value
		players[index].bet(self.stake)
		return
