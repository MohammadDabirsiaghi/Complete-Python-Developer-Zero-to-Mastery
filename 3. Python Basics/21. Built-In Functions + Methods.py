#

# str()
# int()
# float()
# type()
# print()
# https://docs.python.org/3/library/functions.html

print(len('hello world'))

greet = 'helloooo'
print(greet[0:len(greet)])

# https://www.w3schools.com/python/python_ref_string.asp

quote = 'to be or not To be'
print(quote.upper())

print(quote.capitalize())
print(quote.lower())

print(quote.find('be'))

print(quote.replace('be', 'me'))


print(quote)

quote2 = quote.replace('be', 'me')
print(quote)
print(quote2)
