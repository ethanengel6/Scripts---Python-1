while True:

  bday=input("Is today your birthday? Y or N ")
  if bday == "Y" or bday == "N" or bday =="y" or bday =="n":
    break
speed=int(input("Do you know how fast you were going? "))

if (speed<=60 and (bday=="N" or bday=="n")) or (speed<=65 and (bday=="Y" or bday=="y")):
        print("No ticket.  Have a nice day!")
elif (speed>60 and speed<=80 and(bday=="N" or bday=="n")) or (speed>65 and speed<=85 and (bday=="Y" or bday=="y")):
        print("I'm going to have to write a ticket with a small fine.")
else:
    print("That's a ticket with a BIG FAT FINE!")
