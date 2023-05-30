import re

def askForUserFirstName():
    userInput = input("please enter your first name: ")
    return userInput.strip()

def askForUserLastName():
    userInput = input("please enter your last name: ")
    return userInput.strip()

def askForUseEmail():
    userInput = input("please enter your email: ")
    return userInput.strip()

def askForPassword():
    userInput = input("please enter your password: ")
    return userInput.strip()

def askForConfirmPassword():
    userInput = input("please confirm your password: ")
    return userInput.strip()

def askForPhone():
    userInput = input("please enter your PhoneNumber: ")
    return userInput.strip()



def isValidFirstName(firstName):
    if ( len(firstName) != 0 and firstName.isalpha() ):
        return True
    else:
        return False
    
def isValidLastName(lastName):
    if ( len(lastName) != 0 and lastName.isalpha() ):
        return True
    else:
        return False

def isUniqueEmail(email):    #To check thsat email is not already in the users list 
    try:
        fileobject = open("users.txt", 'r')
    except FileNotFoundError as fnf:     #If the file is not created yet, we will create and open it 
        fileobject = open("users.txt" , "a")
        fileobject = open("users.txt", 'r')
    except Exception as e:
        print(e)
        exit()
    finally:
        usersEmailsList = []
        singleUserLine = fileobject.readlines()    
        for line in singleUserLine:
            userData = line.strip('\n')
            userData = userData.split(",")
            usersEmailsList.append((userData[2]))    
        fileobject.close()
        if(email in usersEmailsList):
            return False
        else:
            return True
        
def isValidEmail(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if ( len(email) != 0 and not email.isdigit() and re.fullmatch(regex , email) and isUniqueEmail(email)):
        return True
    else:
        return False
    
def isValidPassword(password , confirmPassword):
    if ( len(password) != 0 and len(confirmPassword) != 0 and password == confirmPassword ):
        return True
    else:
        return False

def isUniquePhone(phone):    #To check that phone is not already in the users list 
    try:
        fileobject = open("users.txt", 'r')
    except Exception as e:
        print(e)
        exit()
    else:
        usersPhonesList = []
        singleUserLine = fileobject.readlines()    
        for line in singleUserLine:
            userData = line.strip('\n')
            userData = userData.split(",")
            usersPhonesList.append((userData[4]))    
        fileobject.close()
        if(phone in usersPhonesList):
            return False
        else:
            return True
          
def isValidPhone(phone):
    if ( phone.isdigit() and len(phone) == 11  and  re.search('^\s*[0][1][0-2]' , phone) and isUniquePhone(phone)):
        return True
    else:
        return False


def saveUserDataInFile(userDataInList):
    try:
        fileobject = open("users.txt", 'a')
    except Exception as e:
        print(e)
        exit()
    else:
        fileobject.write(userDataInList[0] + "," + userDataInList[1] + "," + userDataInList[2] + "," + userDataInList[3] + "," + userDataInList[4] + "\n")
        fileobject.close()


def register():
    firstName = askForUserFirstName()
    if(isValidFirstName(firstName)):
        lastName = askForUserLastName()
        if(isValidLastName(lastName)):
            email = askForUseEmail()
            if(isValidEmail(email)):
                password = askForPassword()
                confirmPassword = askForConfirmPassword()
                if(isValidPassword(password , confirmPassword)):
                    phone = askForPhone()
                    if(isValidPhone(phone)):
                        saveUserDataInFile([firstName , lastName , email , password , phone])
                        print("You've registed successfully")
                        #print([firstName , lastName , email , password , phone])
                    else:
                        print("invalid phone")
                else:
                    print("invalid password")
            else:
                print("invalid email")       
        else:
            ("invalid lastName")
    else:
        print("invalid firstName.")

#register()