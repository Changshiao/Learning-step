catalogue = {
    'apple' : '130',
    'avocadoyields' : '50',
    'banana' : '110',
    'cantaloupe' : '50',
    'grapefruit' : '60',
    'grapes' : '90',
    'honeydew' : '50',
    'kiwifruit' : '90',
    'lemon' : '15',
    'lime' : '20',
    'nectarine' : '60',
    'orange' : '80',
    'peach' : '60',
    'pear' : '100',
    'pineapple' : '50',
    'plums' : '70',
    'strawberries' : '50',
    'sweetcherries' : '100',
    'tangerine' : '50',
    'watermelon' : '80'
}

fruit_type=input("fruit type? ").replace(" ","").lower()
if fruit_type in catalogue:
    print(catalogue[fruit_type])
