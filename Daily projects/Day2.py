print("Welcome to the tip calculator!")
bill = float(input("Wha was the total bill? $"))
tip=int(input("How much tip would you like to give? 10%, 12%, or 15%? "))
ppl = int(input("How many people to split the bill? "))
amount= (bill + bill*tip/100)/ppl
payable= round(amount,2)
print(f"Each person should pay: ${payable}")