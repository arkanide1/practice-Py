# instead of opening and closing files like this there is another mtd

# file= open("file.txt")

# print(file.read())

# file.close()

# normally when you open a file the default mode= "r"

with open("app/sad.txt", mode="w") as file:

    print(file.write(":("))

with open("app/sad.txt", mode="r") as file:
    print(file.readline())
