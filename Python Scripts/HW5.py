#1
def minMaxTuple(List):
    """Takes a list, named List, as an argument and sets the min & max to the first element in the list.  Then goes through the list comparing values.  If a larger value is reached, it replaces the max value.  Then repeats the process for minimum.  This min/max pair is returned as a tuple, named extremes."""

    Largest=List[0]
    Smallest=List[0]
    #Loop to find the list max
    for q in range(len(List)-1):
        if List[q+1]>Largest:
            Largest=List[q+1]
    #Loop to find the list minimum
    for z in range(len(List)-1):
        if List[z+1]<Smallest:
            Smallest=List[z+1]
    #finalizing the tuple
    extremes=(Smallest,Largest)
    return(extremes)
#2
def allPairs(listX,listY):
    """The function takes two lists as arguments, listX & listY.  We will nest a y loop in an x loop.  In each iteration, we will check to see if x=y and if not, will add a coordinate pair tuple to the list.  This list of tuples, pairsList, is returned."""
    pairsList=[]
    for b in range(len(listX)):
        for c in range(len(listY)):
            if listX[b]!=listY[c]:
                pairsList.append((listX[b],listY[c]))
    return(pairsList)

#3
def distance(pointList):
    """Takes a list of tuple pairs, named pointList as an argument.  First sets the distance between the first 2 points in the list as the shortest.  Then, using the distance formula& iterations, compares all other distances.  If a shorter distance is found between 2 points, those two points are substituted as the new shortest distance tuple. This pair of points is returned as a tuple of tuples named smallDistTuple."""
    smallestDistance=((pointList[0][0]-pointList[1][0])**2+(pointList[0][1]-pointList[1][1])**2)**.5
    smallDistTuple=()
    for w in range (len(pointList)-1):
        v=w+1
        while v<len(pointList):
            if ((pointList[w][0]-pointList[v][0])**2+(pointList[w][1]-pointList[v][1])**2)**.5<smallestDistance:
                smallestDistance=((pointList[w][0]-pointList[v][0])**2+(pointList[w][1]-pointList[v][1])**2)**.5
                smallDistTuple=(pointList[w],pointList[v])
            v=v+1
    print(smallDistTuple)
    return(smallDistTuple)


#4
def removeDups(tupleList):
    """A list argument, named tupleList is scanned for all redundancies.  Those redundancies are placed in a new list of elements to be removed from the original.  They are then removed accordingly.  The amended tupleList is returned."""
    dupList=[]
    #finding redundancies
    for zz in range(len(tupleList)):
        if tupleList.count(tupleList[zz])>1 and dupList.count(tupleList[zz])+1<tupleList.count(tupleList[zz]):
            dupList.append(tupleList[zz])
    #removing redundancies
    for yy in range(len(dupList)):
        tupleList.remove(dupList[yy])
    return(tupleList)
