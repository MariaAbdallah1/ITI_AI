red = 5
green = 3
total = red + green

# 1. Probability that the first marble drawn is red and the second marble drawn is also red
prob_both_red = (red * (red - 1)) / (total * (total - 1))

# 2. Probability that the second marble drawn is red given that the first marble drawn is green
prob_second_red_when_first_green = (green * red) / (green * (total - 1))

# 3. Probability that the second marble drawn is green given that the first marble drawn is red
prob_second_green_when_first_red = (red * green) / (red * (total - 1))

# Print the probabilities
print(f"1. Probability that both marbles drawn are red: {prob_both_red:.2f}")
print(f"2. Probability that the second marble is red given the first is green: {prob_second_red_when_first_green:.2f}")
print(f"3. Probability that the second marble is green given the first is red: {prob_second_green_when_first_red:.2f}")
