import numpy as np

class OneMax:
    def __init__(self, length, max_iter):
        self.length = length
        self.max_iter = max_iter
        self.current = np.random.randint(2, size=length)
        self.best_solution = self.current.copy()
        self.best_score = self.score(self.current)
    
    def score(self, solution):
        return np.sum(solution)
    
    def generate_neighbor(self, solution):
        neighbor = solution.copy()
        i = np.random.randint(self.length)
        neighbor[i] = 1 - neighbor[i]
        return neighbor
    
    def hill_climb(self):
        for i in range(self.max_iter):
            neighbor = self.generate_neighbor(self.current)
            neighbor_score = self.score(neighbor)
            
            if neighbor_score > self.best_score:
                self.current = neighbor
                self.best_solution = neighbor
                self.best_score = neighbor_score
            print(f"{i+1}: Score = {self.best_score}")

            if self.best_score == len(neighbor):
                print(f"{i+1}: Number of ones in the best solution = {self.best_score}")
                return self.best_solution, self.best_score            

if __name__ == "__main__":
    length = 10
    iter = 100
    
    onemax = OneMax(length=length, max_iter=iter)
    best_solution, best_score = onemax.hill_climb()
    print("Best solution (bitstring):", best_solution)