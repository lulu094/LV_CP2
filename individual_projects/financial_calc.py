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


def mainmenu():
    print("Financial Calculator Menu")
    print("1. Savings Time Calculator")
    print("2. Compound Interest Calculator")
    print("3. Budget Allocator")
    print("4. Sale Price Calculator")
    print("5. Tip Calculator")
    print("6. Exit")

    choice = input("Choose and option:")
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
    else:
        print("Invalid choice")

def savings_time_calc():
    print("Savings Time Calculator")

def compound_interest_calc():
        print("Compound Interest Calculator")

def budget_allocator():
        print("Budget Allocator")

def sale_price_calc():
        print("Sale Price Calculator")

def tip_calc():
        print("Tip Calculator")

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

    deposit = float(input("Enter the amount you will deposit each time: "))

    frequency = input("Will you deposit weekly or monthly? ").lower()

    if frequency == "weekly":
        weeks_needed = goal / deposit
        months_needed = weeks_needed / 4  # approximate weeks to months
        print(f"It will take about {round(months_needed, 1)} months to reach your goal.")
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
     start = ("Enter Start Amount:")



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
    # Ask user for monthly income
    income = float(input("Enter your monthly income: "))

    # Ask how many budget categories
    num_categories = int(input("How many budget categories do you have? "))

    # Loop through each category
    for i in range(num_categories):
        name = input(f"Enter the name of category {i + 1}: ")
        percent = float(input(f"What percent of your income goes to {name}? "))
        amount = income * (percent / 100)
        print(f"{name}: ${round(amount, 2)}")

#Sale price calc
#FUNCTION sale_price_calculator
    #ASK user for original price
    #ASK user for discount percentage

    #CALCULATE discounted price
    #DISPLAY final sale price
#END FUNCTION

def sale_price_calc():
    # Ask user for original price
    original_price = float(input("Enter the original price: "))

    # Ask for discount percentage
    discount = float(input("Enter the discount percentage: "))

    # Calculate discounted price
    final_price = original_price * (1 - discount / 100)
    print(f"The discounted price is: ${round(final_price, 2)}")

#Tip calc
#FUNCTION tip_calculator
    #ASK user for bill amount
    #ASK user for tip percentage

    #CALCULATE tip amount
    #CALCULATE total bill
    #DISPLAY tip and total
#END FUNCTION

def tip_calc():
    # Ask user for bill amount
    bill = float(input("Enter the bill amount: "))

    # Ask for tip percentage
    tip_percent = float(input("Enter the tip percentage: "))

    # Calculate tip and total
    tip = bill * (tip_percent / 100)
    total = bill + tip
    print(f"Tip amount: ${round(tip, 2)}")
    print(f"Total bill: ${round(total, 2)}")