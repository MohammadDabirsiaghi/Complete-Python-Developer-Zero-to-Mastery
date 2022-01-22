#iterable --> list-dictionary-tuple-set-string

for item in 50:
    print(item)

# #List
# for item in [1,2,3,4,5]:
#     print(item)

user={
    'name':'mohammad',
    'age':56,
    'can_swim':False
}
#dictionary
for item in user:
    print(item)

for item in user.items():
    print(item)
    key,value=item;
    print(key,value)


for key,value in user.items():
    print(key,value)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)