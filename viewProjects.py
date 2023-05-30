
def viewAllProjects():    
    try:
        fileobject = open("projects.txt", 'r')
    except Exception as e:
        print(e)
        exit()
    else:
        filedata = fileobject.readlines()           
        fileobject.close()
        for i , line in enumerate(filedata , 1):
            line = line.strip('\n')
            print(f"{i}- {line}")     

def getListOfAllProjects():
    try:
        fileobject = open("projects.txt", 'r')
    except Exception as e:
        print(e)
        exit()
    else:
        allProjectsList = []
        singleProjectLine = fileobject.readlines()    
        for line in singleProjectLine:
            userData = line.strip('\n')
            userData = userData.split(",")
            allProjectsList.append(userData)
        fileobject.close()
        return allProjectsList   

def getNumOfAllProjects():    
    try:
        fileobject = open("projects.txt", 'r')
    except Exception as e:
        print(e)
        exit()
    else:
        filedata = fileobject.readlines()
        numOfLines = len(filedata)           
        fileobject.close()
        return numOfLines

def viewLoggedInUserProjects(loggedUsername):
    try:
        fileobject = open("projects.txt", 'r')
    except Exception as e:
        print(e)
        exit()
    else:
        userProjectsList = []
        singleUserLine = fileobject.readlines()    
        for line in singleUserLine:
            userData = line.strip('\n')
            userData = userData.split(",")
            if(loggedUsername in userData):
                formatteduserDataStr = str(userData).replace('[', '').replace(']', '').replace("'" , "").replace(', ' , ',')
                userProjectsList.append(formatteduserDataStr)
        fileobject.close()
        for i , line in enumerate(userProjectsList , 1):
            line = line.strip('\n')
            print(f"{i}- {line}")

def getListOfLoggedInUserProjects(loggedUsername):
    try:
        fileobject = open("projects.txt", 'r')
    except Exception as e:
        print(e)
        exit()
    else:
        userProjectsList = []
        singleUserLine = fileobject.readlines()    
        for line in singleUserLine:
            userData = line.strip('\n')
            userData = userData.split(",")
            if(loggedUsername in userData):
                userProjectsList.append(userData)
        fileobject.close()
        return userProjectsList
         
def getNumOfLoggedInUserProjects(loggedUsername):
    try:
        fileobject = open("projects.txt", 'r')
    except Exception as e:
        print(e)
        exit()
    else:
        userProjectsList = []
        singleUserLine = fileobject.readlines()    
        for line in singleUserLine:
            userData = line.strip('\n')
            userData = userData.split(",")
            if(loggedUsername in userData):
                userProjectsList.append(userData) 
        fileobject.close()
        return len(userProjectsList)


#print(getListOfAllProjects())
#print(getListOfLoggedInUserProjects("firstName lastName"))
#viewProjects()
#print(getNumOfProjects())
#viewLoggedInUserProjects("firstName lastName")
#print(viewLoggedInUserProjects("firstName lastName"))
#print( getNumOfLoggedInUserProjects("firstName lastName") )