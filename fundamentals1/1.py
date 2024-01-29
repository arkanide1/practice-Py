fname = "file.txt"

try:
    file = open(fname, "r")
    content = file.read()
    print(content, end="")
    file.close()
except:
    print("Error reading file.")
