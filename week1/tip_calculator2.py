print('Tip Calculator\n')

meal_cost = float(input('Cost of meal: '))
tip15 = round(meal_cost * 0.15,2)
tip20 = round(meal_cost * 0.20,2)
tip25 = round(meal_cost * 0.25,2)

print('\n15%')
print('Tip amount: ' + str(tip15))
print('Total amount: ' + str(round(tip15 + meal_cost,2)))

print('\n20%')
print('Tip amount: ' + str(tip20))
print('Total amount: ' + str(round(tip20 + meal_cost,2)))

print('\n25%')
print('Tip amount: ' + str(tip25))
print('Total amount: ' + str(round(tip25 + meal_cost,2)))