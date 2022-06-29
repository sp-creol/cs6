semi_annual_raise = .07
r = 0.04
portion_down_payment = 0.25
total_cost = 1000000
original_salary = float(input("What is your starting annual salary? "))

low = 0
high = 10000
steps = 0
while True:
    steps += 1
    guess = int((low + high) / 2.0)
    portion_saved = guess / 10000
    months = 0
    current_savings = 0.0
    annual_salary = original_salary
    while months < 36:
        months += 1
        current_savings *= 1 + (r/12)
        current_savings += portion_saved * (annual_salary/12)
        if months % 6 == 0:
            annual_salary *= 1 + semi_annual_raise
    difference = current_savings - (portion_down_payment * total_cost)
    if abs(difference) < 100:
        print("Best savings rate:",portion_saved)
        print("Steps in bisection search:",steps)
        break
    elif guess >= 9999:
        print("It is not possible to pay the down payment in three years.")
        break
    elif difference < 0:
        low = guess
    elif difference > 0:
        high = guess