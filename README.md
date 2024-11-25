Employee Data Management

    This project is for the manager to manage the employee operations in any department.
    
    Manager
        Adding a new employee.
        Viewing all employees.
        Updating an employee's details.
        Deleting an employee.
        Searching for an employee by their unique ID.
        Saving and retrieving employee data using a CSV file.

    
    Display
      Enter the number that represents the service
      To add an employee (1), To update an employee (2), To delete an employee (3), To search for an employee (4), To view all employees (5), Exit (-1)
      - If the manager enters any option that is not in the list, the message "Please enter the number from the list" will appear and the list will be displayed again until entering -1 to exit, then the message "Thank you"    


    
    (1) Add Employee
    
       - Enter information about this employee
       - Note: The ID must be any number except -1; this message will appear if the user enters -1 until they enter a valid ID.
       -   - if the manager enters an ID as a string, the message "Sorry, the ID must be a number :( " will appear.
           - If the manager enters an ID that already exists, the message "This ID already exists" will appear, and it will not be stored in the employee data file.
       - If the manager enters the name as a number, a message will appear "Sorry, the name must be a string :(".
       - If the manager enters the position as a number, a message will appear "Sorry, the position must be a string :(".
       - If the manager enters the salary as a string, a message will appear "Sorry, the salary must be a number :(".
       - If the manager enters the email without gmail.com at the end, the message "Invalid email" will appear.


       
    (2) Update Employee
    
       - Enter an ID to update this employee or Exit (-1) to show the menu again
       - If the user enters an incorrect ID, this message will appear "No employee with ID = ID", until entering -1 to exit.
       - If the user enters valid id
           - Enter the choice you want to modify
           - name (1), position (2), salary (3), email (4), exit (-1)
           - User can select any option to modify data even enter -1 to exit.



    (3) Delete Employee
        - Enter an ID to delete this employee or exit (-1) to show the menu again.
        - If the user enters an incorrect ID, this message will appear "No employee with ID = ID", until entering -1 to exit.
        - If the user enters a valid ID, this message will appear "Employee with ID = 1 has been deleted successfully".



    (4) Search for an employee
    
       - Enter an ID to search about this employee or Exit (-1) to show the menu again
       - If the user enters an incorrect ID, this message will appear "No employee with ID = ID", until entering -1 to exit.
       - If the user enters a valid ID, the employee's ID, name, position, salary and email will be displayed.



    (5) View all employees
    
       - If there is no data, this message will appear "Employees not found", otherwise, there will be data for all employees.

