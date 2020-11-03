"""
Shane Bacchus
Class: CS 521 - Fall 1
Date:10/10
Homework Problem # 5
Description of Problem (just a 1-2 line summary!):
Compound interest recursive and nonrecursive implementation
"""

def calc_compound_interest(principal_float,interest_float,years):
    """Future Value Calculated Non-Recursively"""
    
    
    final_calculation = principal_float*(interest_float)**years
    return final_calculation

def calc_compound_interest_recursive(principal_float, interest_float, years):
    """Future Value Calculated Recursively"""
    
    if years == 0:
        return principal_float
    else:
        return calc_compound_interest_recursive(principal_float * interest_float, interest_float, years-1)

if __name__ == "__main__":
    while True:
        try:
            principle = input("Please enter your principle (no commas): ")
            interest = input("Please enter your interest rate per year: ")
            years = input("Please enter the number of years to calculated the compound interest: ")

            #  Check if conversions work, else go to except 
            principle_float = float(principle)
            interest_float = float(interest) 
            final_interest_float = 1+(interest_float/100.0)
            years = int(years)

            non_recursive_return = calc_compound_interest(principle_float,final_interest_float,years)
            print("Non-Recusrive Ending Value is {:,.2f}".format(non_recursive_return))

        
            recursive_return = calc_compound_interest_recursive(principle_float, final_interest_float, years)
            print("Recusrive Ending Value is {:,.2f}".format(recursive_return))
                        
            #  Check if both returns rounded to 4 are equal
            non_recursive_return_rounded = round(non_recursive_return,4)
            recursive_return_rounded = round(recursive_return,4)
            
            if non_recursive_return_rounded == recursive_return_rounded:
                print("Both function outputs are equal when rounded to 4 decimal points")
            else:
                print("Both function outputs are not equal when rounded to 4 decimal points")

            break
            
              
        except  ValueError: print("You did enter the expected values. Please enter again")