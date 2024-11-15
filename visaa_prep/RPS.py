x,y=input().split()
if x=='R':
    if y == 'P':
        print("Charan")
    elif y=='S':
        print("Vignesh")
    else:
        print("NULL")
elif x=='P':
    if y == 'S':
        print("Charan")
    elif y == 'R':
        print("Vignesh")
    else:
        print("NULL")
elif x=='S':
    if y == 'R':
        print("Charan")
    elif y == 'P':
        print("Vignesh")
    else:
        print("NULL")
