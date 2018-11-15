import random

class Deck:
    def shuffle_cards():
        deck = []
        shape = ["S","D","H","C"]
        number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        for i in range (0,4):
            res_shape = shape[i]
            for n in range (0, 13):
                res_number = number[n]
                card = res_shape + res_number
                deck.append(card)
                random.shuffle(deck)          
        print (deck)
    
    gamers_card []    
    gamers_card = shuffle_cards()

class Part:

    my_card = [] ## 자기가 받는 카드 리스트
    new_card = []

    def card_sum(self):
        return sum(my_card[])

    def receive(self):
        return my_card.extend(new_card)        

    def hit(self):
        return # card.pop

    def stay(self):

    def question(self):
        a = input("카드를 뽑으시겠습니까? (Usage: Yes / No / Stand\n")
        if a == "Yes":
            return #card.pop (새로 카드를 뽑는다.)
        elif a == "No":
            exit() #끝낸다.


class Player(Part):

    def __init__(self):
        self.name = name
    
class Dealer(Part):

    def machine_hit():
        if sum(my_card) > 17:
            #카드 안 받는다
        else:
            #카드 받는다

#---------------Main Flow-------------------
start = input("게임에 참석하시겠습니까? (Usage: Yes / No\n")
if start == "Yes":
    card = gamers_card.pop(1).append(gamers_card.pop(1))           #[].pop type은 str # card []
    print(card)
    elif start == "No":
    print("Bye Bye")
    exit()




    