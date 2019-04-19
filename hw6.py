with open("input.txt") as file:
    data = file.read()

digits = int(filter(str.isdigit, data))
print digits
