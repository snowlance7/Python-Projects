print('Travel Time Calculator\n')

miles = int(input('Enter miles: '))
mph = int(input('Enter miles per hour: '))

time = miles / mph
hrs = int(time)
min = (time * 60) % 60

print('\nEstimated travel time')
print('Hours: ' + str(hrs))
print('Minutes: ' + str(round(min)))