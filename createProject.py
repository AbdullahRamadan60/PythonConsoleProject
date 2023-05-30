from datetime import datetime
import re
#import login

def askForProjectTitle():
    userInput = input("please enter the project title: ")
    return userInput.strip()

def askForProjectDetails():
    userInput = input("please enter the project details: ")
    return userInput.strip()

def askForProjectTotalTarget():
    userInput = input("please enter the project total taget: ")
    return userInput.strip()

def askForProjectStartDate():
    userInput = input("please enter the project start date (YYYY-MM-DD): ")
    return userInput.strip()

def askForProjectEndDate():
    userInput = input("please enter the project end date (YYYY-MM-DD): ")
    return userInput.strip()

def isUniqueProjectTitle(projectTitle):    #To check thsat project title is not already in the projects list (Like ID for the project)
    projTitle  = projectTitle
    try:
        fileobject = open("projects.txt", 'r')
    except FileNotFoundError as fnf:     #If the file is not created yet, we will create and open it 
        fileobject = open("projects.txt" , "a")
        fileobject = open("projects.txt", 'r')
    except Exception as e:
        print(e)
        exit()
    finally:
        projectTitlesList = []
        singleProjectLine = fileobject.readlines()    
        for line in singleProjectLine:
            projectData = line.strip('\n')
            projectData = projectData.split(",")
            projectTitlesList.append((projectData[0]))    
        fileobject.close()
        if(projectTitle in projectTitlesList):
            return False
        else:
            return True

def isValidProjectTitle(projectTitle):
    if ( len(projectTitle) != 0 and projectTitle.isalpha() and isUniqueProjectTitle(projectTitle) ):
        return True
    else:
        return False
    
def isValidProjectDetails(projectDetails):
    if ( len(projectDetails) != 0 ):
        return True
    else:
        return False
        
def isValidProjectTotalTarget(projectTotalTarget):
    if ( len(projectTotalTarget) != 0 and  projectTotalTarget.isdigit() and int(projectTotalTarget) > 0 ):
        return True
    else:
        return False
    
def isValidProjectDates(ProjectStartDate , projectEndDate):
    regex = "^202[3-9]-((0[1-9])|(1[0-2]))-(0[1-9]|[1-2][0-9]|3[0-1])$"    # YYYY-MM-DD  (years from 2023 to 2029)
    if ( len(ProjectStartDate) != 0 and len(projectEndDate) != 0 and re.match(regex , ProjectStartDate) and re.match(regex , projectEndDate) and ProjectStartDate >= datetime.now().strftime("%Y-%m-%d") and projectEndDate > datetime.now().strftime("%Y-%m-%d") and ProjectStartDate < projectEndDate):
        return True
    else:
        return False

def saveProjectDataInFile(projectDataInList):
    try:
        fileobject = open("projects.txt", 'a')
    except Exception as e:
        print(e)
        exit()
    else:
        fileobject.write(projectDataInList[0] + "," + projectDataInList[1] + "," + projectDataInList[2] + "," + projectDataInList[3] + "," + projectDataInList[4] + "," + projectDataInList[5] + "\n")
        fileobject.close()


def createProject(createdByUser):
    projectTitle = askForProjectTitle()
    if(isValidProjectTitle(projectTitle)):
        projectDetails = askForProjectDetails()
        if(isValidProjectDetails(projectDetails)):
            projectTotalTarget = askForProjectTotalTarget()
            if(isValidProjectTotalTarget(projectTotalTarget)):
                projectStartDate = askForProjectStartDate()
                projectEndtDate = askForProjectEndDate()
                if(isValidProjectDates(projectStartDate , projectEndtDate)):
                    saveProjectDataInFile([projectTitle , projectDetails , projectTotalTarget , projectStartDate , projectEndtDate , createdByUser])
                    print("project created successfully")
                    #print([projectTitle , projectDetails , projectTotalTarget , projectStartDate , projectEndtDate, createdByUser])
                else:
                    print("invalid project dates")
            else:
                print("invalid project total target")       
        else:
            ("invalid project details")
    else:
        print("invalid project title")

#loggedUserName = login.login()
#createProject(loggedUserName)