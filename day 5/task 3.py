dice = [1, 2, 3, 4, 5, 6]
sum_A = 0
total_A = 0
sum_AandB = 0
total_AandB = 0

for d1 in dice:
    for d2 in dice:
        for d3 in dice:
            if d1 + d2 > 8:
                sum_A += d1 + d2 + d3
                total_A += 1
                if d3 % 2 != 0:
                    sum_AandB += d1 + d2 + d3
                    total_AandB += 1

E_A = sum_A / total_A
E_AandB = sum_AandB / total_AandB

print(f"Conditional Expectation of the sum of all three dice given A: {E_A:.2f}")
print(f"Conditional Expectation of the sum of all three dice given both A and B: {E_AandB:.2f}")
