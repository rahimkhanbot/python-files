
import random

# random value for 0 to 0.9999 but not 1
value = random.random()
print(value)

# random value in floaating point
val = random.uniform(1,10)
print(val)

values = random.randint(10, 60)
print(values)

greetings = ['Hello', 'Hi', 'Howdy', 'Hola', 'Hey']

greet = random.choice(greetings)
print(greet + ', Rahim!')

colors = ['Red', 'Blue', 'Green', 'Yellow']

result = random.choices(colors, weights = [18, 18, 2, 10], k=10)
print(result)

card = list(range(1, 53))
random.shuffle(card)
print(card)

cards = list(range(1,53))

pick = random.sample(cards, k=5)
print(pick)