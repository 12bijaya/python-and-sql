import random
sister = random.choice(["darpok","brave"])#to chose random
print(f" your sister ia {sister}")
number = random.randint(1,10)#to slect random integer 
print(f"your sister is {number} no {sister} out of 10:")
#shuffle function
cards = ["Bikash","Bijaya","Kalin"]
random.shuffle(cards)
for card in cards:
    print(card)