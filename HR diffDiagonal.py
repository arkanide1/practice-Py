
def diagonalDifference(arr):
    # Write your code here
    diagonal = [0, 0]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                diagonal[0] += arr[i][j]
            if j == len(arr) - i-1:
                diagonal[1] += arr[i][j]

    return abs(diagonal[0]-diagonal[1])


arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]

print(diagonalDifference(arr))
