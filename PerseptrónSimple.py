#importing libraries
import random
import csv
#declaring variables
input,bread,filling,butter,ants,breadWeight,fillingWeight,butterWeight,antsWeight,biasWeight = [],[],[],[],[],[],[],[],[],[]
output,dt,yt,error,overallError = [],[],[],[],[]
bias = 1
rowNumber=0
#reading inputs
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
            ants.append(int(column[4]))
            breadWeight.append(random.random()) #randomizing weights
            fillingWeight.append(random.random())
            butterWeight.append(random.random())
            antsWeight.append(random.random())
            biasWeight.append(random.random())
            rowNumber+=1
#adding sublists to input list
for i in range (rowNumber-1):
    input.append([bread[i],filling[i],butter[i],ants[i],breadWeight[i],fillingWeight[i],breadWeight[i],antsWeight[i],biasWeight[i]])
#propagation function
def fxpro(input,bias,rowNumber):
    list = []
    for i in range(rowNumber-1):
        list.append(input[i][0]*input[i][4]+input[i][1]*input[i][5]+input[i][2]*input[i][6]+input[i][3]*input[i][7]-bias*input[i][8])
    return list
#defining expected outputs
for i in range(rowNumber-1):
    if input[i][3] > 40:
        dt.append(1)
    else:
        dt.append(0)
#activation function
def fxact(yt,rowNumber):
    for i in range(rowNumber-1):
        if yt[i] < 20:
            yt[i] = -1
        else:
            yt[i] = 1
    return yt
#adaptación de pesos

#main
print("\n Reading File...\n")
#printing inputs
print(header[:])
print("\n")
print (*input, sep="\n"*2)
print("\n Expected outputs \n")
print(*dt, sep="\n"*2)
#using propagation function
yt = fxpro(input,bias,rowNumber)
print("\n Propagation function \n")
print(*yt,sep="\n"*2)
yt = fxact(yt,rowNumber)
print("\n Activation function \n")
print(*yt,sep="\n"*2)
#llamada a la función de activación
'''yt = fxact(yt)
print("Activation function...")
print(*yt, sep="\n"*2)'''