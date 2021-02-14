print('Letter Grade Converter')

cont = 'y'

while cont == 'y':
    grade = int(input('\nEnter numerical grade: '))

    if grade >= 88:
        letter_grade = 'A'
    elif grade >= 80:
        letter_grade = 'B'
    elif grade >= 67:
        letter_grade = 'C'
    elif grade >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    print('Letter grade: ' + letter_grade)
    cont = input('\nContinue? (y/n): ').lower()
print('\nBye!')