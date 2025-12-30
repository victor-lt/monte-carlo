import random
from math import floor

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

betting_strat = [0, 1, 5, 10, 20, 30, 30, 30, 30, 30] # bet value for true count from 0 to 9

basic_strategy_betting = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

insurance_strat = 3

ev_chart = 17*[10*[[{}, {}]]]

#####===========================================================#####

class Blackjack:
	def __init__(self, num_decks=6, deck_penetration=0.6, dealer_hits_soft_17=False, split_after_split=True, split_after_aces=False):
		self.num_decks = num_decks
		self.deck_penetration = deck_penetration
		self.dealer_hits_soft_17 = dealer_hits_soft_17
		self.split_after_split = split_after_split
		self.split_after_aces = split_after_aces
		self.shoe = []
		self.bankroll = 0
		self.player = [basic_strategy, basic_strategy_splits, betting_strat, insurance_strat]
		self.dealer_hand = [0, 0]
		self.hole_card = 0
		self.hands = []
		self.starting_num_hands = 2
		self.max_num_hands = 6

		self.count = 0
		self.num_cards_left = 0
		self.true_count = 0

###-------------------------------------------------------------###
		
		self.ev_chart = ev_chart

	def initialize_shoe(self, true_count):
		shoe = []
		for _ in range(4*self.num_decks):
			for value in range(1, 14):  # 1 to 13
				if value > 10:
					shoe.append(10)  # 10, J, Q, K
				elif value == 1:
					shoe.append(11)  # Ace is considered 11
				else:
					shoe.append(value)

		tcount = abs(true_count)
		for _ in range(tcount): #parcours du sabot pour ajuster le compte
			i = 0
			j = 0
			while i < self.num_decks:
				if (true_count >= 0 and shoe[j] >=2 and shoe[j] <= 6) or (true_count <= 0 and shoe[j] >= 10):
					shoe.pop(j)
					i += 1
				j += 1

		random.shuffle(shoe)
		self.count = true_count*self.num_decks
		self.num_cards_left = self.num_decks*(52 - true_count)
		self.true_count = true_count
		return shoe

	def update_count(self, card):
		if card >= 10:
			self.count -= 1
		elif card <=6:
			self.count += 1
		self.num_cards_left -= 1
		val = floor(self.count / max(self.num_cards_left/52, 1))
		self.true_count = val

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

		self.update_count(card)

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
				self.dealer_hand[1] -= 1
			else:
				self.dealer_hand[0] = 100 #100 means bust
		else:
			self.dealer_hand[0] += newcard

		self.update_count(newcard)

		return newcard

	def bet(self):
		return self.player[2][max(min(9, self.true_count), 0)]

	def deal_newhand(self, bet):
		self.hands.append([0, 0, False, bet]) #value, ace_count, splittable, bet
		index = len(self.hands) - 1
		if self.draw_card(index) == self.draw_card(index):
			self.hands[index][2] = True

	def ask_insurance(self):
		self.insurance_bet = 0
		for hand_index in range(len(self.hands)):
			if self.true_count >= self.player[3]:
				self.insurance_bet += self.hands[hand_index][3]/2

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

					if not self.check_blackjack(hand_index): #bust non blackjack hand
						self.hands[hand_index][0] == 100

					self.bankroll += self.insurance_bet
			else:
				self.bankroll -= self.insurance_bet

	def deal_dealer(self, card):
		self.draw_card_dealer(card)
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

		if self.hands[hand_index][0] > 0: # removes blackjack and bust cases

			soft = 1 if self.hands[hand_index][1] > 0 else 0
			dealer_index = self.dealer_hand[0] - 2

			if self.hands[hand_index][2] == True and len(self.hands) < self.max_num_hands: #if split is allowed

				if self.hands[hand_index][1] > 0: # pair of aces case
					paired = 11
				else:
					paired = self.hands[hand_index][0] // 2

				if self.player[1][paired - 2][dealer_index][0]:
					self.split_hand(hand_index, paired)

			hand_value = self.hands[hand_index][0]
			if hand_value <= 20:
				player_action = self.player[0][hand_value - 4][dealer_index][soft]

			if hand_value <= 20 and ( player_action == 'D' or player_action == 'Ds' ): # double action
				self.draw_card(hand_index)
				self.hands[hand_index][3] *= 2
			else:
				while hand_value <= 20 and ( player_action == 'H' or player_action == 'D' ): #keep hitting until player stand
					self.draw_card(hand_index)
					soft = 1 if self.hands[hand_index][1] > 0 else 0

					hand_value = self.hands[hand_index][0]
					if hand_value <= 20:
						player_action = self.player[0][hand_value - 4][dealer_index][soft]

	def dealer_action(self):

		self.draw_card_dealer(self.hole_card)

		while self.dealer_hand[0] < 17 or self.dealer_hits_soft_17 and self.dealer_hand[1] > 0 and self.dealer_hand[0] == 17:
			self.draw_card_dealer(None)

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

		self.deal_dealer(None) #deal dealer
		self.check_blackjack_dealer()

		for hand_index in range(len(self.hands)):
			self.player_action(hand_index)

		self.dealer_action()

		for hand_index in range(len(self.hands)):
			self.bankroll += self.hands[hand_index][3] * self.check_winner(hand_index)

	def play_shoe(self, number_of_hands):
		for i in range(number_of_hands):
			if self.num_cards_left < (1 - self.deck_penetration) * (self.num_decks * 52):
				self.shoe = self.initialize_shoe(0)  # Reshuffle if penetration is reached
			self.play_round()

			print(f'     {(i+1)/number_of_hands*100:.2f}%     |     hands :{(i+1)}/{number_of_hands}', end="\r")
		print('')
		print(f'Final Bankroll : {self.bankroll}     |     EV : {self.bankroll/number_of_hands*100:.2f} %')

###-----------------------------------------------------------------###

	def premade_player_action(self, hand_index, action):
		if self.hands[hand_index][1] > 0: # pair of aces case
			paired = 11
		else:
			paired = self.hands[hand_index][0] // 2

		if action == 'Sp':
			self.hand_split(hand_index, paired)
		elif action == 'D':
			self.draw_card(hand_index)
			self.hands[hand_index][3] *= 2
		elif action == 'H':
			self.draw_card(hand_index)
		else: #stand case
			pass

	def play_premade_hand(self, player_hand, dealer_card, action, true_count):
		self.shoe = self.initialize_shoe(true_count)
		self.hands = [player_hand.copy()]
		self.dealer_hand = [0, 0]

		self.check_blackjack(0)

		self.deal_dealer(dealer_card) #deal dealer
		self.check_blackjack_dealer()
		if self.hands[0][0] == 100:
			self.bankroll -= self.hands[0][3]
		else:
			self.premade_player_action(0, action)

			if action == 'Sp':
				for hand_index in range(len(self.hands)):
					hand = self.hands[hand_index]
					self.bankroll += hand[3]*self.ev_chart[hand[0] - 4][self.dealer_hand[0] - 2][hand[1]][true_count][1]
			else:
				self.dealer_action()
				self.bankroll += self.hands[0][3] * self.check_winner(0)


	def sim_rounds(self, player_hand, dealer_card, action, true_count, repetition):
		self.bankroll = 0
		for _ in range(repetition):
			self.play_premade_hand(player_hand, dealer_card, action, true_count)
		self.ev[action] = self.bankroll / repetition

	def sim_chart(self, repetition, true_count_range):
		sim_number = len(true_count_range) * 17 * 10 * 2 
		sim_done = 0
		for true_count in true_count_range:
			for player_value in range(20, 3, -1):
				for dealer_card in range(11, 1, -1):
					for soft_value in range(2):
						self.ev = {}
						for action in ['D', 'H', 'S']:
							self.sim_rounds([player_value, soft_value, False, 1], dealer_card, action, true_count, repetition)
						maxi = ['D', self.ev['D']]
						if self.ev['H'] > maxi[1]:
							maxi = ['H', self.ev['H']]
						if self.ev['S'] > maxi[1]:
							maxi = ['S', self.ev['S']]
						self.ev_chart[player_value - 4][dealer_card - 2][soft_value][true_count] = maxi

						sim_done += 1
						print(f'     {sim_done/sim_number*100:.2f}%     |     hands :{sim_done}/{sim_number}', end="\r")


		print(self.ev_chart)


if __name__ == '__main__':
	num_of_hands = 100000
	game = Blackjack(num_decks=6, deck_penetration=0.7, dealer_hits_soft_17=False)
	#game.play_shoe(number_of_hands=num_of_hands)
	game.sim_chart(10, [0,1,2,3])