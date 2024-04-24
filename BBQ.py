# Name: Eric Farrar
# Prog Purpose: This program finds the cost of a meal at Branch Barbeque Buffet
#   Price for an adult meal: $19.95
#   Price for a child meal: $11.95
#   Service fee: 10%
#   Sales tax rate: 6.2%

import datetime

############## define global variables ##################
# define tax rate, service fee, and prices
ADULT_MEAL = 19.95
CHILD_MEAL = 11.95
SERVICE_FEE_RATE = .010
SALES_TAX_RATE = .062

# define global variables
num_adult_meals = 0
num_child_meals = 0

################### define program functions ##################
def main():

    more_meals = True

    while more_meals:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to order again (Y or N)? ")
        if yesno == "N" or yesno =="n":
            more_meals = False
            print("Thank you for your order. Enjoy your meal!")


def get_user_data():
    global num_adult_meals
    num_adult_meals = int(input("Number of Adult meals: "))
    global num_child_meals
    num_child_meals = int(input("Number of Child meals: "))
    


def perform_calculations():
    global subtotal, service_fee, sales_tax, total
    cost_adult = num_adult_meals * ADULT_MEAL
    cost_child = num_child_meals * CHILD_MEAL
    subtotal = cost_adult + cost_child
    service_fee = subtotal  * SERVICE_FEE_RATE
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + service_fee + sales_tax
    


def display_results():

    currency_formatter = "{:8,.2f}".format
    timestamp = datetime.datetime.now()
    
    print("\n\n----------------------------------------")
    print("          Branch Barbeque Buffet        ")
    print("----------------------------------------")
    print("Date & Time: ", timestamp)
    print("----------------------------------------")
    print("Number of Adult meals: ", num_adult_meals)
    print("Cost of Adult meals:   $", currency_formatter(num_adult_meals * ADULT_MEAL).rjust(10))
    print("----------------------------------------")
    print("Number of Child meals: ", num_child_meals)
    print("Cost of Child meals:   $", currency_formatter(num_child_meals * CHILD_MEAL).rjust(10))
    print("----------------------------------------")
    print("Subtotal:               $", currency_formatter(subtotal).rjust(10))
    print("Service Fee (10%):      $", currency_formatter(service_fee).rjust(10))
    print("Sales Tax (6.2%):       $", currency_formatter(sales_tax).rjust(10))
    print("----------------------------------------")
    print("Total:                  $", currency_formatter(total).rjust(10))
    print("----------------------------------------")



######### call on main program to execute ###########
main()
