import numpy as np
import matplotlib.pyplot as plt
import csv

causes = ['OUTRAS', 'COVID', 'INSUFICIENCIA_RESPIRATORIA', 'PNEUMONIA', 'SEPTICEMIA', 'SRAG', 'INDETERMINADA']

for i in range(len(causes)):
    vars()[causes[i]] = 0

firstRow = 1

with open('obitos-2020.csv', newline='') as csvfile:
    originalfile = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in originalfile:
        if firstRow:
            firstRow = 0
        else:
            line = np.array(row)

            if(line.size == 1):
                cause = line[0].split(",")[1]
                number = line[0].split(",")[5]
                vars()[cause] += int(number)
            
            elif(line.size == 2):
                cause = line[0].split(",")[1]
                number = line[1].split(",")[2]
                vars()[cause] += int(number)
            
            elif(line.size == 3):
                cause = line[0].split(",")[1]
                number = line[2].split(",")[2]
                vars()[cause] += int(number)

deathCount = []

for i in range(len(causes)):
    deathCount.append(vars()[causes[i]])

deathCount.sort()
causesSorted = causes[:]

for i in range(len(deathCount)):
    for j in range(len(deathCount)):
        if vars()[causes[j]] == deathCount[i]:
            causesSorted[i] = causes[j]
            break


plt.rcdefaults()
fig, ax = plt.subplots()

y_pos = np.arange(len(causesSorted))
ax.barh(y_pos, deathCount, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(causesSorted)

plt.show()