import pandas as pd
import numpy as np

### string variable ###

ing_Dairy = 'milk'
ing_Meat = 'chicken'
ing_Snacks = 'chips'

print(ing_Dairy)
print(ing_Meat)
print(ing_Snacks)

### f string ###

grocery_listFstring = f'{ing_Dairy}, {ing_Meat}, {ing_Snacks}'

print(grocery_listFstring)

### number variable ###

age = 10
print(age)

### List ###

bp_systolic = [100,140,120,160,200]


### Dictionaries ###

food1 = { 
    'ingredientFish': 'salmon',
    'ingredientFruit': 'apple',
    'ingredientVeg': "pepper",
    'ingredientSpices': ['salt', 'paprika', 'seasoning',],
    'costSalmon': 10,
    'costApple' : 2,
    'costPepper': 2.5,
    'recipe': {
        'heat': '450',
        'chop' : 'finely',
        'bake' : 'minutes20',
    }
}

food1['ingredientFish']

food1['ingredientFish'] + ' ' + food1['ingredientFruit'] + ' ' +  food1['ingredientVeg']


######

years = [1995, 2000, 2005, 2010, 2015, 2020]

print('Year 1: ', years[0])
print('Year 2: ', years[1])
print('Year 3: ', years[2])
print('Year 4: ', years[3])

for y in years: 
        print('Year is: ',y)

years = [1995, 2000, 2005, 2010, 2015, 2020]

for y in years:
    if y >= 2030:
        year_plus20 = y +20
        print('Original age:', y)
        print('The year in 20 years is: ', year_plus20)
    else:
        print:('Year is no good')
          ### for some reason it wont run, it will do the math without the "if/eles" but when I add it, it stops and only says "year is no good" multiple times  ###



### Funtions ###

def PApressure (PAS, PAD):
    print(f'Your PApressure is {PAS}/{PAD}')
    if PAS >= 30:
        print('Your PA systolic pressure is too high')
    else:
        print('Your PA systolic pressure is within normal limits')

    if PAS <= 15:
        print('Your PA systolic pressure is too low')
    else:
        print('Your PA systolic pressure is within normal limits')

    if PAD >= 12:
        print('Your PA diastolic pressure is too high')
    else:
        print('Your PA diastolic pressure is within normal limits')

    if PAD <= 4:
        print('Your PA diastolic pressure is too low')
    else:
        print('Your PA diastolic pressure is within normal limits')


PApressure(25,10)
PApressure(35,15)
PApressure(10,3)

### I am not sure why it prints "within normal limits" for every item when you hit run###
