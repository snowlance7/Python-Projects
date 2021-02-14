print ('Registration Form')

first_name = input("First name: ")
last_name = input("Last name: ")
birth_year = input("Birth year: ")

print('Welcome ' + first_name + ' ' + last_name + '!')
print('Your registration is complete.')
print('Your temporary password is: ' + first_name + '*' + birth_year)