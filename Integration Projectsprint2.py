# Arielle Fears 

# A calculator to determine the speed (mph) the user ran 

# based on the distance (feet) and time (seconds) ran. 

##Speed formula is from omnicalculator.com 

print("Hello, my name is Arielle Fears and welcome to my project!") 

print(input("Press enter after each statement to continue.")) 

print("I do overspeed training and have reached a top speed of 23.5 mph") 

print("Let's find out your speed, all you need is the distance and time that you ran!") 

print(input()) 

##Get the variables 

distance_in_feet = float(input("Enter distance ran in feet: ")) 

time_ran = float(input("Enter time ran in seconds: ",))   

##Divide distance by time to get feet per second.  

feet_per_second = distance_in_feet / time_ran 

print("You ran",format(feet_per_second,'.2f'),"feet per second!") 

print (input("Are you ready to find out your speed in mph? Press enter. ")) 

##Convert feet per second to mph 

##1 foot per second = 1/1.46666667 which equals 0.68181818. 

##This calculation is from bing conversion calculator   

miles_per_hour = feet_per_second / 1.146666667   

##Using end='' to create one line between the two print statements.   

print("You ran an average of",format(miles_per_hour,'.2f'),"miles per hour!",end='') 
print(" Let's add to this.") 

##Add a whole number to the distance ran in feet variable. 

whole_number = int(input("Enter any whole number: ")) 

new_distance = whole_number + distance_in_feet 

print("Your new distance is ",new_distance,sep='') 

print(input("Press enter.")) 

##Recalulate speed without decimals using // operator. No remainder will show. 

new_feet_per_second = new_distance // time_ran 

print("With your new distance and same time, you ran",int(new_feet_per_second),"ft/s") 

print(input("Tip: Press enter after each statement that does not require a new number.")) 

##Using the formula from before to convert to mph. 

##1 foot per second = 1/1.46666667 which equals 0.68181818. 

##I am using the floor division operatoe rto get rid of remainders/decimals.            

new_miles_per_hour = new_feet_per_second // 1.46666667 

print("Your new speed in mph is:", int(new_miles_per_hour),sep ='') 

print(input("Let's compare the speeds.")) 

##Getting rid of decimals by casting miles_per_hour to an integer. 

##I am using sep = '' to get rid of the space after the ":". 

print("Your speed before:",int(miles_per_hour),sep = '') 

print("Your speed Now:",int(new_miles_per_hour),sep = '') 

##User presses enter to continue. 

##Using the operator "-", I am subtracting the two to find the difference. 

print(input("Now let's subtract your two speeds in mph.")) 

new_miles_per_hour = new_miles_per_hour - miles_per_hour 

print("The difference of speeds is: ",int(new_miles_per_hour), sep = '') 

print(input("Just one last question.")) 

print("Was the result what you were expecting?") 

print(input("Enter yes or no: ")) 

##Two different statements for the input of the user. 
##Concatenating the two statements for variable yes. 
##Using end='' to join the two print statements on one line. 

##Using the if else statement to print different responses to the user's inputs. 

print("Was this what you expected?") 

userInput = (str(input("Enter yes or no: "))) 
optionOne = "yes" 
if userInput == "yes": 
    print("Awesome! Let's go onto the next calculations.") 
else: 
    print("Okay, Let's move on. Maybe this next part will be more fun!") 

##Creating a list and taking the average of the list.
    
print("Now let's take a look at a list of speeds:") 

def Average(list): 
    return sum(list) / len(list) 
list = [10, 15, 14, 12, 13, 16, 20] 
for x in list: 
    print(x, end=' ') 
print(input("Press enter to continue.")) 
average = Average(list) 
print("The average mph ran from this list is:", round(average, 2)) 

##Comparing the average of this list to the user's mph before. 

print("Your speed before was:", format(miles_per_hour,'.2f')) 

print(input("Press enter to continue.")) 

if miles_per_hour > average: 
    print("You ran faster than average speed!") 
elif miles_per_hour == average: 
    print("You ran average speed!") 
else: 
    print("You ran below the average speed, but dont worry these were fast running speeds!") 
print(input("Press enter to continue.")) 

##Required but not related. 

print(input("Press enter to continue to fun math!")) 
print(input("Otherwise known as.. the required portion. Press enter.")) 

##Modulus calculation  
x=5 
y=3 
print(5%3) 
##Exponent calculation 
x=2 
y=8 
print(x**y) 
##Without the variables 
print(9**4) 
##I want 100 words... 
print("words"*100) 
##This prints "words" 100 times... 
##Multiplication calculation 
x=5 
y=6 
z=9 
print(x*y*z)
##put these together for fun!
print(6**7-4+8//2%3)
##while loop
x = 1 
while x < 8: 
    print(x) 
    break 
x += 1
##For loop prints the list below.
carBrands = ["jeep","ford","tesla"] 
for x in carBrands: 
    print (x)  
##Another example of a for loop which prints the letters of the word.   
for x in "Arielle": 
    print(x)   
##does not equal statement   
x = 1 
value = int(input("Enter a whole number: ")) 
if x != 0: 
    print("This is a valid number") 
if x == 0: 
    print("This is not a valid number") 
if x < 0: 
    print("This number is a negative, not valid.")   
##range statement which prints the range between two numbers.   
for x in range(2,9): 
    print (x)   
## boolean expression
mphTwo = 10
mphThree = 22
if (mphTwo == 10) or (mphThree < 22):
    print("One or Both expressions are True")
else:
    print("Both are False!")
##End of program
print("Thank you!") 
