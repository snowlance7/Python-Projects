print('Tip Calculator\n')

meal_cost = float(input('Cost of meal: '))
tip_percent = float(input('Tip percent: '))

tip_amount = round(meal_cost * (tip_percent / 100),2)
total_amount = round(tip_amount + meal_cost,2)

print('Tip amount: ' + str(tip_amount))
print('Total amount: ' + str(total_amount))