import random

print("Random integer (1-0):", random.randint(1,1))
print("Random float (0-1):", random.random())

colours = ['red', 'green', 'blue', 'yellow']
print("Random colours:", random.choice(colours))
random.shuffle(colours)
print("Shuffled colors", colours)
print("Sample 2 unique numbers:", random.sample(range(10),2))
print("Two random choices with replacement:", random.choice(colours))
print("Gaussian random(mean = 0, std= 1)")
