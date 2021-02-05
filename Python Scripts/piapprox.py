approx=1
for x in range(1,50):
  approx=approx+((-1)**x)*(1/(x*2+1))
 
print(approx*4)
