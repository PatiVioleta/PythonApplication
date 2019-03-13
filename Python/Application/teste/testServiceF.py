'''
Created on Jan 22, 2018

@author: PATI
'''
from service.serviceF import ServiceF
from repo.repoF import RepoF

class TestServiceF():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.__serv=ServiceF(RepoF("testeRepoF.txt"))
        
    def testGetAll(self):
        assert len(self.__serv.getAll())==2
        
    def run(self):
        self.testGetAll()