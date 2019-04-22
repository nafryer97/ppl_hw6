with open("input.txt") as file:
    input = file.read()

data = input.split()

table = []

for x in range(0, len(data)):
    if len(data[x]) == 9 and data[x].isdigit():
        table.append(data[x:x+5])
        
print "\nTable:\n"

for x in table:
    print x

print "\nSorted:\n"

table.sort(key=lambda x: x[-2], reverse=True)

for x in table:
    print x

grades = []

a = 0
b = 0

for x in range(0, len(table)):
    grades.append(table[x][0:3])
    if x < (len(table) / 3):
        if a > (len(table) / 3) and table[x - 1][-1] == "L":
            if table[x][-1] == "E":
                grades[x].append("A")
                grades[x - 1][-1] = "B"
                b += 1
            else:
                grades[x].append("A")
                a += 1
        else:
                grades[x].append("A")
                a += 1
    elif x < (2 *(len(table) / 3)):
        if b > (2 * (len(table) / 3)) and table[x -1][-1] == "L":
            if table[x][-1] == "E":
                grades[x].append("B")
                grades[x - 1][-1] = "C"
        else:    
                grades[x].append("B")
                b += 1
    elif x >= ((len(table) % 10) - 1):
        if table[x][-2] == table[x - 1][-2]:
            if table[x][-1] == "E":
                grades[x].append("C")
                grades[x -1][-1] = "F"
            elif table[x][-1] == "L":
                grades.append("F")
        else:
            grades.append("F")
    else:
        if table[x][-1] == "E":
            grades[x].append("C")
        else:
            grades[x].append("D")

print "\nGrades:\n"

for x in grades:
    print x

print "\nCounts:\n"
print a
print b

grades.sort(key=lambda x: x[-2])

print"\nSorted by last name:\n"

for x in grades:
    print x    





