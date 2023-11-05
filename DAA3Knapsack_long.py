#3- knapsack

# A utility function that returns the maximum of two integers
def max(a, b):
    return a if a > b else b

# Returns the maximum value that can be put in a knapsack of capacity W
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in a bottom-up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    return K[n][W]

if __name__ == "__main__":
    print("Enter the number of items in a Knapsack:")
    n = int(input())
    val = []
    wt = []
    for i in range(n):
        print(f"Enter value and weight for item {i}:")
        v, w = map(int, input().split())
        val.append(v)
        wt.append(w)

    print("Enter the capacity of the knapsack:")
    W = int(input())
    print("Maximum Profit:", knapSack(W, wt, val, n))
