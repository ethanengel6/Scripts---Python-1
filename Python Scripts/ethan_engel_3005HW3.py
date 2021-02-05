#1
def calcSum (a,b,c):
    if a!=b and b!=c and a!=c:
        return a+b+c
    elif a==b and b!=c:
        return a+c
    elif (a==c and a!=b) or (b==c and a!=b):
        return a+b
    else:
        return a

#2
def intDiff(a,b,c):
        if abs(a-b)<=1 and abs(a-c)>=2 and abs(b-c)>=2:
            return True
        elif abs(a-c)<=1 and abs(a-b)>=2 and abs(b-c)>=2:
            return True
        else:
            return False

#3
def multTable(q):
        for i in range(1,q+1):
            print("4 x",i,"=",4*i)

#4
def numToWords(i):
    import math
    shrinker=i
    while shrinker>1:
        shrinker/=10
    powerTen=int(i/shrinker)
    numAsString=""
    while powerTen>=10:
        shrinker=shrinker*10
        if int(shrinker)==1:
            numAsString=numAsString+" one"
        elif int(shrinker)==2:
            numAsString=numAsString+" two"
        elif int(shrinker)==3:
            numAsString=numAsString+" three"
        elif int(shrinker)==4:
            numAsString=numAsString+" four"
        elif int(shrinker)==5:
            numAsString=numAsString+" five"
        elif int(shrinker)==6:
            numAsString=numAsString+" six"
        elif int(shrinker)==7:
            numAsString=numAsString+" seven"
        elif int(shrinker)==8:
            numAsString=numAsString+" eight"
        elif int(shrinker)==9:
            numAsString=numAsString+" nine"
        else:
            numAsString=numAsString+" zero"
        shrinker=shrinker-int(shrinker)
        powerTen=powerTen/10
    print(numAsString)

#5
def userMeasurements():
    height=int(input("What is your height in inches? "))
    weight=int(input("What is your weight in pounds? "))
    age=int(input("How old are you? "))
    def hSize():
        hatSize=round(weight/height*2.9,2)
        print("Your hat size is: ",hatSize)
    def jSize():
        jacketSize=round(height*weight/288,2)
        if age>=30:
            jsAddition=.125*int((age-30)/10)
            jacketSize=round(jacketSize+jsAddition,2)
        print("Your jacket size is: ",jacketSize)
    def wSize():
        waistSize=round(weight/5.7,2)
        if age>=28:
            wsAddition=.1*int((age-28)/2)
            waistSize=round(waistSize+wsAddition,2)
        print("Your waist size is: ",waistSize)
    choice=input("Which measurement would you like? 1) Hat size    2)Jacket size      3) Waist size      ")
    if choice=="1":
        hSize()
    if choice=="2":
        jSize()
    if choice=="3":
        wSize()
    measurement=input("Would you like to take another measurement? y/n ")
    if measurement=="y":
                userMeasurements()
measurement=input("Would you like to take a measurement? y/n ")
if measurement=="y":
        userMeasurements()
