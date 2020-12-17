#importing libraries
import csv
import random
#reading inputs
print("Reading File...")
print("Randomizing weights...")
#declaring variables
content,bread,filling,butter,ants,bias,bread_weight,filling_weight,butter_weight,ants_weight,bias_weight = [],[],[],[],[],[],[],[],[],[],[]
columnNumber=0 #Defining the column number (Number of trials+the header)
with open('SandwichAnts.csv',newline='\n') as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        if (columnNumber==0): #Getting headers
            columnNumber+=1
            header=row[1:]
            header.append("Bias") #Adding headers
            header.append("Bread Weight")
            header.append("Filling Weight")
            header.append("Butter_Weight")
            header.append("Ants Weight")
            header.append("Bias Weight")
        else:
            if row[1]=='MultiGrain': #Coding inputs
                bread.append(1)
            elif row[1]=='Rye':
                bread.append(2)
            elif row[1]=='White':
                bread.append(3)
            else:
                bread.append(4)
            if row[2]=='HamPickles':
                filling.append(1)
            elif row[2]=='PeanutButter':
                filling.append(1)
            else:
                filling.append(1)
            if row[3]=='yes':
                butter.append(1)
            else:
                butter.append(0)
            ants.append(row[4])
            bias.append(1)
            bread_weight.append(random.random()) #randomizing weights
            filling_weight.append(random.random())
            butter_weight.append(random.random())
            ants_weight.append(random.random())
            bias_weight.append(random.random())
            columnNumber+=1

print(header[:])
for i in range (columnNumber-1): #adding sublists
    content.append([bread[i],filling[i],butter[i],ants[i],bias[i],bread_weight[i],filling_weight[i],bread_weight[i],ants_weight[i],bias_weight[i]])
print("Content...")
print (*content, sep="\n"*2)