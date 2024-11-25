class Employee:
    def __init__(self,id, name, position, salary, email):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary
        self.email = email

    # Setter And Getter Id
    def setId(self, id):
        self.id = id
    
    def getId(self):
        return self.id

    # Setter And Getter Name
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name

    # Setter And Getter Position
    def setPosition(self, position):
        self.position = position
    
    def getPosition(self):
        return self.position

    # Setter And Getter Salary
    def setSalary(self, salary):
        self.salary = salary
    
    def getSalary(self):
        return self.salary

    # Setter And Getter Email
    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email