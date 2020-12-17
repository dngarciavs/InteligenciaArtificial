#importing libraries
import random
import csv
#declaring variables
input,bread,filling,butter,ants,breadWeight,fillingWeight,butterWeight,antsWeight,biasWeight = [],[],[],[],[],[],[],[],[],[]
output,dt,yt,error,overallError = [],[],[],[],[]
bias = 1
rowNumber=0 #Defining the column number (Number of trials+the header)
#reading inputs
print("Reading File...")
print("Randomizing weights...")
with open('SandwichAnts.csv',newline='\n') as csvfile:
    reader=csv.reader(csvfile)
    for column in reader:
        if (rowNumber==0): #Getting headers
            rowNumber+=1
            header=column[1:] #getting headers
            header.append("Bread Weight") #adding headers
            header.append("Filling Weight")
            header.append("Butter_Weight")
            header.append("Ants Weight")
            header.append("Bias Weight")
        else:
            if column[1]=='MultiGrain': #coding inputs
                bread.append(1)
            elif column[1]=='Rye':
                bread.append(2)
            elif column[1]=='White':
                bread.append(3)
            else:
                bread.append(4)
            if column[2]=='HamPickles':
                filling.append(1)
            elif column[2]=='PeanutButter':
                filling.append(1)
            else:
                filling.append(1)
            if column[3]=='yes':
                butter.append(1)
            else:
                butter.append(0)
            ants.append(column[4])
            breadWeight.append(random.random()) #randomizing weights
            fillingWeight.append(random.random())
            butterWeight.append(random.random())
            antsWeight.append(random.random())
            biasWeight.append(random.random())
            rowNumber+=1

print(header[:]) #printing inputs
for i in range (rowNumber-1): #adding sublists
    input.append([bread[i],filling[i],butter[i],ants[i],breadWeight[i],fillingWeight[i],breadWeight[i],antsWeight[i],biasWeight[i]])
print("Inputs...")
print (*input, sep="\n"*2)
#propagation function
def fxpro(input,yt,bias,rowNumber):
    for i in range(rowNumber-1):
        yt.append(bread[i]*breadWeight[i]+filling[i]*fillingWeight[i]+butter[i]*butterWeight[i]+ants[i]*antsWeight[i]-bias*biasWeight[i]) #operation
    return yt
#activation function
'''def fxact(yt,rowNumber):
    for i in range(rowNumber-1):
        if yt < 40:
            yt = -1
        elif y > 40:
            yt = 1
        else:
            res = 0
    return yt'''
#adaptación de pesos

#main
yt = fxpro(input,yt,bias,rowNumber)
print("Propagation function...")
print(yt)
'''#llamada a la función de activación
yt = fxact(yt)
print("Activation function...")
print(*yt, sep="\n"*2)'''