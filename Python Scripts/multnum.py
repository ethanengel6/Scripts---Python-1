while True:
  multnum=int(input("Please enter a non-negative integer. "))
  if multnum>=0:
    break
if multnum%15!=0 and (multnum%5==0 or multnum%3==0):
    print("True")
else:
        print("False")
