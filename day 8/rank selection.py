def RankSelection(ind):
    sort_ind = sorted(ind, key=lambda x: x[1])
    rank_sum = sum(i + 1 for i in range(len(sort_ind)))
    for index, (ind, fitness) in enumerate(sort_ind):
        rank = index + 1
        #ind_fit = (rank / rank_sum) * 100
        rank_fitness = (rank / rank_sum) * 100
        print(f"Individual: {ind}, Original Fitness: {fitness}, Rank Fitness: {rank_fitness:.2f}")
    return sort_ind

#example (individual, fitness)
individuals = [('A', 5), ('B', 2), ('C', 0.5), ('D', 1.5), ('E', 1)]
RankSelection(individuals)
