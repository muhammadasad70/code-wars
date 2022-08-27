def hellow(name, emoji):
    print(f'hellow, {name} {emoji}  :')


hellow('asad', '')
print('pakistan'.capitalize('pakistan'))
def test(a):
    '''
    info: this function is test and print param in a
    '''
    print(a)
print(test.__doc__)
def is_even(num):
    return num%2==0
print(is_even(50))
#......................................................................#
#the use of *args and *kwargs
def super_func(*args):
    return sum(args)
print(super_func(1,2,3,4,5,1000,2000,93232,8848))