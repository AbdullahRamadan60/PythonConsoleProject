import register
import login
import createProject
import viewProjects
import editProject
import deleteProject

def main():
    isloggedIn = False
    while True:
        print("     1- Register    || 2- Login    || 3- exit")
        userinput = input("please choose the operation you want to make: ")
        if( len(userinput) != 0 and userinput.isdigit() and int(userinput) > 0 and int(userinput) < 3 ):
            if(int(userinput) == 1):
                register.register()
                continue
            elif(int(userinput) == 2):
                loggedUserName = login.login()
                if( loggedUserName != None ):
                    isloggedIn = True
                    break
                else:
                    isloggedIn = False
                    continue
        elif( len(userinput) != 0 and userinput.isdigit() and int(userinput) == 3 ):
            print("Bye Bye")
            break
        else:
            print("invalid operation #")
    
    while isloggedIn:
        print("     1- create project    || 2- view all projects    || 3- view my projects")
        print("     4- edit my project   || 5- delete my project    || 6- exit")
        userinput = input("please choose the operation you want to make: ")
        if( len(userinput) != 0 and userinput.isdigit() and int(userinput) > 0 and int(userinput) < 6 ):
            if(int(userinput) == 1):
                createProject.createProject(loggedUserName)
                continue
            elif(int(userinput) == 2):
                viewProjects.viewAllProjects()
                continue
            elif(int(userinput) == 3):
                viewProjects.viewLoggedInUserProjects(loggedUserName)
                continue
            elif(int(userinput) == 4):
                editProject.editProject(loggedUserName)
                continue
            elif(int(userinput) == 5):
                deleteProject.deleteProject(loggedUserName)
        elif( len(userinput) != 0 and userinput.isdigit() and int(userinput) == 6 ):
            print("Bye Bye")
            break
        else:
            print("invalid operation #")
            
        
main()