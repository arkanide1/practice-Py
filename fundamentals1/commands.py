
if __name__ == '__main__':
    N = int(input())
    li = []

    while (N != 0):
        #action = list(map(str, input().split()))
        action = input().split()
        if (action[0] == "print"):
            print(li)
        elif (action[0] == "insert"):
            li.insert(int(action[1]), int(action[2]))

        elif (action[0] == "remove"):
            li.remove(int(action[1]))
        elif (action[0] == "append"):
            li.append(int(action[1]))
        elif (action[0] == "sort"):
            li = sorted(li)
        elif (action[0] == "pop"):
            li.pop()
        elif (action[0] == "reverse"):
            li.reverse()
        N -= 1


