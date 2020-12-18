#importing libraries
import random
import csv
#declaring variables
inputs,bread,filling,butter,ants,breadWeight,fillingWeight,butterWeight,antsWeight,biasWeight = [],[],[],[],[],[],[],[],[],[]
outputs,dt,yt,error = [],[],[],[]
overallError = 0
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
#adding into list
for i in range (rowNumber-1):
    inputs.append([bread[i],filling[i],butter[i],ants[i],breadWeight[i],fillingWeight[i],breadWeight[i],antsWeight[i],biasWeight[i]])
#defining expected outputs
for i in range(rowNumber-1):
    if inputs[i][3] > 40:
        dt.append(1)
    else:
        dt.append(0)
#propagation function
def fxpro(inputs,bias,rowNumber):
    yt = []
    for i in range(rowNumber-1):
        yt.append(inputs[i][0]*inputs[i][4]+inputs[i][1]*inputs[i][5]+inputs[i][2]*inputs[i][6]+inputs[i][3]*inputs[i][7]-bias*inputs[i][8])
    return yt
#activation function
def fxact(yt,rowNumber):
    for i in range(rowNumber-1):
        if yt[i] < 20:
            yt[i] = -1
        else:
            yt[i] = 1
    return yt
#error calculator
def fxerror(dt,yt,rowNumber):
    error = []
    for i in range(rowNumber-1):
        error.append(dt[i]-yt[i])
    return error
#adaptación de pesos

#main
print("\n Reading File...\n")
#printing inputs
print(header[:])
print("\n")
print (*inputs, sep="\n"*2)
#printing expected outputs
print("\n Expected outputs \n")
print(*dt, sep="\n"*2)
#using propagation function
yt = fxpro(inputs,bias,rowNumber)
#printing propagation function outputs
print("\n Propagation function \n")
print(*yt,sep="\n"*2)
#using activation function
yt = fxact(yt,rowNumber)
#printing activation function outputs
print("\n Activation function \n")
print(*yt,sep="\n"*2)
#using error function
error = fxerror(dt,yt,rowNumber)
#printing error function outputs
print("\n Error function \n")
print(*error,sep="\n"*2)