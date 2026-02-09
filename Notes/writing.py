
"""with open("Notes\\proof.txt",'rt') as file:
    content = file
    content += "\nI wrote on my file"
    file.write(content)


with open("Notes\\writing.txt",'a') as file:
    file.write("\nThis is more on my file!")
print("code end")"""

import csv

with open("Notes\Class CSV sample - Sheet1.csv",'r+', newline ='') as csvfile:
    fieldnames = ['username', 'color']
    reader = csv.reader(csvfile)
    for line in reader:
        print(f"{fieldnames[0]}, {line[0]} favorite color {line [1]}")
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #writer.writeheader()
    writer.writerow({'username': 'aUser','color': 'pink'})
    writer.writerow({'username': 'basicPerson','color': 'red'})
    writer.writerow({'username': 'anotherUser','color': 'green'})
    writer.writerow({'username': 'thirdUser','color': 'blue'})
print("Code is done")