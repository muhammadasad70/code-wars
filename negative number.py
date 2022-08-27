number=int(input("enter a number:\n"))
if number>0:
    number=number*-1
elif number<0:
    number=number
elif number==0:
    number=number
print(number)
def negative(number):
    if number>0:
        number=number*-1
        return number
    elif number<0:
        number=number
        return number
    elif number==0:
        number=number
        return number
    else:
        return 'invalid'
def main():
    number=int(input("enter a number:\n"))
    print(negative(number))
main()
