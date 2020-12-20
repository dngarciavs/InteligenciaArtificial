#importing libraries
import random #required for weights assignment
import csv #required for file reading
#declaring variables
inputs,bread,filling,butter,ants,breadWeight,fillingWeight,butterWeight,biasWeight = [],[],[],[],[],[],[],[],[]
alpha,bias,overallError,epoch,rowNumber = 1,1,1,0,0
#reading inputs
with open('SandwichAnts.csv',newline='\n') as csvfile:
    reader=csv.reader(csvfile)
    for column in reader:
        if (rowNumber==0): #Getting headers
            rowNumber+=1 #counting records
            header=column[1:] #getting headers
            header.append("Bread Weight") #adding weights into header
            header.append("Filling Weight")
            header.append("Butter Weight")
            header.append("Bias Weight")
        else:
            if column[1]=='MultiGrain': #coding types of bread
                bread.append(1)
            elif column[1]=='Rye':
                bread.append(2)
            elif column[1]=='White':
                bread.append(3)
            else:
                bread.append(4)
            if column[2]=='HamPickles': #coding types of filling
                filling.append(1)
            elif column[2]=='PeanutButter':
                filling.append(1)
            else:
                filling.append(1)
            if column[3]=='yes': #coding types of butter
                butter.append(1)
            else:
                butter.append(0)
            ants.append(int(column[4])) #adding number of ants we expect to have
            breadWeight.append(random.random()) #randomizing weights
            fillingWeight.append(random.random())
            butterWeight.append(random.random())
            biasWeight.append(random.random())
            rowNumber+=1 #counting records
#adding inputs into list
for i in range (rowNumber-1):
    inputs.append([bread[i],filling[i],butter[i],ants[i],breadWeight[i],fillingWeight[i],butterWeight[i],biasWeight[i]])
#propagation function
def fxpro(inputs,bias,i):
    sum = inputs[i][0]*inputs[i][4]+inputs[i][1]*inputs[i][5]+inputs[i][2]*inputs[i][6]-bias*inputs[i][7]
    return sum
#activation function
def fxact(sum):
    if sum > 20: #proposed condition
        yt = 1
    else:
        yt = -1
    return yt
#expected output function
def fxexp(inputs,i):
    if inputs[i][3] > 40: #initial condition
        dt = 1
    else:
        dt = -1
    return dt
#error calculator
def fxerror(dt,yt):
    error = dt-yt
    return error
#new weights function
def fxweight(inputs,bias,error,alpha,i):
    inputs[i][4] += alpha*error*inputs[i][0]
    inputs[i][5] += alpha*error*inputs[i][1]
    inputs[i][6] += alpha*error*inputs[i][2]
    inputs[i][7] += alpha*error*bias
    return inputs
#main
print("\nReading File...\n")
print(header[:]) #printing header
print (*inputs,sep="\n"*2) #printing records
#learning phase
while overallError != 0: #adquiring knowledge
    epoch += 1
    print(f"\nStarts {epoch} # epoch")
    overallError = 0
    for i in range(rowNumber-1):
        dt = fxexp(inputs,i) #applying expected output function
        print(f"\nExpected output = {dt}")
        sum = fxpro(inputs,bias,i) #applying propagation function
        print(f"Propagation fuction output = {sum}")
        yt = fxact(sum) #applying activation function
        print(f"Output = {yt}")
        error = fxerror(dt,yt) #getting error
        print(f"Error = {error}")
        if error == 0:
            print("The activation function output was the expected")
            print("There will be no changes")
        else:
            print("Recalculating weights...")
            inputs = fxweight(inputs,bias,error,alpha,i) #getting new weights
            print("The new weights are:")
            print(inputs[i][4:],sep = "\n"*2)
        overallError += error
    overallError = abs(overallError/rowNumber) #getting overall Error
    print(f"Overall error = {overallError}")
    print(f"\nEnds {epoch} # epoch")
    print("\n*************************************************************************************************************************************")
#testing phase
print("\nTesting phase:")
for i in range(rowNumber-6,rowNumber-1): #testing the adquired knowledge with te last 5 records
    dt = fxexp(inputs,i) #applying expected output function
    print(f"\nExpected output = {dt}")
    sum = fxpro(inputs,bias,i) #applying propagation function
    print(f"Propagation fuction output = {sum}")
    yt = fxact(sum) #applying activation function
    print(f"Output = {yt}")
    error = fxerror(dt,yt) #getting error
    print(f"Error = {error}")
print("\nThe program has ended")