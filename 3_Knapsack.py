
# Aim: Solve the 0/1 Knapsack problem using
# dynamic programming.

# Instructions:
# 1. Enter the number of items.
# 2. Enter the weight and profit of each item.
# 3. Enter the knapsack capacity.
# 4. The program calculates maximum profit.

def knapsack(weights, profits, capacity):
    n = len(weights)

    dp = [
        [0] * (capacity + 1)
        for i in range(n + 1)
    ]

    for i in range(1, n + 1):
        for w in range(capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    profits[i - 1]
                    + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )

            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


n = int(input("Enter number of items: "))

weights = []
profits = []

for i in range(n):
    weight = int(input("Enter weight: "))
    profit = int(input("Enter profit: "))

    weights.append(weight)
    profits.append(profit)

capacity = int(input("Enter knapsack capacity: "))

print(
    "Maximum profit:",
    knapsack(weights, profits, capacity)
)

# Time Complexity: O(n * capacity)
# Space Complexity: O(n * capacity)

# Sample Input:
# Items: (5,20), (2,30), (4,15),(3,10)
# Capacity: 7

# Output:
# Maximum profit: 50

# I/P:
# Enter number of items: 4
# Enter weight: 5
# Enter profit: 20
# Enter weight: 2
# Enter profit: 30
# Enter weight: 4
# Enter profit: 15
# Enter weight: 3
# Enter profit: 10
# Enter knapsack capacity: 7

# O/P:
# Maximum profit: 50

# Result: Maximum profit obtained using dynamic programming.

