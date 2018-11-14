import random
print( random.randrange(6) ) #random class에 randrange라는 함수를 소환한다. (0~5 사이의 숫자를 random하게 봅아냄, randrange(1,7)하면 1~6 사이에서 random하게 가져온다.)
lst = range(1, 14) # list(lst)  >> [1,2,3,4,...,13]
print( random.shuffle(lst) )  # shuffle: 섞어버리는 것
lst = list(range(1, 14))
print(lst, type(lst))
random.shuffle(lst)
print(lst)

class Card:
	def __init(self, m, n):
		self.m = m  #모양
		self.n = n  #숫자
cards = [
	Card('Clover', 3),
	Card('Spade', 9),
	Card('Heart', 13),
	....
]
random.shuffle(cards) #cards (lisit)가 shuffled

# dir(random) 하면 random 모듈에 있는 함수 다 보여준다. 