change=float(input("Please enter an amout of money. (No dollar sign): "))
totalcents=int(change*100)
dollars=totalcents//100
cents=totalcents-dollars*100
for a in range (0,dollars,100):
    if dollars-a<100:
        break
cnotes=int(a/100)

dollarsafter100s=dollars-cnotes*100
for b in range(0,dollarsafter100s,50):
    if dollarsafter100s-b<50:
            break
fifties=int(b/50)

dollarsafter50s=dollarsafter100s-fifties*50
for c in range(0,dollarsafter50s,20):
        if dollarsafter50s-c<20:
            break
twenties=int(c/20)

dollarsafter20s=dollarsafter50s-twenties*20
for d in range(0,dollarsafter20s,10):
        if dollarsafter20s-d<10:
                break
tens=int(d/10)

dollarsafter10s=dollarsafter20s-tens*10
for e in range(0,dollarsafter10s,5):
    if dollarsafter10s-e<5:
            break
fives=int(e/5)

singles=dollarsafter10s-fives*5

for f in range(0,cents, 25):
        if cents-f<25:
            break
quarters=int(f/25)

centsafterQs=cents-quarters*25
for g in range(0,centsafterQs,10):
        if centsafterQs-g<10:
                break
dimes=int(g/10)

centsafterdimes=centsafterQs-dimes*10
for h in range(0,centsafterdimes,5):
        if centsafterdimes-h<5:
                break
nickels=int(h/5)

pennies=centsafterdimes-nickels*5
print ("Your change will be:")
if cnotes>0:
        print(cnotes,"100 dollar bills")
if fifties>0:
        print(fifties,"fifties")
if twenties>0:
        print(twenties,"twenties")
if tens>0:
        print(tens,"tens")
if fives>0:
        print(fives,"fives")
if singles>0:
        print(singles,"singles")
if quarters>0:
    print(quarters,"quarters")
if dimes>0:
        print(dimes,"dimes")
if nickels>0:
    print(nickels,"nickels")
if pennies>0:
        print(pennies,"pennies")
    
