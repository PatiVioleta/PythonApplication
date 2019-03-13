'''
Created on Jan 22, 2018

@author: PATI
'''
from domain.jucator import Jucator

class TestJ():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.__ju=Jucator("ana","ala",120,"Fundas")
    
    def testGetNume(self):
        assert self.__ju.get_nume()=="ana"
        
    def testGetPrenume(self):
        assert self.__ju.get_prenume()=="ala" 
        
    def testGetInaltime(self):
        assert self.__ju.get_inaltime()==120
        
    def testGetPost(self):
        assert self.__ju.get_post()=="Fundas"
        
    def testSetInaltime(self):
        self.__ju.set_inaltime(10)
        assert self.__ju.get_inaltime()==10
        
    def run(self):
        self.testGetNume()
        self.testGetPrenume()
        self.testGetInaltime()
        self.testGetPost()
        self.testSetInaltime()
    
    
    