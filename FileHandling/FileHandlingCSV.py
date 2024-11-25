
import csv  # To send the list to the file via csv.writer & writerow method
# from FileHandling import FileHandlingImp

class FileHandlingCSV():
    fileName = "" 
    file = ""
    extension = ".csv"
    
    def __init__(self, fileName, header):
        FileHandlingCSV.fileName = fileName
        # To create a file and insert the header into the first row (at index in data = 0)
        try:
            with open(self.fileName + self.extension, mode="w", newline="") as self.file:
                writer = csv.writer(self.file)
                writer.writerow(header)
        except IOError:
            print("Unable to create " + self.fileName + " file")
        
    
    def __deleteAllData(self): # private method to delete all data
        with open(self.fileName + self.extension, mode="w") as file:
            file.seek(0)
            file.truncate()


    def add(self, data):    # To add data as a list to the file (Starting at index in data = 1)
        try:
            with open(self.fileName + self.extension, mode="a", newline="") as self.file:
                writer = csv.writer(self.file)
                writer.writerow(data)
        except IOError:
            print("Unable to add data to "+ self.fileName + " file")


    def __addLine(self, line): # to convert an employee (string) into list and remove double quotation, then add it to data in file
        line = line.split()
        line[0] = line[0].strip("\"")
        self.add(line)

    
    def get(self):  #  Returns all data as a list and details of each employee in an index in this list
        try:
            with open(self.fileName + self.extension, mode="r") as self.file:
                return self.file.readlines()
        except IOError:
            print("Cannot read data in " + self.fileName + " file")
        

    def update(self, id, new, choice): # Take choice (name, position, salary or email) and change it with new after searching it with ID
        data = self.get()
        updatedDate = self.search(id)
        try:  
            old = updatedDate.split(",")[choice] # To determine where I will change it
        except:
            return "ID not found"
        
        updatedDate = updatedDate.replace(old, new)
        updatedDate = updatedDate.split() # Convert string to a list because (add method) must take list
        self.__deleteAllData()
        
        for line in data:
            endIndexId = line.find(",")
            if line[:endIndexId].strip("\"") == id:
                self.add(updatedDate)
            else:
                self.__addLine(line)
        return updatedDate


    def delete(self, id): # To delete data using the id
        data = self.get()
        self.__deleteAllData()
        flag = False    # To check if the ID is exited or not
        for line in data:
            endIndexId = line.find(",")
            if line[:endIndexId].strip("\"") != id:
                self.__addLine(line)
            else:
                flag = True
        return flag


    def search(self, id):   
        data = self.get() 
        for line in data:
            endIndexId = line.find(",")  # To find the index of the first comma to locate the id
            if id == line[:endIndexId].strip("\""):
                return line.split()[0].strip("\"")
            
        