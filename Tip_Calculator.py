#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percent = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = float(input("How many people are to split the bill? "))
bill_split = total_bill/people
percent_split= round(bill_split*(tip_percent/100),3)
each_to_pay = "{:.2f}".format(bill_split + percent_split)
price_per_person = each_to_pay
print(f"Each person should pay: ${price_per_person}") 