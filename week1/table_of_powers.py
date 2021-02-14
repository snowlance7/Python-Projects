print('Table of Powers\n')

cont = True

while cont == True:
    start = int(input('Start number: '))
    stop = int(input('Stop number: ')) + 1

    if start < stop:
        print('\nNumber       Squared        Cubed\n')

        for n in range(start, stop):
            square = n ** 2
            cube = n ** 3
            print(str(n) + '        ' + str(square) + '       ' + str(cube))

        cont = False

    else:
        print('Start number must be less than the stop number. Please try again.')
