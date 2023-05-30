import viewProjects
import createProject

def printDeleteProjectScreen(loggedUsername):
    print("Here's the list of the projects you created: ")
    viewProjects.viewLoggedInUserProjects(loggedUsername)

def askforProjectTitle():
    userInput = input("please enter the project title that you want to delete: ")
    return userInput.strip()

def isValidProjectTitle(projectTitle , loggedUsername):
    if ( len(projectTitle) != 0 and projectTitle.isalpha() and (not createProject.isUniqueProjectTitle(projectTitle)) ):
        userProjectList = viewProjects.getListOfLoggedInUserProjects(loggedUsername)
        for i in userProjectList:
            if( i[0] == projectTitle ):
                return True
    else:
        return False


def deleteProjectDataInFile(projectTitle):  
    allProjectsList = viewProjects.getListOfAllProjects()
    newProjectsList = list()
    for i in allProjectsList:
        if(i[0].strip() == projectTitle):
            #don't append it
            pass
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


def deleteProject(loggedUsername):
    printDeleteProjectScreen(loggedUsername)
    projectTitle = askforProjectTitle()
    if(isValidProjectTitle(projectTitle , loggedUsername)):
        deleteProjectDataInFile(projectTitle) 
        print("project deleted successfully")               
    else:
        print("invalid project title")


#deleteProject("firstName lastName")