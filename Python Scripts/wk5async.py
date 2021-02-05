rows=["A","B","C","D"]
seats=["1","2","3","4","5","6","7","8","9","10"]
z=[]
t=""
for i in range(len(rows)):
    y=[]
    for q in range(len(seats)):
        t=rows[i]+seats[q]
        y.append(t)
        r=tuple(y)
    z.append(r)
print(z)
