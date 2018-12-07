inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory["pocket"] = []

inventory["pocket"] = ['seashell', 'strange berry', 'lint']

print(inventory['pocket'])

backpack = inventory["backpack"]
backpack.remove('dagger')
print(backpack)

gold = inventory['gold']
gold += 50
print(gold)
