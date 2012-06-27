from hand import Hand
from player import Player
from dealer import Dealer

bets = []
state = []
players = []

def run():
	ps = [Player() for i in range(3)]
	d = Dealer(ps,10)
	hands = d.deal(ps)
	for i in range(len(ps)):
		ps[i] = Player(hands[i])

	betting(ps,bets,state)
	return

def fold(p):
	return
