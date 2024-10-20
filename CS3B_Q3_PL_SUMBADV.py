import random     #import the module to pick a random number

userGuess = 0     #initialized value for variable userGuess and computerGuess
computerGuess = 0

def guesses():    #initialize a function guesses()
    global userGuess   #access the globally scoped variable
    userGuess = input("There are 10 Students, how many do you guess passed?: ") #the program must accept an input from the user
    
    global computerGuess    #access the globally scoped variable
    computerGuess = random.randrange(1, 10) #the computerGuess must be assigned with a random number every run with a range of 1 - 10

    print(f"Your guess is {userGuess}")     #print the user's Guess, utilise the f string "Your Guess is [userGuess]"
    print(f"The Computer Guess is {computerGuess}")     #print the computer's Guess, utilise the f string "The Computer Guess is [computerGuess]"
    continueProgram = input("Continue the evaluation? (Yes/YES): ")     #the program must accept an input from the user

guesses()

studentList = {
  "studentOne" : {
  "studentName": "Ricardo P",    #1
  "studentGrade": 85,
  "classSubject": "DSA"
  }, 
  "studentTwo": {
  "studentName": "Anagracia A",  #2
  "studentGrade": 82,
  "classSubject": "DSA"
  }, 
  "studentThree": {
  "studentName": "Anastacia D",  #3
  "studentGrade": 75,
  "classSubject": "DSA"
  }, 
  "studentFour": {
  "studentName": "Gregorio D",  #4
  "studentGrade": 74,
  "classSubject": "DSA"
  }, 
  "studentFive" : {
  "studentName": "Alegro",  #5
  "studentGrade": 95,
  "classSubject": "DSA"
  }, 
  "studentSix" :  {
  "studentName": "Maria Juana",  #6
  "studentGrade": 90,
  "classSubject": "DSA"
  }, 
  "studentSeven" : {
  "studentName": "Shantal T",   #7
  "studentGrade": 83,
  "classSubject": "OS"
  }, 
  "studentEight" :{
  "studentName": "Mariano J",   #8
  "studentGrade": 91,
  "classSubject": "OS"
  }, 
  "studentNine" : {
  "studentName": "Josefa G",   #9
  "studentGrade": 73,
  "classSubject": "OS"
  }, 
  "studentTen" : {
  "studentName": "Eliseo S",   #10
  "studentGrade": 75,
  "classSubject": "OS"
  }
}

sizeClass = len(studentList)             #assign the length of the studentList (this is a dictionary)
passStudents = []               #instantiate this as a blank list
failedStudents = []               #instantiate this as a blank list
pStudentCounter = 0               #instantiate this passed student counter as an integer with initial value
fStudentCounter =  0              #instantiate this passed student counter as an integer with initial value

def counterPass():                  #create a counterPass() function in here to serve as your counter for passed students
    global pStudentCounter          #access your global pStudentCounter here
    pStudentCounter += 1            #create a counter here for your pStudentCounter

def counterFail():                  #create a counterFail() function in here to serve as your counter for failed students 
    global fStudentCounter          #access your global fStudentCounter here
    fStudentCounter += 1            #create a counter here for your fStudentCounter

def testGrade(name, grade, subject):    #create a function testGrade() that must receive a parameter: name, grade, subject
    if grade >= 75:                     #checks if the grade of the passed parameter is greater than or equal to 75
        passStudents.append(name)       #if so append the following to the passStudents List: name, grade, and subject; hint: this is multiline
        passStudents.append(grade)
        passStudents.append(subject)

        counterPass()                   #in every passed students call your counterPass() to increment the pStudentCounter  
    else:
        failedStudents.append(name)     #if so append the following to the failedStudents List: name, grade, and subject; hint: this is multiline
        failedStudents.append(grade)
        failedStudents.append(subject)

        counterFail()                   #in every failed students call your counterFail() to increment the fStudentCounter

def guessedNearer():  #create a function guessedNear()
    global userGuess, computerGuess, pStudentCounter    #access locally all the global variable noted as: userGuess, computerGuess, pStudentCounter. Hint: This can be multilin

    nearUGuess = pStudentCounter - int(userGuess)       #subtract the pStudentCounter with the converted datatype of userGuess
    nearCGuess = pStudentCounter - computerGuess        #subtract the pStudentCounter with the converted datatype of userGuess

    if abs(nearCGuess) < abs(nearUGuess):     #implement an if statement to test if the user guess's nearer than the computer's
                                              #by comparing the nearUGuess and nearCGuess, make sure that the values are absolute
                                             #enclosed your variables with abs() for absolute value
        print("")                             
        print("User is Nearer",nearUGuess)    #call the value of nearUGuess

    elif abs(nearCGuess) < abs(nearUGuess):     #implement an elif statement to test if the user guess's and the computer's are the same
                                                #by comparing the nearUGuess and nearCGuess, make sure that the values are absolute 
                                                #enclosed your variables with abs() for absolute value
        print("")                               
        print("User and Computer are the same")
    
    else:
        print("")
        print("Computer Guess is Nearer", nearCGuess)   #call the value of nearCGuess

def printList():  #create a function printList()
    print("")
    print("----------- List of Students who has a Passing Mark --------------------")
    print(passStudents)     #print the list of passStudent
    print(f"Total no. of Failed Students: {pStudentCounter}")   #use the fstring format, print out the "Total no. of Passed Students: {pStudentCounter}

    print("")
    print("------------ List of Students who has a Faily Mark ---------------------")
    print(failedStudents)   #print the list of failedStuden
    print(f"Total no. of Failed Students: {fStudentCounter}")   #use the fstring format, print out the "Total no. of Failed Students: {fStudentCounter}

print(f"The following are the List of Students. Total of {sizeClass}")  #print out using the fstring "The following are the List of Students. Total of {sizeClass}" then calls out the size of the class
print("----------------------------------------------------")

for x, obj in studentList.items():      #create a for loop which will extract the items content (key:value) with x and obj vars;       
                                         #   noting the receiving value will be "x" and "obj" for each of the items in the studentList
    print(f"{obj.get('studentName')} is enrolled in {obj.get('classSubject')}")     #create a print out which for each of the item retrieved
                                                                                    #   using the for loop must equate to : "{studentName} is enrolled in {classSubject}"
                                                                                     #   utilise your .get("") for your objects to get the studentName and classSubject
for x, obj in studentList.items():      #create a for loop which will extract the items content (key:value) with x and obj vars;
                                        #   noting the receiving value will be "x" and "obj" for each of the items in the studentList
    testGrade(obj.get("studentName"), obj.get("studentGrade"), obj.get("classSubject"))     #pass the following parameters to testGrade() for each retrieved item in the for loop
                                                                                            #   studentName, studentGrade, classSubject; utilise .get("key name") to your obj var.

printList()         #call the printList()
guessedNearer()     #call the guessedNear()

