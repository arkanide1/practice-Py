def plusMinus(arr):
    # Write your code here
    Sums = [0, 0, 0]
    Ratio = [0, 0, 0]
    for _ in arr:
        if (_ > 0):
            Sums[0] += 1
        elif (_ < 0):
            Sums[1] += 1
        else:
            Sums[2] += 1
    for i in range(3):
        Ratio[i] = Sums[i]/len(arr)
        print(format(Ratio[i], '.6f'))


arr = [1, 1, 0, -1, -1]
plusMinus(arr)