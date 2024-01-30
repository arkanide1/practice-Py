file= open("file.txt")

print(file.read())
file.seek(0)
print(file.read())
# seek() to reset the file position indecator
# readline() for reading line by line 
# readlines() gives a list of the lines
file.seek(0)
print(file.readlines())

file.close()