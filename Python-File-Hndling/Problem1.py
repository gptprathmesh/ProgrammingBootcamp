# Create a new file “practice.txt” using python. Add the following data in it:

# Hi everyone
# we are learning File I/O
# using Java.
# I like programming in Java.

# WAF that replace all occurrences of “java” with “python” in above file.
# Search if the word “learning” exists in the file or not.
# WAF to find out that in which line of the file does the world "learning" exists. Print -1 if not found


with open("Python-File-Hndling/practice.txt", "w") as f:
    f.write(
        "Hi everyone\nWe are learning File I/O using Java\nI like Programming in Java"
    )

with open("Python-File-Hndling/practice.txt", "r") as f:
    data = f.read()
    data = data.replace("Java", "Python", 3)
    print(f"\n{data}\n")

with open("Python-File-Hndling/practice.txt", "r") as f:
    data = f.read()
    if "learning" in data:
        print('Yes, "Learning" exists in the file')
    else:
        print('No, "Learning" doesn\'t exist in the file')

with open("Python-File-Hndling/practice.txt", "r") as f:
    found = False
    counter = 0
    while not found:
        counter += 1
        if "learning" in f.readline():
            print(f'"Learning" found in {counter} line of the file.')
            found = True
    if not found:
        print(f'"Learning" not found in the file')
