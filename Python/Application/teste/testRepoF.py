'''
Created on Jan 22, 2018

@author: PATI
'''
from repo.repoF import RepoF

class TestRepoF():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.__repo=RepoF("testeRepoF.txt")
        
    def testGetAll(self):
        assert len(self.__repo.getAll())==2
        
    def run(self):
        self.testGetAll()