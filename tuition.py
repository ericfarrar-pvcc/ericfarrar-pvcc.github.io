# Name: Eric Farrar
# Prog Purpose: This program computes PVCC college tuition & fees based on number of credits
#   PVCC Fee Rates are from: https://www.pvcc.edu/tuition-and-fees


# define tuition & fee rates
RATE_TUITION_IN = 159.61
RATE_TUITION_OUT = 336.21
RATE_CAPITAL_FEE = 23.50
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90
import datetime
#define global variables
inout = 1 # 1 means in-state, 2 means out of state
numcredits = 0
scholarship_amt = 0

tuition_amt = 0
inst_fee = 0
cap_fee = 0
act_fee = 0
total = 0
balance = 0

############### define program functions ###############
def main():
    
        more = True
        while more:
            get_user_data()
            perform_calculations()
            display_results()

        yesno = input("\nWould you like to calculate tuition & fees for another student? (Y/N): ")
        if yesno == "n" or yesno == "N":
            more = False
            print("Thank you for enrolling at PVCC. Enjoy the semester!")

def get_user_data():
    global inout, numcredits, scholarship_amt
    print('**** PEDMONT VIRGINIA COMM COLLEGE Tuition & fees ****')
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarship_amt = int(input("Scholarship amount received: "))

def perform_calculations():
    global tuition_amt, inst_fee, cap_fee, act_fee, total, balance

    if inout == 1:
        tuition_amt = numcredits * RATE_TUITION_IN
        cap_fee = 0
    else:
        tuition_amt = numcredits * RATE_TUITION_OUT
        cap_fee = numcredits * RATE_CAPITAL_FEE

    inst_fee = numcredits * RATE_INSTITUTION_FEE
    act_fee = numcredits * RATE_ACTIVITY_FEE

    total = tuition_amt + inst_fee + act_fee + cap_fee

    balance = total 


def display_results():
    currency = '8,.2f'
    line = '-------------------------------------------'

    print(line)
    print('*** PIEDMONT VIRGINIA COMM COLLEGE ****')
    print('   Tuition and Fees Report')
    print(line)
    print('Tuition        $ ' + format(tuition_amt,currency))
    print('Capital Fee    $ ' + format(cap_fee,currency))
    print('Institution Fee $ ' + format(inst_fee, currency))
    print('Activity Fee   $ ' + format(act_fee, currency))
    print('Total Fees     $ ' + format(total, currency))
    print('Scholarship    $ ' + format(scholarship_amt, currency))
    print('Balance Due    $ ' + format(balance, currency))
    print(line)
    print(datetime.datetime.now())



main()
            
