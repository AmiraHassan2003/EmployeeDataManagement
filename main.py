
import sourceMain 



choice = 0

while(choice != -1):
    try:
        sourceMain.separator('*', 20)
        print("Enter the number that represents the service")
        choice = int(input(" To add an employee (1),\n To update an employee (2),\n To delete an employee (3),\n To search for an employee (4),\n To view all employees (5),\n Exit (-1)\n => "))
        if choice == -1:
            break
    except:
        print("\n\nPlease enter number from menu")
        choice = int(input(" To add an employee (1),\n To update an employee (2),\n To delete an employee (3),\n To search for an employee (4),\n To view all employees (5),\n Exit (-1)\n => "))


    

    if choice == 1: # To add an employee
        sourceMain.separator()
        sourceMain.addEmployeeChoice()
    

    elif choice == 2: # To update an employee
        sourceMain.separator()
        sourceMain.updateEmployeeChoice()
        

    elif choice == 3: # To delete an employee
        sourceMain.separator()
        sourceMain.deleteEmployeeChoice()
        
    
    elif choice == 4: # To search for an employee
        sourceMain.separator()
        sourceMain.searchEmployeeChoice()
        

    elif choice == 5:  # To view all employees
        sourceMain.separator()
        sourceMain.viewAllEmployeeChoice()

    else:
        pass
        

print("\n Thank You :)")