TotalSeconds=int(input("Enter a number of seconds: "))
TotalMinutes=TotalSeconds//60
Seconds=TotalSeconds%60
Hours=TotalMinutes//60
Minutes=TotalMinutes%60
print (TotalSeconds," seconds is ",Hours,"hours,",Minutes," minutes and ", Seconds, "seconds.")
