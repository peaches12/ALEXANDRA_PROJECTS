def find_average(gradesList):
    total = 0
    for score in gradesList:
        total += int(score)
    return int(total/len(gradesList))

def little_message(numGrade):
    if 90 <= numGrade <= 100:
        return("Excellent Job!")
    elif 75 <= numGrade <= 89:
        return("Sometimes I get B's")
    elif 60 <= numGrade <= 74:
        return("Whatever.")
    else:
        return("My parents are going to kill me")
    
def space_number(nombre):
    total_space = 25
    return total_space - len(nombre) - 2
# open the files
inFile = open('classgrades.txt','r')
outFile = open('classscores.txt','w')
# you have to write the rest!
        
listedLines = inFile.readlines()
for line in listedLines:
    line = line.strip()
    NameScores = line.split()
    Name = NameScores[0]
    Scores = NameScores[1:len(NameScores)]
    Average = find_average(Scores)
    outFile.write(str(Name) + ' ' * space_number(Name) + str(Average) + '\t' + little_message(Average) + '\n')

outFile.close()

printFile = open('classscores.txt', 'r')
paragraph = printFile.read()
print(paragraph)
    
    
