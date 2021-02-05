k=int(input("Please enter the (integer) length of the row: "))
smallBrick=int(input("How many small bricks do you have? "))
largeBrick=int(input("How many large bricks do you have? "))
for x in range (largeBrick*5, 0, -5):
  if k>=x:
    break
remaininglength=k-x
if k-x>smallBrick:
    print("Sorry.  Not possible.")
else:
    print("This is possible with",int(x/5),"large bricks and",k-x,"small bricks.")
