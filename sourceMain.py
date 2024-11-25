from Manager.EmployeeManager import EmployeeManager
from Employee import Employee

empManager = EmployeeManager()


def addEmployeeChoice():
    print("Enter information about this employee")
    try:
        id = -1
        while (id == -1):
            print("Note: The ID must be any number except -1")
            id = int(input(" => Id: "))
    except:
        print("Sorry, Id must be number :( ")
        return

    name = input(" => Name: ")
    if name.isnumeric():
        print("Sorry, Name must be String :( ")
        return

    position = input(" => Position: ")
    if position.isnumeric():
        print("Sorry, Position must be String :( ")
        return

    try:
        salary = float(input(" => Salary: "))
    except:
        print("Sorry, Salary must be number :(")
        return

    email = input(" => Email: ")  

    emp = Employee(id, name, position, salary, email)
    if empManager.addEmployee(emp) == False:
        return



def updateEmployeeChoice():
    try:
        id = int(input("Enter an ID to update this employee or Exit (-1): "))
        id = str(id)
        while((id != "-1") & (int(id) not in empManager.getIdEmployees())):
            print("There is no employee with ID = " + id)
            id = input(" => Enter valid id or Exit (-1) : ")
        
    except:
        print("Sorry, Id must be number :(")
        return

    if id == "-1":
        return
    

    choiceUpdate = 0
    while(choiceUpdate != -1):
        try:
            print("\nEnter the choice you want to modify")
            choiceUpdate = int(input(" name (1),\t position (2),\t salary (3),\t email (4),\t exit (-1) \n => "))
        except:
            print("please enter number from list")
            
        if choiceUpdate == 1:
            name = input(" => New name: ")
            if name.isnumeric():
                print("Name must be String")
                break
            else:
                empManager.updateName(id, name)

        elif choiceUpdate == 2:
            position = input(" => New position: ")
            if position.isnumeric():
                print("Position must be String")
                break
            else:
                empManager.updatePosition(id, position)

        elif choiceUpdate == 3:
            try:
                salary = float(input(" => New salary: "))
                salary = str(salary)
                empManager.updateSalary(id, salary)
            except:
                print("Salary must be number")
                break
            
        elif choiceUpdate == 4:
            email = input(" => New email: ")
            if email.isnumeric():
                print("Email must be String")
                break
            if empManager.updateEmail(id, email) == False:
                print("Email is invalid")
                break    



def deleteEmployeeChoice():
    try:
        id = int(input(" => Enter an ID to delete this employee or Exit (-1) : "))
        id = str(id)
        while((id != "-1") & (empManager.deleteEmployee(id) == False)):
            id = input(" => Enter valid id or Exit (-1) : ")
    except:
        print("Id must be number")
        return



def searchEmployeeChoice():
    try:
        id = int(input(" => Enter an ID to search about this employee or Exit (-1) : "))
        id = str(id)
        while((id != "-1") & (empManager.searchEmployee(id) == False)):
            id = input(" => Enter valid id or Exit (-1) : ")
        
    except:
        print("Id must be number")
        return



def viewAllEmployeeChoice():
    empManager.viewAllEmployees()



# Specify the shape of the separator between the choices.
def separator(shape = '-', repeat = 20):
    print("\n\t")
    for i in range(repeat):
        print(shape, end=" ")
    print("\n")


