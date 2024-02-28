
#• Define the problem by constructing an algorithm using pseudocode, and use that to write the application that calculates the total cost of a fence.
#How much should a fence cost?

#You've just been hired by Alton's Hardware Store.Your job is to develop a tool which will allow his customers to calculate the cost for installing a fence.Start by determining the algorithm to calculate the cost of installing the fence.
#Create a program that will calculate the cost with tax of fencing a rectangular yard.The cost of the fencing will depend on the amount of fencing required(the perimeter of the yard), and the type of fencing used.Gates can are available for an additional cost.At least one gate is required.
#Prices(including installation)

#• Wooden fencing costs $25 per foot
#• Chain - link fencing costs $15 per foot
#• Gates cost $150 each.You must install at least one gate and can install up to 3
#• A building permit is required.It costs $50.00.
#• The tax rate is 6.0 % but it doesn't apply to the building permit

#Your algorithm should allow any other person to achieve the same result by following your steps.They should not have to think about what they are doing.*/
print ("--------------------- Welcome to Alton's Hardware Store ---------------------\n")
print ('Please answer the following questions to get an estimate for you fence.\n')

woden = 25
chainLink = 15
fGate = 150 # First gate
additionalGates = 150
buildingPermit = 50 # tax not applicable
taxRate = 0.06

def fenceCalculator():
    while True:
        try:
            userInput = float(input('Please enter a \'1\' for Wooden Fencing, \'2\' for Chain link Fencing: , or \'0\' to Stop: \n'))
            while True:   
                    if userInput == 1:
                            print('\nYou picked Wooden Fencing\n')
                            customerName = input('Please enter your name: ')
                            wf = float(input('How many foot of Wooden Fencing do you need? '))
                            ag = float(input('how many additional Gates do you need? please enter a number from 1 to 3. '))
                            wfTotal = woden * wf
                            agTotal = (additionalGates * ag)+fGate
                            subTotal = wfTotal+agTotal #amount without taxes
                            ordertotal = wfTotal+agTotal*taxRate #tax amount
                            total = buildingPermit+subTotal+ordertotal
                            print('\n---------------Here is your bill summary---------------')
                            print(f'Customer Name: {customerName}')
                            print(f'\nFoot amount ordered: {wf}')
                            print(f'First gate for the fence = {fGate}')
                            print(f'Total of additional gates = {ag}')
                            print(f'Building permit = {buildingPermit} ** Not Taxable **')
                            print(f'Subtotal = {subTotal}')
                            print(f'Taxes = {ordertotal}')
                            print(f'Total = {total}') 
                            break
                    elif userInput == 2:
                            print('\nYou picked Chain Link Fencing\n')
                            customerName = input('Please enter your name: ')
                            cl = float(input('How many foot of Chain Link Fencing do you need? '))
                            ag = float(input('Do you need any additional Gates? '))
                            clTotal = chainLink * cl
                            agTotal = (additionalGates * ag)+fGate
                            subTotal = clTotal+agTotal #amount without taxes
                            ordertotal = clTotal+agTotal*taxRate #tax amount
                            total = buildingPermit+subTotal+ordertotal
                            print('\n---------------Here is your bill summary---------------')
                            print(f'Customer Name : {customerName}')
                            print(f'\nFoot amount ordered: {cl}')
                            print(f'First gate for the fence = {fGate}')
                            print(f'Total of additional gates = {ag}')
                            print(f'Building permit = {buildingPermit }** Not Taxable **')
                            print(f'Subtotal = {subTotal}')
                            print(f'Taxes = {ordertotal}')
                            print(f'Total = {total}')
                            break
                    elif userInput == 0:
                            print('Thank you for spending time with us today!!!')
                            return
        except:
            print('---ERROR---Oh Oh Please enter a \'1\' or a \'2\' to continue.')
               
                
                           
fenceCalculator()
   







