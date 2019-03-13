'''
Created on Jan 22, 2018

@author: PATI
'''

class ServiceF():
    '''
    Clasa de service pentru fisier
    '''


    def __init__(self, repo):
        '''
        initializam campul repo cu repo corespunzator
        '''
        self.__repo=repo
        
    """
    Functia returneaza toate elementele din fisier
    """
    def getAll(self):
        return self.__repo.getAll()