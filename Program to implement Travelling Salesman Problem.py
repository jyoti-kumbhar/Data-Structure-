from itertools import permutations
import math

class TSP:
    def __init__(self, distance_matrix, forts):
        self.distance_matrix = distance_matrix
        self.num_cities = len(distance_matrix)
        self.forts = forts

    def calculate_total_distance(self, route):
        """Calculate the total distance of a given route."""
        total_distance = 0
        for i in range(len(route) - 1):
            total_distance += self.distance_matrix[route[i]][route[i+1]]
        # Add distance to return to the starting city
        total_distance += self.distance_matrix[route[-1]][route[0]]
        return total_distance

    def solve(self):
        """Solve the TSP using brute force."""
        min_distance = math.inf
        best_route = None
        # Generate all possible permutations of cities (excluding the starting city)
        for perm in permutations(range(self.num_cities)):
            current_distance = self.calculate_total_distance(perm)
            if current_distance < min_distance:
                min_distance = current_distance
                best_route = perm
        return best_route, min_distance

def print_route(route, distance):
    """Print the optimal route and its distance."""
    route_str = " -> ".join(f"{user_list[i]}" for i in route)
    print(f"Optimal Route: {route_str}")
    print(f"Total Distance: {distance}")

# Example usage
if __name__ == "__main__":
    # Take input as a comma-separated string and split into a list
    user_input = input("Enter places separated by commas: ")
    user_list = user_input.split(",")
# Strip any extra spaces from the elements
    user_list = [element.strip() for element in user_list]
    print("User List:", user_list)
# Input the number of rows
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
# Initialize matrix
    distance_matrix = []
# Input each row as comma-separated values
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1} values separated by commas: ").split(',')))
        if len(row) == cols:
            distance_matrix.append(row)
        else:
            print(f"Error: Please enter exactly {cols} values.")
    print("Matrix:")
    for row in distance_matrix:
        print(row)
    tsp = TSP(distance_matrix, user_list)
    best_route, min_distance = tsp.solve()
    print_route(best_route, min_distance)
