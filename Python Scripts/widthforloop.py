width=int(input("How wide bruh?"))
zags=int(input("How many zags bruh?"))
for z in range(zags):
        for x in range (width):
            print(x*" "+"F")
        for z in range (width-2,0,-1):
            print(z*" "+"F")
