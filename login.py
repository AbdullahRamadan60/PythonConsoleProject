
def askForLoginEmail():
    userInput = input("please enter your email: ")
    return userInput.strip()

def askForLoginPassword():
    userInput = input("please enter your password: ")
    return userInput.strip()


def getLoginCredentailsFromFileAsListOfTuples():
    try:
        fileobject = open("users.txt", 'r')
    except Exception as e:
        print(e)
        exit()
    else:
        usersCredentialsList = []
        singleUserLine = fileobject.readlines()    
        for line in singleUserLine:
            userData = line.strip('\n')
            userData = userData.split(",")
            usersCredentialsList.append((userData[2], userData[3]))    
        fileobject.close()
        return usersCredentialsList


def isValidLoginCredentials(email , password , usersCredentialsList):
    loginCredentials = (email , password)
    if (loginCredentials in usersCredentialsList):
        return True
    else:
        return False
    
def getLoggedInUsernameByEmail(loginEmail):
    try:
        fileobject = open("users.txt", 'r')
    except Exception as e:
        print(e)
        exit()
    else:
        emailsUsernamesList = []
        singleUserLine = fileobject.readlines()    
        for line in singleUserLine:
            userData = line.strip('\n')
            userData = userData.split(",")
            emailsUsernamesList.append((userData[2] , userData[0] + " " + userData[1]))    
        fileobject.close()

        for i in emailsUsernamesList:
            if(loginEmail == i[0]):
                return i[1]

def login():
    loginEmail = askForLoginEmail()
    loginPassword = askForLoginPassword()
    if(isValidLoginCredentials(loginEmail , loginPassword , getLoginCredentailsFromFileAsListOfTuples())):
        loggedUsername = getLoggedInUsernameByEmail(loginEmail)
        print(f"You've logged in succesfully. Welcome back {loggedUsername}")
        return loggedUsername
    else:
        print("invalid email or password")


#login()
