def get_grade(s1,s2,s3):
    sum = s1 + s2 + s3
    average = sum / 3
    if average>90 and average<=100:
        return 'A'
    elif average>80 and average<=90:
        return 'B'
    elif average>70 and average<=80:
        return 'C'
    elif average>60 and average<=70:
        return 'D'
    elif average>50 and average<=60:
        return 'E'
    elif average<50 and average<=50:
        return 'F'

def main():
    s1=int(input("enter 1st number:\n"))
    s2 = int(input("enter 2nd number:\n"))
    s3 = int(input("enter 3rd number:\n"))
    print(get_grade(s1,s2,s3))
main()
