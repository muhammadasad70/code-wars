def bool_to_word(boolean):
    if boolean == 'True' or boolean == 'true':
        return "yes"
    elif boolean == 'False' or boolean == 'false':
        return "No"

def main():
    boolean=input("enter True and False:\n")
    print(bool_to_word(boolean))

main()

