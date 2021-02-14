print('Change Calculator')

cont = 'y'

while cont.lower() == 'y':
    cents = int(input('\nEnter number of cents (0-99): '))

    quarters = cents // 25
    cents = cents % 25
    dimes = cents // 10
    cents = cents % 10
    nickels = cents // 5
    cents = cents % 5
    pennies = cents

    print('\nQuarters: ' + str(quarters))
    print('Dimes: ' + str(dimes))
    print('Nickels: ' + str(nickels))
    print('Pennies: ' + str(pennies))

    cont = input('\nContinue? (y/n): ')

print('Bye!')

