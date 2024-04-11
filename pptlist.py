# Name: your name here
# Program Purpose: This program uses lists to find the personal property tax for vehicles 
#    in Charlottesville and produces a report which displays all data and the total tax due
#    for six months
#
# Personal property tax in Charlottesville:
#       -- 4.20% per year
#       -- Paid every six months
# Personal Property Tax Relief (PPTR):
#       -- Eligibility: vehicles used for personal use only          
#       -- Tax relief rate is 33%

import datetime

################# define tax rates  ################
PPT_RATE = .042
RELIEF_RATE = .33

################# create list data  ################
vehicle = ["2019 Volvo ",
           "2018 Toyota",
           "2022 Kia   ",
           "2020 Ford  ",
           "2023 Honda ",
           "2019 Lexus " ,
           "2002 Suburban " ,
           "2010 Kia   " ,
           "2015 Tesla " ,
           "2018 Lamborghini",] 

vehicle_value = [13000, 10200, 17000, 21000, 28000, 16700, 34000, 25000, 30000, 2000000000 ,]

pptr_eligible = ["Y", "Y", "N", "Y", "N", "Y", "Y", "N", "Y", "Y" , ]

owner_name = ["Brand, Debra      ",
              "Smith, Carter     ",
              "Johnson, Bradley  ",
              "Garcia, Jennifer  ",
              "Henderson, Leticia",
              "White, Danielle" ,
              "White, Walter" ,
              "Pinkman, Jesse" ,
              "Skywalker, Luke" ,
              "Vader, Darth" ,]
ppt_owed = []

num_vehicles = len(vehicle)
tax_due = 0
total = 0


######## define program functions #######
def main():
    perform_calculations()
    display_results()

def perform_calculations():
    global total

    for i in range(num_vehicles):

        tax_due = (vehicle_value[i] * PPT_RATE / 2 )

        if pptr_eligible[i].upper() == "Y": 
         tax_due = tax_due * .67

        ppt_owed.append(tax_due)

        total = total + tax_due

def display_results():
    moneyf = '8,.2f'
    line =("---------------------------------------------------------------")
    tab = "\t"
    dt_full = str(datetime.datetime.now())
    dt_short = dt_full[0:16]

    print(line)
    print("***************** PEROSNAL PROPERTY TAX REPORT **************")
    print("                   Charlottesville, Virginia")

    print ("\n\t\tRUN DATE/TIME: " + dt_short )
    print ("\nNAME" + tab + tab + tab + "VEHICLE" + tab + tab + "VALUE" + tab + tab + "RELIEF" + tab + "   TAX DUE")

    for i in range(num_vehicles):
        dataline1 = owner_name[i]+ tab + vehicle[i] + tab + format(vehicle_value[i],moneyf) + tab
        dataline2 = pptr_eligible[i] + tab + format(ppt_owed[i],moneyf)
        print(dataline1 + dataline2)

    print(line)
    print("*********************************************** TOTAL TAX DUE: " + tab + format(total,moneyf))
main()        

