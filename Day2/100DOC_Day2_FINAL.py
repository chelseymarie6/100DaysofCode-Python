#100 Days of Code_Day2.py

#If the bill was $150.00, split evenly between 5 people, with 12% tip,
#each person should pay (150/5)*1.12
#Round the result to two decimal places

#header
print("Welcome to the Tip Calculator")

#variables
bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

people = int(input("How many people are splitting the bill? 1"))

#math operations

#calculated_bill = (tip / 100) * bill + bill
total_bill = bill * (1 + tip / 100)

bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)

#formatting issue to get 2 decimal places
final_amount = "{:.2f}".format(bill_per_person)

#print output of math
print(f"Each person should pay ${final_amount}")
