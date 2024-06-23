

from card import Card

olga = User('Olga')
stefan = User('Stefan')
mark = User('Mark')

olga.sayName()
olga.setAge(28)
olga.sayAge()

card = Card('4561 7896 4561 1236', '28/95', 'Olga O')
olga.addCard(card)
olga.getCard(card).pay(1000)

card.pay(1000)







