print('Shipping Calculator')

cont = 'y'

while cont.lower() == 'y':

    order_cost = float(input('\nCost of items ordered: '))

    if order_cost > 0.00:
        if order_cost >= 75.00:
            ship_cost = 0.00
        elif order_cost >= 50.00:
            ship_cost = 9.95
        elif order_cost >= 30.00:
            ship_cost = 7.95
        else:
            ship_cost = 5.95

        total = round(order_cost + ship_cost,2)

        print('Shipping cost:   ' + str(ship_cost))
        print('Total cost:  ' + str(total))

        cont = input('\nContinue? (y/n): ')

    else:
        print('You must enter a positive number. Please try again.')

print('\nBye!')

