
from abc import ABCMeta, abstractmethod

class FileHandlingCSVImp(metaclass=ABCMeta):
    @abstractmethod
    def add(self, data):    # To add data as a list to the file (Starting at index in data = 1)
        pass
    
    @abstractmethod
    def get(self):  #  Returns all data as a list and details of each employee in an index in this list
        pass

    @abstractmethod
    def update(self, id, new, choice): # Take choice (name, position, salary or email) and change it with new after searching it with ID
        pass

    @abstractmethod
    def delete(self, id): # To delete data using the id
        pass

    @abstractmethod 
    def search(self, id):  # To search for data using an identifier
        pass
            
        