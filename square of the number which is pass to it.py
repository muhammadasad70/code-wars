def sqrt():
     num=int(input("enter the number you want to enter:\n"))
     i=1
     sum=0
     while i<=num:
         number=int(input("enter the number:\n"))
         sqrt=number*number
         sum=sum+sqrt
         i=i+1
     return sum
def main():
    print("the sum of the square of the number is:",sqrt())
main()

