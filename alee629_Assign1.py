#Assignment 1: Coffee or Tea, I See
#Andrea Lee 250836721

#dictionary of product offerings and prices
beverageCoffee = {
    'coffee',
    'c'
}

beverageTea = {
    'tea',
    't'
}

beverageSize = {
    'small': 1.50,
    's': 1.50,
    'medium': 2.50,
    'm': 2.50,
    'large': 3.25,
    'l': 3.25
}

flavouringCoffee = {
    'vanilla': 0.25,
    'v': 0.25,
    'chocolate': 0.75,
    'c': 0.75,
    'none': 0.00,
    '': 0.00
}

flavouringTea = {
    'lemon': 0.25,
    'l': 0.25,
    'mint': 0.50,
    'm': 0.50,
    'none': 0.00,
    '': 0.00
}

#prompt user for input and return error message if input is invalid
name = input('Enter name:\n')

beverage = input('Enter beverage:\n')
if beverage.lower() not in beverageCoffee:
    if beverage.lower() not in beverageTea:
        print('Invalid beverage specified.')
        exit()

size = input('Enter size:\n')
if size.lower() not in beverageSize:
    print('Invalid size specified.')
    exit()

flavouring = input('Enter flavouring:\n')
if beverage.lower() in beverageCoffee:
    if flavouring.lower() not in flavouringCoffee:
        print('Invalid flavour specified.')
        exit()
elif beverage.lower() in beverageTea:
    if flavouring.lower() not in flavouringTea:
        print('Invalid flavour specified.')
        exit()
else:
    print('Invalid flavour specified.')
    exit()

#calculate cost of user input
sizeCost = beverageSize.get(size.lower())

flavouringCost = ()
if beverage.lower() in beverageCoffee:
    flavouringCost = flavouringCoffee.get(flavouring.lower())
elif beverage.lower() in beverageTea:
    flavouringCost = flavouringTea.get(flavouring.lower())

totalCost = (sizeCost + flavouringCost) * 1.13

#format variables appropriately for output as a string (i.e. proper letter case and no abbreviations)
name = name.title()

size = size.lower()
if size == 's':
    size = 'small'
elif size == 'm':
    size = 'medium'
elif size == 'l':
    size = 'large'

beverage = beverage.lower()
if beverage == 'c':
    beverage = 'coffee'
elif beverage == 't':
    beverage = 'tea'

flavouring = flavouring.lower()
if flavouring == 'v':
    flavouring = 'vanilla'
elif flavouring == 'c':
    flavouring = 'chocolate'
elif flavouring == 'l':
    flavouring = 'lemon'
elif flavouring == 'm':
    flavouring = 'mint'
elif flavouring == 'none':
    flavouring = 'no'
elif flavouring == '':
    flavouring = 'no'

#print output
print('\nFor %s, a %s %s, %s flavouring, cost: $%.2f.' % (name, size, beverage, flavouring, totalCost))
