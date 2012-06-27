from pot import Pot
from hand import Hand
from player import Player
from dealer import Dealer


def run():
	ps = [Player() for i in range(4)]
	d = Dealer()

	hands = d.deal(len(ps))
	for i in range(len(ps)):
		ps[i] = Player(hands[i])

	pot = Pot(ps,10)

	betting(ps,pot)
	return

def betting(play,pot):
	c = 0
	while c != -1:
		for i in range(2,len(play)+2):
			c = -1
			a = raw_input('Action? ')
			if a == 'f':
				pot.fold(play,i%len(play))
				play.pop(i%len(play))
			elif a == 'c':
				pot.cc(play,i%len(play))
			elif a == 'r':
				val = int(raw_input('By? '))
				pot.raisepot(play,i%len(play),val)
				c = 0
			for p in play:
				print p.getbet()

run()		
