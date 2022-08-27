def highest_even_num(li):
    evens=[]
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)

print(highest_even_num([1,2,3,4,10,23,24]))

lis=int(input(["enter a number:\n"]))
print(lis)



