try:
    with open("app/happy.txt", mode="r") as file:
        print(file.readline())
except FileNotFoundError as err:
    print("file doesn't exist")
    raise err
except IOError as err:
    print("io error")
    raise err