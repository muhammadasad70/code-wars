def are_you_playing_banjo(name):
    var=name[0]
    if var=='R' or var=='r':
        return True
    else:
        return False
def main():
    name=input("enter your name:\n")
    if are_you_playing_banjo(name)==True:
        print(name ,"play banjo")
    else:
        print(name,"does not play banjo")
main()







