import numpy as np

class shift_schedule:
    def __init__(self, no_employees, no_shifts, available, preferences, max_iterations):
        self.no_employees = no_employees
        self.no_shifts = no_shifts
        self.available = available
        self.preferences = preferences
        self.max_iterations = max_iterations
        self.current_schedule = np.random.randint(0, no_employees, size=no_shifts)
        self.current_cost = self.cost(self.current_schedule)

    def cost(self, schedule):
        cost = 0
        for shift in range(self.no_shifts):
            emp = schedule[shift]
            if emp not in self.available[shift]:
                cost += 1
            if self.preferences[shift][emp] > 1:
                cost += 1
        return cost

    def generate_neighbor(self, schedule):
        neighbor = schedule.copy()
        i1, i2 = np.random.choice(self.no_shifts, 2, replace=False)
        neighbor[i1], neighbor[i2] = neighbor[i2], neighbor[i1]
        return neighbor

    def run(self):
        for i in range(self.max_iterations):
            neighbor = self.generate_neighbor(self.current_schedule)
            neighbor_cost = self.cost(neighbor)
            if neighbor_cost < self.current_cost:
                self.current_schedule = neighbor
                self.current_cost = neighbor_cost
                print(f"Iteration {i+1}: Cost = {self.current_cost}")
        return self.current_schedule, self.current_cost

if __name__ == "__main__":
    no_employees = 10
    no_shifts = 20
    available = [list(range(no_employees)) for _ in range(no_shifts)]
    preferences = [np.random.randint(0, 10, no_employees) for _ in range(no_shifts)]

    schedule = shift_schedule(no_employees,no_shifts, available, preferences, 1000)
    best_schedule, best_cost = schedule.run()
    print("Best schedule:", best_schedule)
    print("Cost of best schedule:", best_cost)
