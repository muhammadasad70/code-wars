def rvs(string):
    rvs = string[-1::-1]
    return rvs


def main():
    string = input("enter the string:\n")
    print(rvs(string))


main()
print("hellow")
