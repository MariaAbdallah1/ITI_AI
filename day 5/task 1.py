# What is the probability that half the product of three dice will exceed their sum? 
exceed = 0

for d1 in range(1, 7):
    for d2 in range(1, 7):
        for d3 in range(1, 7):
            product = d1 * d2 * d3
            sum = d1 + d2 + d3
            if 0.5 * product > sum:
                exceed += 1

probability = exceed / (6**3)
print(f"The probability is: {probability:.2f}")
