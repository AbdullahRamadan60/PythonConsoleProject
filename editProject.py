import viewProjects
import createProject

def printEditProjectScreen(loggedUsername):
    print("Here's the list of the projects you created: ")
    viewProjects.viewLoggedInUserProjects(loggedUsername)

def askforProjectTitle():
    userInput = input("please enter the project title that you want to edit: ")
    return userInput.strip()

def isValidProjectTitle(projectTitle , loggedUsername):
    if ( len(projectTitle) != 0 and projectTitle.isalpha() and (not createProject.isUniqueProjectTitle(projectTitle)) ):
        userProjectList = viewProjects.getListOfLoggedInUserProjects(loggedUsername)
        for i in userProjectList:
            if( i[0] == projectTitle ):
                return True
    else:
        return False

def printProjectProperties():
    print("1- project title    ||    2- project details")
    print("3- total target     ||    4- start & end date")

def askForThePropertyIndexToEdit():
    userInput = input("please enter the number of data to edit: ")
    return userInput.strip()

def isValidPropertyIndex(propertyIndex):
    if ( len(propertyIndex) != 0 and propertyIndex.isdigit() and int(propertyIndex) > 0 and int(propertyIndex) <= 4 ):
        return True
    else:
        return False
    
def askForTheNewValueToAdd(propertyIndex):
    propertyIndex = int(propertyIndex)
    if(propertyIndex in range(1,4)):
        userInput = input("please enter the new value you want to add: ")
        return userInput.strip()
    elif(propertyIndex == 4):
        startDateInput = createProject.askForProjectStartDate()
        endDateInput = createProject.askForProjectEndDate()
        return (startDateInput , endDateInput)

def isValidValue(propertyIndex , value):
    propertyIndex = int(propertyIndex)
    if(propertyIndex == 1):
        return createProject.isUniqueProjectTitle(value)
    elif(propertyIndex == 2):
        return createProject.isValidProjectDetails(value)
    elif(propertyIndex == 3):
        return createProject.isValidProjectTotalTarget(value)
    elif(propertyIndex == 4):
        return createProject.isValidProjectDates(value[0] , value[1])

def editProjectDataInFile(projectTitle , propertyIndex , newValue):  
    propertyIndex = int(propertyIndex)
    allProjectsList = viewProjects.getListOfAllProjects()
    newProjectsList = list()
    for i in allProjectsList:
        if(i[0].strip() == projectTitle):
            i[propertyIndex - 1] = newValue
            newProjectsList.append(i)
        else:
            newProjectsList.append(i)   
    try:
        fileobject = open("projects.txt", 'w')
    except Exception as e:
        print(e)
        exit()
    else:
        for _list in newProjectsList:
                strFormatted = str(_list).replace('[', '').replace(']', '').replace("'" , "").replace(', ' , ',')
                fileobject.write(strFormatted + '\n')
        fileobject.close()


def editProject(loggedUsername):
    printEditProjectScreen(loggedUsername)
    projectTitle = askforProjectTitle()
    if(isValidProjectTitle(projectTitle , loggedUsername)):
        printProjectProperties()
        propertyIndex = askForThePropertyIndexToEdit()
        if(isValidPropertyIndex(propertyIndex)):
            newValue = askForTheNewValueToAdd(propertyIndex)
            if(isValidValue(propertyIndex , newValue)):
                editProjectDataInFile(projectTitle , propertyIndex , newValue)
                print("project edited successfully")                
            else:
                print("invalid value")
        else:
            print("invalid property index")
    else:
        print("invalid project title")


#editProjectDataInFile("pONe" , "2" , "descriptiiion")
#print(isValidProjectTitle("pONe" , "firstName lastName"))
#print(isValidProjectIndex("1" , "firstName lastName"))
#printProjectProperties()
#editProject("firstName lastName")
#editProject("firstName lastName")