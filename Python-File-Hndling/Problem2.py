# From a file containing numbers seperated by comma, print the count of the even numbers

with open("Python-File-Hndling/Problem2.txt", "r") as f:
    # Way 1
    data = [num.strip() for num in f.read().split(",")]

    # Way 2
    # data = f.read().split(",")
    # for i, num in enumerate(data):
    #     data[i] = num.strip()

counter = 0
for num in data:
    number = int(num)
    if number % 2 == 0:
        counter += 1
print(f"There are {counter} even numbers in the file")
