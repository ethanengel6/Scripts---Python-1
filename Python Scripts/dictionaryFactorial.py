factorialDictionary={}
factorialDictionary[int(1)]=1
factorialDictionary={n:n*factorialDictionary[int(n-1)] for n in range(2,20)}
print(factorialDictionary)
