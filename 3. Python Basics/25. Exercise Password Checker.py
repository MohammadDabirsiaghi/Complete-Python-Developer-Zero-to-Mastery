# input('jayjay')
# input('secret')

# print('{username}, your password {*****} is {6} letters long')

#print('*' * 10)

username=input('what is your username?')
password=input('what is your password?')

print(f'{username},your password, {password}, is {len(password)} letters long')

password_length=len(password)

hidden_password='*' * password_length

print(f'{username},your password, {hidden_password}, is {password_lengthdabir} letters long')