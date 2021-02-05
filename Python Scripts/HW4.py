#1
allEven=[i for i in range(3,1000) if i%6==0]

#2
primeNum=[2]
a=3
while len(primeNum)<10:
    for b in range (2,int(a-1)):
        if a%b==0:
            break
        else:
            primeNum.append(a)
    a+=1

#3
def firstLast(list):
    """First and last elements of any list returned"""
    return [list[0],list[-1]]

#4
def listSum(list):
    "Sums the elements of a list by adding them one at a time"""
    sum=list[0]
    for q in range(1,len(list)):
        sum+=list[q]
    return(sum)


#5
def commonElems(firstlist,secondlist):
    """First identifies the longer of 2 lists.  Then goes through the lists looking for common elements, checking against each item in the longer list.  If there are any duplicates, they are deleted out"""
    commonElemList=[]
    if len(firstlist)>len(secondlist):
        for q in range(len(firstlist)):
            if firstlist[q] in secondlist:
                commonElemList.append(firstlist[q])
    elif len(secondlist)>=len(firstlist):
        for q in range(len(secondlist)):
            if secondlist[q] in firstlist:
                commonElemList.append(secondlist[q])
    z=0
    for x in range(len(commonElemList)):
        if commonElemList.count(commonElemList[z])>1:
            del commonElemList[z]
        else:
            z+=1
    return(commonElemList)

#6
def uniqueElems(list):
    """Checks for unique elements of a list (count =1)"""
    uelist=[]
    for s in range(len(list)):
        if list.count(list[s])==1:
            uelist.append(list[s])
    return(uelist)

#7
def sortList(listtoSort):
    """Takes a numerical list and starts at the last element, comparing to each before it. If it is smaller than the previous, it moves it to the left."""

    for q in range(len(listtoSort),1,-1):
        for z in range(len(listtoSort),1,-1):
            if listtoSort[z-1]<listtoSort[z-2]:
                listtoSort.insert(z-2,listtoSort.pop(z-1))
    return(listtoSort)

#8
def rotateList(a,k):
    """Takes the first element of a list & puts it at the end.  Goes through this process k times"""
    for w in range(k):
        a.append(a.pop(0))
    return(a)

#9
binList=[7,7,7,7,7]
playerturn=1
print("Player 1 you are up!")
def removeMatches(binChoice,numMatches,binList):
    """Player chooses a bin 1-5 and a number of matches to remove, up to the number remining in that bin.  Then alternates the turn"""
    global playerturn

    if binChoice<1 or binChoice>5:
        print("Bin must be 1,2,3,4 or 5! ")
        removeMatches(int(input("From which bin would you like to select?(1-5) ")),int(input("How many matches are you taking from the bin? ")),binList )
    else:
        if numMatches==0:
            print("Gotta take a match bruh!")
            removeMatches(int(input("From which bin would you like to select?(1-5) ")),int(input("How many matches are you taking from the bin? ")),binList )
        elif numMatches<=binList[binChoice-1]and numMatches>0:
                binList[binChoice-1]=binList[binChoice-1]-numMatches
                playerturn+=1
                displayGame(binList)
                checkGameEnd(binList)
                return True
        elif numMatches>binList[binChoice-1]:
            print("Too many matches man!")
            removeMatches(int(input("From which bin would you like to select?(1-5) ")),int(input("How many matches are you taking from the bin? ")),binList )
def checkGameEnd(binList):
    """Sees if all the bins are empty.  If so a winner is declared.  If not the game turn function reiterates"""
    if binList==[0,0,0,0,0]:
        if playerturn%2!=0:
            print("Player one wins!")
        else:
            print("Player two wins!")
            return True
    else:
        if playerturn%2==0:
            print("Player 2's turn:")
        else:
            print("Player 1's turn:")
        removeMatches(int(input("From which bin would you like to select?(1-5) ")),int(input("How many matches are you taking from the bin? ")),binList )
        return False

def displayGame(binList):
    """Displays the remaining number of matches in each bin after a turn"""
    print("|",binList[0],"|     |",binList[1],"|     |",binList[2],"|     |",binList[3],"|     |",binList[4],"|")
    print("")


removeMatches(int(input("From which bin would you like to select?(1-5) ")),int(input("How many matches are you taking from the bin? ")),binList )
