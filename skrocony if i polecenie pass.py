dayType = 1

weekend = 1
workday = 2
holiday = 3

if dayType == 1:
    pass
elif dayType == 2:
    pass
else:
    pass


dayDescribtion = 'weekend' if dayType == 1 else 'workday' if dayType == 2 else 'holiday'
print(dayDescribtion)

price = 123
bonus = 23
bonus_granted = 1
price_bonus = price - bonus

if bonus_granted:
    price_bonus
    print(price_bonus)
else:
    print(price)





new_price = price_bonus if bonus_granted else price
print('New price is', new_price)


rating = 4

if rating == 5:
    print('very good')
elif rating == 4:
    print('good')
else:
    print('weak')

new_rating = print('very good') if rating == 5 else  print('good') if rating == 4 else print('weak')

weekday = 'Czwartek'

if weekday == 'Poniedzialek':
    print('Nie moge bo pomagam mamie')
elif weekday == 'Wtorek' or weekday == 'Sroda':
    print('Ty masz w domu pranie')
elif weekday == 'Czwartek':
    print('Ja mam dyzur')
elif weekday == 'Piatek':
    print('Dwa zebrania')
elif weekday == 'Sobota':
    print('Ty na lekcje ganiasz')
else:
    print('Niedziela bedzie dla nas')

spotkanie = print('Nie moge bo pomagam mamie') if weekday == 'Poniedzialek' else print('Ty masz w domu pranie') if weekday == 'Wtorek' or weekday == 'Sroda' else print('Ja mam dyzur') if weekday == 'Czwartek' else print('Dwa zebrania') if weekday == 'Piatek' else print('Ty na lekcje ganiasz') if weekday == 'Sobota' else print('Niedziela bedzie dla nas')

