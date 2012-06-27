class Pot:
	bets = []

	def __init__(self,players,blind):
		bets = [0]*len(players)
		bets[0] = blind/2
		bets[1] = blind
