def cat_and_mouse(x,y,z):

    cat_1=abs(z-x)
    cat_2=abs(z-y)

    if cat_1 < cat_2:
        return 'Cat A'
    elif cat_1==cat_2:
        return 'Mouse C'
    else:
        return 'Cat B'
    

print(cat_and_mouse(1,3,2))