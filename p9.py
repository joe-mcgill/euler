for a in range(1,999):
    for b in range(1,999-a):
        c=1000-a-b
        if a**2+b**2==c**2: print(a*b*c)
