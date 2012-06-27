class Pot:
	bets = []
	state = []

	def __init__(self,players,blind):
		state = [0]*len(players)
		bets = [0]*len(players)
		bets[0] = blind/2
		bets[1] = blind
		return
