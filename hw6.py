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
        if a > (len(table) / 3) and grades[x - 1][3] == "A":
            grades[x].append("B")
        else:
            grades[x].append("A")
            a += 1
    elif x < (2 *(len(table) / 2)):
        if b > (2 * (len(table) / 2)) and grades[x -1][3] == "B":
            if table[x - 1][-1] == "E":
                
            else:    
                grades[x].append("C")
    elif x >= ((len(table) % 10) - 1):
        grades[x].append("F")
    else:
        grades[x].append("C")

print "\nGrades:\n"

for x in grades:
    print x

print "\nCounts:\n"
print a
print b

    





