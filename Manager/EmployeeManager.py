
import re   # To check whether the email is valid or not
from Employee import Employee
from FileHandling.FileHandlingCSV import FileHandlingCSV
from Manager.EmployeeManagerImp import EmployeeManagerImp

class EmployeeManager(EmployeeManagerImp, FileHandlingCSV, Employee):
    idEmployees = []    # To check whether the ID already exists or not, so it includes a unique ID

    def __init__(self):
        # create file csv called dataEmployee with header => ["id","name","position","salary","email"]
        fileCsv = FileHandlingCSV('dataEmployee', ["id","name","position","salary","email"])
        

    def __checkEmail(self, email): # check if email is valid or not 
        validEmail = re.match(r'^[a-zA-Z0-9]+@gmail.com', email)
        if validEmail:
            return True
        else:
            return False
        

    def addEmployee(self, emp):
        if emp.getId() not in self.idEmployees: # Check the ID if it already exists or not
            self.idEmployees.append(emp.getId())
        else:
            print("This ID already exists\n")
            return False
        
        if self.__checkEmail(emp.getEmail()) == True:
            employee = []
            employee.append(emp.getId())
            employee.append(emp.getName())
            employee.append(emp.getPosition())
            employee.append(emp.getSalary())
            employee.append(emp.getEmail())
            self.add(employee)
            print("The employee has been added successfully\n")
            return True
        
        else:
            print("Email is invalid")
            return False

    def getIdEmployees(self): 
        return self.idEmployees

    def viewAllEmployees(self):
        numberOfEmployees = len(self.get())
        if numberOfEmployees != 1:
            for i in range(1,numberOfEmployees):
                emp = self.get()[i].strip("\"").split(",")
                self.searchEmployee(emp[0])     #emp[0] => id
                print("-----------")
        else:
            print("Not Found Employees\n")
        

    def updateName(self, id, name):
        return self.update(id, name, 1)
        

    def updatePosition(self, id, position):
        return self.update(id, position, 2)
    
        
    def updateSalary(self, id, salary):
        return self.update(id, salary, 3)
        

    def updateEmail(self, id, email):
        if self.__checkEmail(email) == True:
            return self.update(id, email, 4)
        else:
            return False
        

    def deleteEmployee(self, id):
        if self.delete(id) == False:
            if id != "-1":
                print("There is no employee with ID = " + id)
                return False
            else:
                return False
        else:
            print("Employee with ID = " + id + " was successfully deleted")
            return True


    def searchEmployee(self, id):
        if self.search(id) is None:
            if id != "-1":
                print("There is no employee with ID = " + id)
                return False
            else:
                return False
        else:
            employee = self.search(id).split(",")
            print("Id : " + employee[0])
            print("Name : " + employee[1])
            print("Position : " + employee[2])
            print("Salary : " + employee[3])
            print("Email : " + employee[4])
        return True


    