
from abc import ABCMeta, abstractmethod

class EmployeeManagerImp(metaclass=ABCMeta):

    # Add an employee with a unique ID and valid email.
    @abstractmethod
    def addEmployee(self, emp):  
        pass

    # If there are employees in the dataEmployee file, this method will appear them.
    @abstractmethod
    def viewAllEmployees(self): # 
        pass

    # If the employee exists, the name, position, salary and email will be updated as desired.
    @abstractmethod
    def updateName(self, id, name): 
        pass       

    @abstractmethod
    def updatePosition(self, id, position):  
        pass  

    @abstractmethod
    def updateSalary(self, id, salary):
        pass

    @abstractmethod
    def updateEmail(self, id, email):
        pass

    @abstractmethod
    def deleteEmployee(self, id):
        pass

    @abstractmethod
    def searchEmployee(self, id):
        pass

    