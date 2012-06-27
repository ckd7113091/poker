from hand import Hand
from player import Player
from dealer import Dealer


def run():
	ps = [Player() for i in range(3)]
	d = Dealer(ps,10)
	pot = Pot(ps,10)

	hands = d.deal(ps)
	for i in range(len(ps)):
		ps[i] = Player(hands[i])

	print ps[1].gethand()

	betting(ps,pot)
	return

def betting(play,p):
	
