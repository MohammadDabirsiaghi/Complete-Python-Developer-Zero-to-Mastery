# https://replit.com/@aneagoie/string-formatting
# name='mohammad'

print('hi '+name)

age = 55

print('hi '+name + '.You are '+str(age)+' year old')

print(f'hi {name}.You are {age} year old')


print('hi {}.You are {} year old'.format('ali', 65))
print('hi {}.You are {} year old'.format(name, age))
print('hi {1}.You are {0} year old'.format(name, age))

print('hi {new_name}.You are {age} year old'.format(new_name=name, age=100))
