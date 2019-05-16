inventory = {
    'gold' : [500],
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']}
# insert key pocket
inventory['pocket'] = ['seashell', 'strange berry', 'lint'] 

# delete value "dagger" in key "backpack"
remove = inventory['backpack']
remove.remove('dagger')

# add value "50" to key "gold"
add = inventory['gold']
add.append(50)

print(inventory)
