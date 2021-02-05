def largeofTen():
    largeSoFar=0
    a=float(input("PLease enter the first of ten values: "))
    b=float(input("and the 2nd value: "))
    if a>b:
        largeSoFar=a
    else:
        largeSoFar=b
    c=float(input("3rd value: "))
    if c>largeSoFar:
        largeSoFar=c
    d=float(input("4th value: "))
    if d>largeSoFar:
        largeSoFar=d
    e=float(input("5th value: "))
    if e>largeSoFar:
        largeSoFar=e
    f=float(input("6th value: "))
    if f>largeSoFar:
        largeSoFar=f
    g=float(input("7th value: "))
    if g>largeSoFar:
        largeSoFar=g
    h=float(input("8th value: "))
    if h>largeSoFar:
        largeSoFar=h
    i=float(input("9th value: "))
    if i>largeSoFar:
        largeSoFar=i
    j=float(input("And finally the 10th value: "))
    if j>largeSoFar:
        largeSoFar=j
    print("The largest value you entered was: ", largeSoFar)
largeofTen()
