for item in range (1,5) :
    for x in ['a','b','c']:
        print(item,x)
for item in 'pakistan':
    print(item)

user={
    'name':'asad',
    'age':25,
    'can_swing':False
}
for item in user.values():
    print(item)
for item in user.keys():
    print(item)
for key,value in user.items():
    print(key,value)
for item in range(1):
    print(list(range(0,10)))