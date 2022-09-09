# collect the necessary inputs: p, n, r
# calculate the monthly payment
# show to the user

def monthlyInterestCalculator():
    p = int(input("Enter the principle amount : "))
    n = int(input("Enter the no of years      : "))
    r = int(input("Enter the rate of interest : "))
    
    monthlyInterestRate = r/1200
    noOfMonths = n * 12
    monthlyPayment = p * monthlyInterestRate / (1 - (1 + monthlyInterestRate) ** (-noOfMonths))
    
    print("Monthly Payment : %.2f" %monthlyPayment)

monthlyInterestCalculator()