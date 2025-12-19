import random

#TO DO LIST: self.ask_insurance(), check well working of self.check_blackjack_dealer()

basic_strategy = [

[[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None], [ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None]], #4
[[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None], [ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None]], #5
[[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None], [ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None]], #6
[[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None], [ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None]], #7
[[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None], [ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None]], #8
[[ 'H', None],[ 'D', None],[ 'D', None],[ 'D', None],[ 'H', None], [ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None]], #9
[[ 'D', None],[ 'D', None],[ 'D', None],[ 'D', None],[ 'D', None], [ 'D', None],[ 'D', None],[ 'D', None],[ 'H', None],[ 'H', None]], #10
[[ 'D', None],[ 'D', None],[ 'D', None],[ 'D', None],[ 'D', None], [ 'D', None],[ 'D', None],[ 'D', None],[ 'D', None],[ 'H', None]], #11
[[ 'H', 'H'],[ 'H', 'H'],[ 'S', 'H'],[ 'S', 'H'],[ 'S', 'H'], [ 'H', 'H'],[ 'H', 'H'],[ 'H', 'H'],[ 'H', 'H'],[ 'H', 'H']], #12
[[ 'S', 'H'],[ 'S', 'H'],[ 'S', 'H'],[ 'S', 'D'],[ 'S', 'D'], [ 'H', 'H'],[ 'H', 'H'],[ 'H', 'H'],[ 'H', 'H'],[ 'H', 'H']], #13
[[ 'H', 'H'],[ 'H', 'H'],[ 'S', 'H'],[ 'S', 'D'],[ 'S', 'D'], [ 'H', 'H'],[ 'H', 'H'],[ 'H', 'H'],[ 'H', 'H'],[ 'H', 'H']], #14
[[ 'S', 'H'],[ 'S', 'H'],[ 'S', 'D'],[ 'S', 'D'],[ 'S', 'D'], [ 'H', 'H'],[ 'S', 'H'],[ 'H', 'H'],[ 'H', 'H'],[ 'H', 'H']], #15
[[ 'S', 'H'],[ 'S', 'H'],[ 'S', 'D'],[ 'S', 'D'],[ 'S', 'D'], [ 'H', 'H'],[ 'S', 'H'],[ 'H', 'H'],[ 'H', 'H'],[ 'H', 'H']], #16
[[ 'S', 'H'],[ 'S', 'D'],[ 'S', 'D'],[ 'S', 'D'],[ 'S', 'D'], [ 'S', 'H'],[ 'S', 'H'],[ 'S', 'H'],[ 'S', 'H'],[ 'S', 'H']], #17
[[ 'S', 'Ds'],[ 'S', 'Ds'],[ 'S', 'Ds'],[ 'S', 'Ds'],[ 'S', 'Ds'], [ 'S', 'S'],[ 'S', 'S'],[ 'S', 'H'],[ 'S', 'H'],[ 'S', 'H']], #18
[[ 'S', 'S'],[ 'S', 'S'],[ 'S', 'S'],[ 'S', 'S'],[ 'S', 'Ds'], [ 'S', 'S'],[ 'S', 'S'],[ 'S', 'S'],[ 'S', 'S'],[ 'S', 'S']], #19
[[ 'S', 'S'],[ 'S', 'S'],[ 'S', 'S'],[ 'S', 'S'],[ 'S', 'S'], [ 'S', 'S'],[ 'S', 'S'],[ 'S', 'S'],[ 'S', 'S'],[ 'S', 'S']], #20

]

basic_strategy_splits = [

[[True], [True], [True], [True], [True], [True], [False], [False], [False], [False]], #22
[[True], [True], [True], [True], [True], [True], [False], [False], [False], [False]], #33
[[False], [False], [False], [True], [True], [False], [False], [False], [False], [False]], #44
[[False], [False], [False], [False], [False], [False], [False], [False], [False], [False]], #55
[[True], [True], [True], [True], [True], [False], [False], [False], [False], [False]], #66
[[True], [True], [True], [True], [True], [True], [False], [False], [False], [False]], #77
[[True], [True], [True], [True], [True], [True], [True], [True], [True], [True]], #88
[[True], [True], [True], [True], [True], [False], [True], [True], [False], [False]], #99
[[False], [False], [False], [False], [False], [False], [False], [False], [False], [False]], #TT
[[True], [True], [True], [True], [True], [True], [True], [True], [True], [True]], #AA

]

betting_strat = []

#####===========================================================#####

class Blackjack:
	def __init__(self, num_decks=6, deck_penetration=0.6, dealer_hits_soft_17=False, split_after_split=True, split_after_aces=True):
		self.num_decks = num_decks
		self.deck_penetration = deck_penetration
		self.dealer_hits_soft_17 = dealer_hits_soft_17
		self.split_after_split = split_after_split
		self.split_after_aces = split_after_aces
		self.shoe = self.initialize_shoe()
		self.bankroll = 0
		self.player = [basic_strategy, basic_strategy_splits, betting_strat, False]
		self.dealer_hand = [0, 0]
		self.hole_card = 0
		self.hands = []
		self.starting_num_hands = 2
		self.max_num_hands = 6 #TO BE CHANGED

	def initialize_shoe(self):
		shoe = []
		for _ in range(self.num_decks):
			for value in range(1, 14):  # 1 to 13
				if value > 10:
					shoe.append(10)  # 10, J, Q, K
				elif value == 1:
					shoe.append(11)  # Ace is considered 11
				else:
					shoe.append(value)
		random.shuffle(shoe)
		return shoe

	def draw_card(self, hand_index):

		card = self.shoe.pop()

		if card == 11: #update ace count
			self.hands[hand_index][1] += 1

		# adjust the hand value for encoding
		if self.hands[hand_index][0] + card > 21:
			if self.hands[hand_index][1] > 0:
				self.hands[hand_index][0] += card - 10
				self.hands[hand_index][1] -= 1
			else:
				self.hands[hand_index][0] = 100
		else:
			self.hands[hand_index][0] += card
		print('le joueur pioche un', card)
		print('la main devient :', self.hands[hand_index])
		return card

	def draw_card_dealer(self, card):

		if card == None: #if a card is in argument, add this card to hand. Actually only for the holecard
			newcard = self.shoe.pop()
		else:
			newcard = card

		if newcard == 11: #update ace count
			self.dealer_hand[1] += 1

		# adjust the hand value for encoding
		if self.dealer_hand[0] + newcard > 21:
			if self.dealer_hand[1] > 0:
				self.dealer_hand[0] += newcard - 10
			else:
				self.dealer_hand[0] = 100 #100 means bust
		else:
			self.dealer_hand[0] += newcard
		print('le dealer pioche un', newcard)
		return newcard

	def bet(self):
		return 1 #NEEDS TO BE CHANGED

	def deal_newhand(self, bet):
		self.hands.append([0, 0, False, bet]) #value, ace_count, splittable, bet
		index = len(self.hands) - 1
		if self.draw_card(index) == self.draw_card(index):
			self.hands[index][2] = True
			print('il y a split')

	def ask_insurance(self):
		for hand_index in range(len(self.hands)):
			if self.player[3] == True:
				self.insurance_bet += self.hands[hand_index][3]

	def check_blackjack(self, hand_index):
		if self.hands[hand_index][0] == 21:
			self.hands[hand_index][0] = -2 # -2 means blackjack
			return True
		else:
			return False

	def check_blackjack_dealer(self):
		if self.dealer_hand[0] == 11:
			self.ask_insurance()
			if self.hole_card == 10:
				for hand_index in range(len(self.hands)):
					if not self.check_blackjack(hand_index):
						self.hands[hand_index][0] == 100

	def deal_dealer(self):
		self.draw_card_dealer(None)
		self.hole_card = self.shoe.pop()

	def split_hand(self, hand_index, paired):
		self.hands[hand_index][0] = paired
		self.hands[hand_index][1] //= 2

		self.hands.insert(hand_index + 1, self.hands[hand_index].copy())

		if self.split_after_split == True: #if split allowed
			if self.split_after_aces == True or self.hands[hand_index][0] != 11:
				self.hands[hand_index][2] == True
				self.hands[hand_index + 1][2] == True
			else:
				self.hands[hand_index][2] == False
				self.hands[hand_index + 1][2] == False
		else:
			self.hands[hand_index][2] == False
			self.hands[hand_index + 1][2] == False

		self.draw_card(hand_index)
		self.draw_card(hand_index + 1)

	def player_action(self, hand_index):

		print('la main est :', self.hands[hand_index])

		if self.hands[hand_index][0] > 0: # removes blackjack and bust cases

			soft = 1 if self.hands[hand_index][1] > 0 else 0
			dealer_index = self.dealer_hand[0] - 2

			if self.hands[hand_index][2] == True:

				if self.hands[hand_index][1] > 0: # pair of aces case
					paired = 11
				else:
					paired = self.hands[hand_index][0] // 2

				if self.player[1][paired - 2][dealer_index][0]:
					self.split_hand(hand_index, paired)
					print('SPLIT')

			if self.hands[hand_index][0] <= 20 and self.player[0][self.hands[hand_index][0] - 4][dealer_index][soft] == 'D': # double action
				self.draw_card(hand_index)
				self.hands[hand_index][3] *= 2
				print('DOUBLE')
			else:
				while self.hands[hand_index][0] <= 20 and self.player[0][self.hands[hand_index][0] - 4][dealer_index][soft] == 'H': #keep hitting until player stand
					self.draw_card(hand_index)
					soft = 1 if self.hands[hand_index][1] > 0 else 0
					print('HIT')

	def dealer_action(self):

		self.draw_card_dealer(self.hole_card)

		while self.dealer_hand[0] < 17 or self.dealer_hits_soft_17 and self.dealer_hand[1] > 0 and self.dealer_hand[0] == 17:
			self.draw_card_dealer(None)
			print('dealer hand :', self.dealer_hand)

	def check_winner(self, hand_index):
		hand_value = self.hands[hand_index][0]
		dealer_value = self.dealer_hand[0]

		if hand_value == -2:
			return 1.5
		elif hand_value == 100:
			return -1
		elif dealer_value == 100 or hand_value > dealer_value:
			return 1
		elif dealer_value == hand_value:
			return 0
		else:
			return -1


	def play_round(self):

		self.dealer_hand = [0, 0] #reset table
		self.hands = []

		for hand_index in range(self.starting_num_hands): #deal player
			self.deal_newhand(self.bet())
			self.check_blackjack(hand_index)

		self.deal_dealer()
		self.check_blackjack_dealer()

		for hand_index in range(len(self.hands)):
			self.player_action(hand_index)

		self.dealer_action()

		for hand_index in range(len(self.hands)):
			self.bankroll += self.hands[hand_index][3] * self.check_winner(hand_index)
			print('tu as gagné : ', self.hands[hand_index][3] * self.check_winner(hand_index))

	def play_shoe(self, number_of_hands):
		for _ in range(number_of_hands):
			if len(self.shoe) < (1 - self.deck_penetration) * (self.num_decks * 52):
				self.shoe = self.initialize_shoe()  # Reshuffle if penetration is reached
				print('reshuffle')
			self.play_round()

if __name__ == '__main__':
	game = Blackjack(num_decks=6, deck_penetration=0.5, dealer_hits_soft_17=False)
	game.play_shoe(number_of_hands=100000)
	print("Final Bankroll:", game.bankroll)
