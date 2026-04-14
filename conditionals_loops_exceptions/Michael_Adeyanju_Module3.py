# assignment

# TASK 1 guessing game 
print('|||||GUESSING GAME')
guess_number = 20 # this is the number the computer guessed 

try :
    data = int(input('Enter a number : ')) # taking user input in int form
    if data > 20 :                          # higner value if the value entered is higer that the guessing number
        print('Higher value of number')               
    elif data < 20 :                        # lesse value if the value entered is lesser that the guessing number       
        print('lower level of number')                
    elif data == 20 :                        # exact guess number        
        print('Correct you won the game!!!')
except ValueError :                             # cant enter a string as an int it has to int
    print('Enter a valid number  (value inputed is not a number)')


# TASK 2 list of exams scores above 50 then calculate the average
print('|||||SCORE ANALYZER')
scores = [10,80,40,60,70,85,35,20,62,20]

scores_above_fifty = [x for x in scores if x > 50]  # get the values that are greater that 50 in the list (scores)
print(f'SCORES ABOVE 50 : {scores_above_fifty}')

average = sum(scores_above_fifty) / len(scores_above_fifty) # calculate average 
print(F'AVERAGE OF THE SCORES ABOVE 50 :  {average}')


# TASK 3 multiplication table to display a 1-12 time table for any number the user type in using while loop
print('|||||MULTIPLICATION TABLE')
number_input = int(input('Enter number : '))           # user input the number they want to multiply
start = 1                                               # multiplication starts from 1
while start <= 12 :                                     # as long as the start variable starts from 1 to 12 the block of code runs 
    multiply = number_input * start                     # multiply the loop number by the inputed number eg 2 x 1 = 2 , 2 x 2 = 4
    print(f'{number_input} x {start} = {multiply}')
    start += 1


# TASK 4 ATM FLOW 
print('|||||ATM FLOW MACHINE')
pin = '2468'                                            # pin to mock the flow of an atm machine(all atm machines requires pin)
balance = 1000                                          # customer balance

try :
    security = input('Enter pin to withdraw : ')
    if security == pin :                                # using pin to access the atm (withdraw)
        print(f'Current balance: {balance}')
        withdraw_amount = int(input('Enter amount to withdraw $: '))
        if withdraw_amount > balance :                                  # if the amount entered is greater than the balance print insufficient bal
            print('Insufficient balance')
        elif withdraw_amount <= 0 :                                     # cant enter 0 as a withdrawing amount
            print('Error: withdraw amount must be greater that 0 you cant withdraw 0 ')
        else :                                                          # this is if the amount is acurate or lesse that balance 
            print(f'withdraw for ${withdraw_amount} successful')
            print(f'New balance : ${balance - withdraw_amount}')
    else :
        print('wrong pin')                                              # if the pin is not correct the atm flow is canceled

except ValueError :                                                     # value is a int if strings it gives an error 
    print('Enter valid amount')


