#(20~25 min)

# Transform the following code to a function and add exception handling (should prompt user until the valid input is entered) :

# Speeding tickets and birthdays :
def speeding():

	# Get user input for the speed and birthday
	speed = int(input("What speed were you going ? "))	
	
	birthday = input("Is it your birthday ? y/n ")
	
	if birthday.lower() == "y":
		speed -= 5
	
	# Check the speed, and give the appropriate ticket. 
	if speed <= 60:
		print("No ticket for you.") 
	elif 61 <= speed <= 80:
		print("Small ticket for you.") 
	else:
		print("Big fat ticket for you.")






# Create a single function that takes in as an argument a file name and writes to a file the 99 bottles of beer song. It should then read in the file and print the song to the console to the console.


	






















