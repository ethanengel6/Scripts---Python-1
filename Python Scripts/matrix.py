def matrix():
  import random
  rows = random.randint(1,10)
  columns=random.randint(1,10)
  min=0
  max=100
  element=""
  for x in range (1,rows):
      element=""
      for y in range (1,columns):
            element += str(random.randint(min,max))+ " "
      print(element)
matrix()
