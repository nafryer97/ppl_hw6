# Noah Fryer 113387301
# CS 3323 PPL 
# Homework 6


with open("input.txt", "r") as file: #Open the file in a context and close it when context is finished
    input = file.read() #read file into a var

data = input.split() #split the data into a list separated by whitespace

table = [] #this will be a list of lists

for x in range(0, len(data)): #separates data into matrices delimited by ID numbers
    if len(data[x]) == 9 and data[x].isdigit():
        table.append(data[x:x+5]) #append relevant data (we don't care about location info)

table.sort(key=lambda x: x[-2], reverse=True) #sort by score, descending order

grades = []

a = 0 #used for counting
b = 0 #used for counting

#Control flow for assigning grades
for x in range(0, len(table)):
    grades.append(table[x][0:3])
    if x < ((len(table) / 3) + 1): #first n/3 students receive A
        if a >= (len(table) / 3) and table[x - 1][-2] == table[x][-2]:
            if table[x][-1] == "E" and table[x - 1][-1] == "L": #if there is a tie
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
        if b >= (2 * (len(table) / 3)) and table[x - 1][-2] == table[x][-2]: # 2 * n/3 receive Bs
            if table[x][-1] == "E" and table[x - 1][-1] == "L": #if there is a tie
                grades[x].append("B")
                grades[x - 1][-1] = "C"
        else:    
                grades[x].append("B")
                b += 1
    elif x >= ((len(table) % 10) - 1): #bottom 10% receive F
        if table[x][-2] == table[x - 1][-2]:
            if table[x][-1] == "E":
                grades[x].append("C")
                grades[x -1][-1] = "F"
            elif table[x][-1] == "L":
                grades.append("F")
        else: 
            grades.append("F")
    else: #all others receive C or D depending on eagerness
        if table[x][-1] == "E":
            grades[x].append("C")
        else:
            grades[x].append("D")

grades.sort(key=lambda x: x[-2]) #sort by last name

with open("output.html", "w") as output: #write to HTML file
    output.write("<!DOCTYPE html>\n<html>\n<head>\n</head>\n<body>\n<table border=\"1\">\n")
    for x in grades:
        output.write("\n<tr>")
        for y in x:
            output.write("\n<td>")
            output.write(str(y))
            output.write("</td>")
        output.write("\n</tr>\n")
    output.write("\n</table>\n</body>\n</html>\n")
    





