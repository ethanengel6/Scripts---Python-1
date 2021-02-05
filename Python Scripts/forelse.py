import random

for x in range (5):
  y = random.randint(-10,100)
  if y<0:
    break
else:
  print("no negative generated")
