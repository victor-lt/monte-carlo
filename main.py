import random
from math import floor
import csv

#TO DO LIST: self.ask_insurance(), check well working of self.check_blackjack_dealer()

#strategy array, line index = player's hand value - 4, column index = dealer's up card value - 2
#the array is a tuple, first value is the action when the player's hand is hard, second is he has a soft hand
basic_strategy = [

[[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None], [ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None]], #4
[[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None], [ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None]], #5
[[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None], [ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None]], #6
[[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None], [ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None]], #7
[[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None], [ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None]], #8
[[ 'H', None],[ 'D', None],[ 'D', None],[ 'D', None],[ 'D', None], [ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None],[ 'H', None]], #9
[[ 'D', None],[ 'D', None],[ 'D', None],[ 'D', None],[ 'D', None], [ 'D', None],[ 'D', None],[ 'D', None],[ 'H', None],[ 'H', None]], #10
[[ 'D', None],[ 'D', None],[ 'D', None],[ 'D', None],[ 'D', None], [ 'D', None],[ 'D', None],[ 'D', None],[ 'D', None],[ 'D', None]], #11
[[ 'H', 'H'],[ 'H', 'H'],[ 'S', 'H'],[ 'S', 'H'],[ 'S', 'H'], [ 'H', 'H'],[ 'H', 'H'],[ 'H', 'H'],[ 'H', 'H'],[ 'H', 'H']], #12
[[ 'S', 'H'],[ 'S', 'H'],[ 'S', 'H'],[ 'S', 'D'],[ 'S', 'D'], [ 'H', 'H'],[ 'H', 'H'],[ 'H', 'H'],[ 'H', 'H'],[ 'H', 'H']], #13
[[ 'S', 'H'],[ 'S', 'H'],[ 'S', 'H'],[ 'S', 'D'],[ 'S', 'D'], [ 'H', 'H'],[ 'H', 'H'],[ 'H', 'H'],[ 'H', 'H'],[ 'H', 'H']], #14
[[ 'S', 'H'],[ 'S', 'H'],[ 'S', 'D'],[ 'S', 'D'],[ 'S', 'D'], [ 'H', 'H'],[ 'S', 'H'],[ 'H', 'H'],[ 'H', 'H'],[ 'H', 'H']], #15
[[ 'S', 'H'],[ 'S', 'H'],[ 'S', 'D'],[ 'S', 'D'],[ 'S', 'D'], [ 'H', 'H'],[ 'S', 'H'],[ 'H', 'H'],[ 'H', 'H'],[ 'H', 'H']], #16
[[ 'S', 'H'],[ 'S', 'D'],[ 'S', 'D'],[ 'S', 'D'],[ 'S', 'D'], [ 'S', 'H'],[ 'S', 'H'],[ 'S', 'H'],[ 'S', 'H'],[ 'S', 'H']], #17
[[ 'S', 'Ds'],[ 'S', 'Ds'],[ 'S', 'Ds'],[ 'S', 'Ds'],[ 'S', 'Ds'], [ 'S', 'S'],[ 'S', 'S'],[ 'S', 'H'],[ 'S', 'H'],[ 'S', 'H']], #18
[[ 'S', 'S'],[ 'S', 'S'],[ 'S', 'S'],[ 'S', 'S'],[ 'S', 'Ds'], [ 'S', 'S'],[ 'S', 'S'],[ 'S', 'S'],[ 'S', 'S'],[ 'S', 'S']], #19
[[ 'S', 'S'],[ 'S', 'S'],[ 'S', 'S'],[ 'S', 'S'],[ 'S', 'S'], [ 'S', 'S'],[ 'S', 'S'],[ 'S', 'S'],[ 'S', 'S'],[ 'S', 'S']], #20
[[ 'S', 'S'],[ 'S', 'S'],[ 'S', 'S'],[ 'S', 'S'],[ 'S', 'S'], [ 'S', 'S'],[ 'S', 'S'],[ 'S', 'S'],[ 'S', 'S'],[ 'S', 'S']], #21

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

expected_value_array = [[[{}, {}] for _ in range(10)] for _ in range(18)]

#####================= WRITING DATA BLOC ===================#####

def write_simple_expected_value_array(chart, true_count, repetition):
	data_hard = [[element[0][true_count] for element in row] for row in chart]
	data_soft = [[element[1][true_count] for element in row] for row in chart]
	data = data_hard + data_soft
	file = open('simple_strategy chart' + str(true_count) + '-rep=' + str(repetition) + '.csv', 'w', newline='')
	writer = csv.writer(file)
	writer.writerows(data)


#####===========================================================#####

class Blackjack:
	def __init__(self, number_of_decks=6, deck_penetration_ratio=0.6, do_dealer_hits_soft_17=False, is_split_after_split_allowed=True, is_split_after_aces_allowed=False):
		self.number_of_decks = number_of_decks
		self.deck_penetration_ratio = deck_penetration_ratio
		self.do_dealer_hits_soft_17 = do_dealer_hits_soft_17
		self.is_split_after_split_allowed = is_split_after_split_allowed
		self.is_split_after_aces_allowed = is_split_after_aces_allowed and is_split_after_split_allowed
		self.shoe = []
		self.bankroll_value = 0
		self.player = [basic_strategy, basic_strategy_splits, betting_strat, insurance_strat]
		self.dealer_hand = [0, 0]
		self.hole_card = 0
		self.list_of_hands = []
		self.starting_number_of_hands = 2
		self.maximum_number_of_hands = 6

		self.count_value = 0
		self.number_of_cards_left = 0
		self.true_count_value = 0

###-------------------------------------------------------------###
		
		self.expected_value_array = expected_value_array

	def initialize_shoe(self, true_count_value):
		shoe = []
		for _ in range(4*self.number_of_decks):
			for card in range(1, 14):  # value varies from 1 to 13
				if card >= 10:
					shoe.append(10)  # 10, J, Q, K have values of 10
				elif card == 1:
					shoe.append(11)  # Ace has a value of 11
				else:
					shoe.append(value)
		
		#on parcours le sabot pour enlever certaines cartes pour ajuster le true count
		self.count_value = true_count_value*self.number_of_decks
		is_true_count_positive = True if true_count_value >= 0 else False
		number_of_card_removed = 0
		card_index_in_shoe = 0
		while number_of_card_removed <= self.count_value:
			if is_true_count_positive and shoe[card_index_in_shoe] >= 10:
				shoe.pop(card_index_in_shoe)
				i += 1
			elif not is_true_count_positive and shoe[card_index_in_shoe] <= 6:
				shoe.pop(card_index_in_shoe)
				i += 1
			else
				j += 1

		random.shuffle(shoe)
		self.number_of_cards_left = self.number_of_decks*(52 - true_count_value)
		self.true_count_value = true_count_value
		return shoe
		
	def update_count(self, card):
		if card >= 10:
			self.count_value -= 1
		elif card <=6:
			self.count_value += 1
		self.number_of_cards_left -= 1
		self.true_count_value = floor(self.count_value / (self.number_of_cards_left/52) )

	def draw_card(self, hand_index):

		card = self.shoe.pop()

		if card == 11: #update ace count
			self.list_of_hands[hand_index][1] += 1

		# adjust the hand value for encoding
		if self.list_of_hands[hand_index][0] + card > 21:
			if self.list_of_hands[hand_index][1] > 0:
				self.list_of_hands[hand_index][0] += card - 10
				self.list_of_hands[hand_index][1] -= 1
			else:
				self.list_of_hands[hand_index][0] = 100
		else:
			self.list_of_hands[hand_index][0] += card

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
		return self.player[2][max(min(9, self.true_count_value), 0)]

	def deal_newhand(self, bet):
		self.list_of_hands.append([0, 0, False, bet]) #value, ace_count, splittable, bet
		index = len(self.list_of_hands) - 1
		if self.draw_card(index) == self.draw_card(index):
			self.list_of_hands[index][2] = True

	def ask_insurance(self):
		self.insurance_bet = 0
		for hand_index in range(len(self.list_of_hands)):
			if self.true_count_value >= self.player[3]:
				self.insurance_bet += self.list_of_hands[hand_index][3]/2

	def check_blackjack(self, hand_index):
		if self.list_of_hands[hand_index][0] == 21:
			self.list_of_hands[hand_index][0] = -2 # -2 means blackjack
			return True
		else:
			return False

	def check_blackjack_dealer(self):
		if self.dealer_hand[0] == 11:
			self.ask_insurance()
			if self.hole_card == 10:
				for hand_index in range(len(self.list_of_hands)):

					if not self.check_blackjack(hand_index): #bust non blackjack hand
						self.list_of_hands[hand_index][0] == 100

					self.bankroll_value += self.insurance_bet
			else:
				self.bankroll_value -= self.insurance_bet

	def deal_dealer(self, card):
		self.draw_card_dealer(card)
		self.hole_card = self.shoe.pop()

	def split_hand(self, hand_index, paired):
		self.list_of_hands[hand_index][0] = paired
		self.list_of_hands[hand_index][1] //= 2

		self.list_of_hands.insert(hand_index + 1, self.list_of_hands[hand_index].copy())

		if self.is_split_after_split_allowed == True: #if split allowed
			if self.is_split_after_aces_allowed == True or self.list_of_hands[hand_index][0] != 11:
				self.list_of_hands[hand_index][2] == True
				self.list_of_hands[hand_index + 1][2] == True
			else:
				self.list_of_hands[hand_index][2] == False
				self.list_of_hands[hand_index + 1][2] == False
		else:
			self.list_of_hands[hand_index][2] == False
			self.list_of_hands[hand_index + 1][2] == False

		self.draw_card(hand_index)
		self.draw_card(hand_index + 1)

	def player_action(self, hand_index):

		if self.list_of_hands[hand_index][0] > 0: # removes blackjack and bust cases

			soft = 1 if self.list_of_hands[hand_index][1] > 0 else 0
			dealer_index = self.dealer_hand[0] - 2

			if self.list_of_hands[hand_index][2] == True and len(self.list_of_hands) < self.maximum_number_of_hands: #if split is allowed

				if self.list_of_hands[hand_index][1] > 0: # pair of aces case
					paired = 11
				else:
					paired = self.list_of_hands[hand_index][0] // 2

				if self.player[1][paired - 2][dealer_index][0]:
					self.split_hand(hand_index, paired)

			hand_value = self.list_of_hands[hand_index][0]
			if hand_value <= 20:
				player_action = self.player[0][hand_value - 4][dealer_index][soft]

			if hand_value <= 20 and ( player_action == 'D' or player_action == 'Ds' ): # double action
				self.draw_card(hand_index)
				self.list_of_hands[hand_index][3] *= 2
			else:
				while hand_value <= 20 and ( player_action == 'H' or player_action == 'D' ): #keep hitting until player stand
					self.draw_card(hand_index)
					soft = 1 if self.list_of_hands[hand_index][1] > 0 else 0

					hand_value = self.list_of_hands[hand_index][0]
					if hand_value <= 20:
						player_action = self.player[0][hand_value - 4][dealer_index][soft]

	def dealer_action(self):

		self.draw_card_dealer(self.hole_card)

		while self.dealer_hand[0] < 17 or self.do_dealer_hits_soft_17 and self.dealer_hand[1] > 0 and self.dealer_hand[0] == 17:
			self.draw_card_dealer(None)

	def check_winner(self, hand_index):
		hand_value = self.list_of_hands[hand_index][0]
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
		self.list_of_hands = []

		for hand_index in range(self.starting_number_of_hands): #deal player
			self.deal_newhand(self.bet())
			self.check_blackjack(hand_index)

		self.deal_dealer(None) #deal dealer
		self.check_blackjack_dealer()

		for hand_index in range(len(self.list_of_hands)):
			self.player_action(hand_index)

		self.dealer_action()

		for hand_index in range(len(self.list_of_hands)):
			self.bankroll_value += self.list_of_hands[hand_index][3] * self.check_winner(hand_index)

	def play_shoe(self, number_of_hands):
		for i in range(number_of_hands):
			if self.number_of_cards_left < (1 - self.deck_penetration_ratio) * (self.number_of_decks * 52):
				self.shoe = self.initialize_shoe(0)  # Reshuffle if penetration is reached
			self.play_round()

			print(f'	 {(i+1)/number_of_hands*100:.2f}%		|		hands :{(i+1)}/{number_of_hands}', end="\r")
		print('')
		print(f'Final Bankroll : {self.bankroll_value}	 |	 EV : {self.bankroll_value/number_of_hands*100:.2f} %')

###-----------------------------------------------------------------###

	def premade_player_action(self, hand_index, action):
		if self.list_of_hands[hand_index][1] > 0: # pair of aces case
			paired = 11
		else:
			paired = self.list_of_hands[hand_index][0] // 2

		if action == 'Sp':
			self.hand_split(hand_index, paired)
		elif action == 'D':
			self.draw_card(hand_index)
			self.list_of_hands[hand_index][3] *= 2
		elif action == 'H':
			self.draw_card(hand_index)
		else: #stand case
			pass

	def play_premade_hand(self, player_hand, dealer_card, action, true_count):
		self.shoe = self.initialize_shoe(true_count)
		self.list_of_hands = [player_hand.copy()]
		self.dealer_hand = [0, 0]

		self.check_blackjack(0)

		self.deal_dealer(dealer_card) #deal dealer
		self.check_blackjack_dealer()

		if self.list_of_hands[0][0] == 100:
			self.bankroll_value -= self.list_of_hands[0][3]
		elif self.list_of_hands[0][0] == -2:
			self.bankroll_value -= self.list_of_hands[0][3]
		else:
			self.premade_player_action(0, action)

			if self.list_of_hands[0][0] == 100:
				self.bankroll_value -= self.list_of_hands[0][3]
			elif action in ['Sp', 'H', 'D']:
				for hand_index in range(len(self.list_of_hands)):
					hand = self.list_of_hands[hand_index]

					self.bankroll_value += hand[3]*self.expected_value_array[hand[0] - 4][self.dealer_hand[0] - 2][hand[1]][true_count][1]
			else:
				self.dealer_action()
				self.bankroll_value += self.list_of_hands[0][3] * self.check_winner(0)


	def sim_rounds(self, player_hand, dealer_card, action, true_count, repetition):
		self.bankroll_value = 0
		for _ in range(repetition):
			self.play_premade_hand(player_hand, dealer_card, action, true_count)

			self.sim_done += 1
			print(f'	 {self.sim_done/self.sim_number*100:.2f}%		|		hands :{self.sim_done}/{self.sim_number}', end="\r")

		self.ev[action] = self.bankroll_value / repetition

	def sim_actions(self, player_hand, dealer_card, true_count, repetition):
		#self.sim_done = 0
		#self.sim_number = repetition * 3 #TO BE REMOVED
		self.ev = {}
		for action in ['D', 'H', 'S']:
			self.sim_rounds(player_hand, dealer_card, action, true_count, repetition)
		maxi = ['D', self.ev['D']]
		if self.ev['H'] > maxi[1]:
			maxi = ['H', self.ev['H']]
		if self.ev['S'] > maxi[1]:
			maxi = ['S', self.ev['S']]
		self.expected_value_array[player_hand[0] - 4][dealer_card - 2][player_hand[1]][true_count] = maxi

	def sim_chart(self, repetition, true_count_range):
		self.sim_done = 0
		self.sim_number = len(true_count_range) * 18 * 10 * 2 * repetition * 3 
		for true_count in true_count_range:
			for soft_value in range(2):
				for player_value in range(21, 3, -1):
					for dealer_card in range(11, 1, -1):
						self.sim_actions([player_value, soft_value, False, 1], dealer_card, true_count, repetition)

		print(self.expected_value_array)


if __name__ == '__main__':
	repetition = 100
	true_count = 1
	game = Blackjack(number_of_decks=6, deck_penetration_ratio=0.7, do_dealer_hits_soft_17=False)
	#game.play_shoe(number_of_hands=repetition)
	#game.sim_actions([16, 0, False, 1], 10, true_count, 1000)
	game.sim_chart(repetition, [true_count])
	print(game.expected_value_array)
	#write_simple_expected_value_array(game.expected_value_array, true_count, repetition)
