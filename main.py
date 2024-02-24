print("Welcome to the Tip Calculator")
Total_bill = float(input("What was the total Bill? $"))
Percentage_on_tip = int(input("What percentage tip would you like to give? 10,12 or 15 "))
if Percentage_on_tip == 10:
    Total_bill += (Total_bill*0.1)
elif Percentage_on_tip == 12:
    Total_bill += (Total_bill*0.12)
elif Percentage_on_tip == 15:
    Total_bill += (Total_bill*0.15)
Bill_splitting = int(input("How many people to split the bill?"))
Total_Bill_splitting = (Total_bill/Bill_splitting)
#print(f'Each person should pay:${Total_Bill_splitting}')
print("Each person should pay:$ {:.2f} " .format(Total_Bill_splitting, 2)) # .format is used to print 2 decimal digits even after it's 0.
