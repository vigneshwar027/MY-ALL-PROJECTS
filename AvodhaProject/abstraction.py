#example for class abstractions
from abc import *

class Ideas(ABC):
     @abstractmethod
     def createideas(self):
         pass

     def idea_suggestions(self):
         pass

class Students(Ideas):
    def createideas(self):
        print('add scholships to the students')

class Farmers(Ideas):
    def createideas(self):
        print('give waivers')

class Doctors(Ideas):

    def createideas(self):
        print('increase salary')

Prof = input('Enter your profession:')
class_name = globals()[Prof]
candidate = class_name() #dont forget to add brackets even when using globals
candidate.createideas()