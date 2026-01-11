# LV 1st Financial Calculator

# Main Program
# Start program
# Call main_menu()
# End program

# Main menu Function
# Function main_menu
#   Display menu options:
    #  1 Savings Time Calculator
    #  2 Compound Interest Calculator
    #  3 Budget Allocator
    #  5 Sale Price Calculator
    #  6 Tip Calculator
    #  Exit

#   Ask user to choose an option
#   if choice == 1
        # call savings_time_calc
#   elif choice == 2
        # call compound_interest_calc
#   elif choice == 3
        # call budget_allocator
#   elif choice == 4
        # call sale_price_calc
#   elif choice == 5
        # call tip_calc
#   elif choice == 6
        # end program
    # else 
        # print  Invalid choice
    #return to main menu
#End function


def main():
    while True:
        print("\nFinancial Calculator Menu")
        print("1. Savings Time Calculator")
        print("2. Compound Interest Calculator")
        print("3. Budget Allocator")
        print("4. Sale Price Calculator")
        print("5. Tip Calculator")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            savings_time_calc()
        elif choice == "2":
            compound_interest_calc()
        elif choice == "3":
            budget_allocator()
        elif choice == "4":
            sale_price_calc()
        elif choice == "5":
            tip_calc()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


# Savings time calc
# function savings_time_calc
    #ask user for savings goal
    #ask user for deposit amount
    #ask user if deposit is weekly or monthly

    # if weekly
        # calculate months needed using weekly formula
    #else
        # calculate months needed using monthly formula
    #display how long it will take to reach the goal
#end function

def savings_time_calc():
    goal = float(input("Enter your savings goal: "))
    deposit = float(input("Enter how much you deposit each time: "))

    print("How often do you deposit?")
    print("1. Weekly")
    print("2. Monthly")
    frequency = input("Choose 1 or 2: ")

    if frequency == "1":
        weeks_needed = goal / deposit
        months_needed = weeks_needed / 4
    else:
        months_needed = goal / deposit

    print(f"It will take about {round(months_needed, 1)} months to reach your goal.")

#Compound interest calculator with inner function
#function compound_interest_calculator
    #ask user for starting amount
    #ask user for interest rate
    #ask user for number of years

    #define inner function calculate_compound_interest
       # use formula: amount * (1 + rate) ^ years
        #return final amount
    #end inner function

    #call calculate_compound_interest
    #displa final amount
#end function

def compound_interest_calc():
    start = float(input("Starting Amount: "))
    rate = float(input("Interest Rate Percent: ")) / 100
    years = int(input("Years Spent Compounding: "))
    def calculate_compound():
        return start * (1 + rate) ** years

    final_amount = calculate_compound()
    print(f"At the end of {years} years you will have ${round(final_amount, 2)}")

#Budget allocator
#FUNCTION budget_allocator
    #ASK user for monthly income
    #ASK how many budget categories

    #FOR each category
        #ASK for category name
        #ASK for percentage
        #CALCULATE amount based on income and percentage
        #DISPLAY result
#END FUNCTION
def budget_allocator():
    income = float(input("What is your monthly income: "))
    categories = int(input("How many budget categories do you have: "))

    for i in range(categories):
        name = input(f"Category {i + 1} name: ")
        percent = float(input(f"What percent is your {name}: "))
        amount = income * (percent / 100)
        print(f"{name} is ${round(amount, 2)}")

#Sale price calc
#FUNCTION sale_price_calculator
    #ASK user for original price
    #ASK user for discount percentage

    #CALCULATE discounted price
    #DISPLAY final sale price
#END FUNCTION

def sale_price_calc():
    original_price = float(input("How much does the item originally cost: "))
    discount = float(input("What percent is the discount: "))

    final_price = original_price * (1 - discount / 100)
    print(f"The item now costs ${round(final_price, 2)}")
#Tip calc
#FUNCTION tip_calculator
    #ASK user for bill amount
    #ASK user for tip percentage

    #CALCULATE tip amount
    #CALCULATE total bill
    #DISPLAY tip and total
#END FUNCTION

def tip_calc():
    bill = float(input("How much is the bill: "))
    tip_percent = float(input("What percent of a tip are you giving: "))

    tip = bill * (tip_percent / 100)
    total = bill + tip

    print(f"The tip amount is ${round(tip, 2)} and your total is ${round(total, 2)}")

# Start the program 
main()