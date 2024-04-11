# Name: Eric Farrar
# Prog Purpose: This program fi
#   PPT: 4.2%
#   Relief rate: 33% (for personal vehichles only)

import datetime
##############  define global variables #########
# define tax rate and prices
PPT_RATE = .042
RELIEF_RATE = .33

# define global variables
assessed_value = 0
relief_yn = "N"

############# define program functions ###############
def main():
    prompt_in = "\nIs there another PPT payer (Y or N)  "
    goodbye_msg = "Personal Property are due DEC 5, 2024"
    more_data = True

    while more_data:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("Are there any more vehicles? (Y/N) ")
        yesno = yesno.upper()
        if yesno == "N":
            more_data = False
            print ("Taxes due 12/05/2024")
         

def get_user_data():
    global assessed_value, relief_yn
    assessed_value = int(input("What is the assessed value of the vehicle? "))
    relief_yn = input("Is the vehicle eligible for relief? (Y/N) ")
    relief_yn = relief_yn.upper()

def perform_calculations():
    global ppt_amount_anual, ppt_amount_6months, relief_amount, biannual_amount_owed
    ppt_amount_anual = assessed_value * PPT_RATE

    if relief_yn == "Y":
        relief_amount = ppt_amount_anual * RELIEF_RATE
    else:
        relief_amount = 0  #fix this with an IF/ELSE
        
    amount_owed = ppt_amount_anual - relief_amount
    biannual_amount_owed = amount_owed / 2
    


def display_results():
    print('------------------------------')
    print('**** CITY OF CHARLOTTESVILLE ****')
    print('PERSONAL PROPERTY TAX')
    print('------------------------------')
    print('PPT ANNUAL       $ ' + format(ppt_amount_anual,'8,.2f'))
    print('RELIEF           $ ' + format(relief_amount,'8,.2f'))
    print('AMOUNT DUE (6 Mo)$ ' + format(biannual_amount_owed,'8,.2f'))
    print('------------------------------')
    print(str(datetime.datetime.now()))

    

main()
