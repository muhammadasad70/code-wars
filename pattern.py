pattern=[
    [1,0,0,0,0],
    [1,1,0,0,0],
    [1,1,1,0,0],
    [1,1,0,1,0],
    [1,0,1,0,1]
]
for row in pattern:
    for pixel in row:
        if pixel==1:
            print('*',end='')
        else:
            print(' ',end='')
    print(' ')