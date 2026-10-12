f = open("Python-File-Hndling/text.txt")

data = f.read()
print(data.split("\n"))

f.close()
