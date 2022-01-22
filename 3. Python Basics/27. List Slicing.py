# List slicing

# string='hello'
# string[0:2:1]
# print(string[0:2:1])

amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

#print(amazon_cart)

#print(amazon_cart[0:2])

#print(amazon_cart[0::2])

# immutable string
# greet='hello'
# greet[0]='Z'

# List Mutable
# amazon_cart[0] = 'laptop'

# #print(amazon_cart)


# #print(amazon_cart[1:3])

# new_cart = amazon_cart[0:3]
# print(new_cart)

# new_cart[0]='gum'
# print(new_cart)



# new_cart2=amazon_cart;
# new_cart2[0]='New'
# print(new_cart2)
# print(amazon_cart)

new_cart2=amazon_cart[:];
new_cart2[0]='New'
print(new_cart2)
print(amazon_cart)
