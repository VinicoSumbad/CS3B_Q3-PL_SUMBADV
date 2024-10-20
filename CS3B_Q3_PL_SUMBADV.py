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

def counterPass():
    global pStudentCounter
    pStudentCounter += 1

def counterFail():
    global fStudentCounter
    fStudentCounter += 1

def testGrade(name, grade, subject):
    if grade >= 75:
        passStudents.append(name)
        passStudents.append(grade)
        passStudents.append(subject)

        counterPass()
    else:
        failedStudents.append(name)
        failedStudents.append(grade)
        failedStudents.append(subject)

        counterFail()

def guessedNearer():
    global userGuess, computerGuess, pStudentCounter

    nearUGuess = pStudentCounter - int(userGuess)
    nearCGuess = pStudentCounter - computerGuess

    if abs(nearCGuess) < abs(nearUGuess):
        print("")
        print("User is Nearer",nearUGuess)

    elif abs(nearCGuess) < abs(nearUGuess):
        print("")
        print("User and Computer are the same")
    
    else:
        print("")
        print("Computer Guess is Nearer", nearCGuess)

def printList():
    print("")
    print("----------- List of Students who has a Passing Mark --------------------")
    print(passStudents)
    print(f"Total no. of Failed Students: {pStudentCounter}")

    print("")
    print("------------ List of Students who has a Faily Mark ---------------------")
    print(failedStudents)
    print(f"Total no. of Failed Students: {fStudentCounter}")

print(f"The following are the List of Students. Total of {sizeClass}")
print("----------------------------------------------------")

for x, obj in studentList.items():
    print(f"{obj.get('studentName')} is enrolled in {obj.get('classSubject')}")

for x, obj in studentList.items():
    testGrade(obj.get("studentName"), obj.get("studentGrade"), obj.get("classSubject"))

printList()
guessedNearer()

