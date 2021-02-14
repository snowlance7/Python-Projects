print ('Price Comparison\n')

oz_price64 = float(input('Price of 64 oz size: '))
oz_price32 = float(input('Price of 32 oz size: '))

price_per_64oz = round(oz_price64 / 64,2)
price_per_32oz = round(oz_price32 / 32,2)

print('\nPrice per oz (64 oz): ' + str(price_per_64oz))
print('Price per oz (32 oz): ' + str(price_per_32oz))