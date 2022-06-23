portion_down_payment = 0.25
current_savings = 0.0
r = 0.04
annual_salary = float(input("What is your starting annual salary? "))
portion_saved = float(input("What portion of your salary will be saved each month (decimal)? "))
total_cost = float(input("How much does your dream home cost? "))

months = 0
while current_savings < (portion_down_payment * total_cost):
    months += 1
    current_savings *= 1 + (r/12)
    current_savings += portion_saved * (annual_salary/12)
print("Number of months:",months)