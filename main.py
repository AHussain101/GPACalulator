import math
import time
def gpaCalculator(honorsNum, glist):
    points = {"a":4, "b":3, "c":2, "d":1, "f":0}
    #Initialize Variables
    letterNum = 0
    unweighted = 0
    weighted = 0
    #Access point values from dictionary and add them to the unweighted var
    #Increment letternum by 1.
    #Add letter points to weighted (Saves time)
    for letter in glist:
        letterNum += 1
        unweighted += points[letter]
        weighted += points[letter]
    #Calculate unweighted GPA
    unweightedGPA =(math.floor((unweighted/letterNum)*100))/100
    #Calculate Weighted GPA
    weightedGPA = unweighted + honorsNum 
    weightedGPA = (weightedGPA/letterNum)*100
    weightedGPA = (math.floor(weightedGPA))/100
    print("\nYour unweighted GPA is: " + str(unweightedGPA))
    print("Your weighted GPA is: " + str(weightedGPA))
    analysis = ["Congrats on getting that 4.0, keep up the hard work!\n", "Not bad, push yourself harder!\n", "You have lots of room for improvement, but do not give up!!\n"]
    if unweightedGPA == 4.0:
      print(analysis[0])  
    if unweightedGPA >= 3.0 and unweightedGPA < 4.0:
      print(analysis[1]) 
    if unweightedGPA < 3.0:
      print(analysis[2])
        
def main():
    print('Welcome to the GPA calculator!\n')
    #Create List
    global glist
    global honorsNum
    glist = []
    points = {"a":4, "b":3, "c":2, "d":1, "f":0, "A":4, "B":3, "C":2, "D":1, "F":0, " ":'n/a', "+":0, "-":0, ",":0}
    #Asks for number of honors classes
    while True:
        try:
            honorsNum = int(input("How many honors/ap classes do you have? "))
            if type(honorsNum) == int:
              break
        except:
            print("Enter only an integer value")
    #Ask for each class grade
    grades = input('Enter your grades. \nFor example: "A B C D A", "a a b c a", "aabca": ')
    if len(grades)*2 < (honorsNum*2-1):
        grades = input('\n Bad input. Try again: ')
    elif len(grades)*2 > (honorsNum*2-1):
        print('Calculating GPA...')
        time.sleep(2)
    for let in grades:
      if let not in points.keys() :
        grades = input('Sorry your grades contain a grade outside "A B C D F" \nEnter your grades separated by a space. \nFor example: "A B C D A" : ')
    #Grab letters and put them in a list
    for letter in grades:
        if (letter.isalpha()):
            glist.append(letter.lower())
    #calling function
    gpaCalculator(honorsNum, glist)
main()
