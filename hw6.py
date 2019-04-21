with open("input.txt") as file:
    data = file.read()

digits = filter(str.isdigit, data)
print digits
