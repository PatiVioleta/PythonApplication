'''
Created on Jan 22, 2018

@author: PATI
'''

class ServiceJ():
    '''
    Clasa service pentru jucatori
    '''


    def __init__(self, repo):
        '''
        Initializam campul repo cu repo corespunzator pt jucatori
        '''
        self.__repo=repo
        
    """
    Adauga un jucator in fisier
    Date intrare: ju-jucator
    """
    def add(self,ju):
        return self.__repo.add(ju)
    
    """
    Adauga un jucator in fisier fara a arunca exceptii
    Date intrare: ju-jucator
    """
    def add2(self,ju):
        return self.__repo.add2(ju)
    
    """
    Modifica ianltimea unui jucator din fisier
    Date intrare: nume-nume jucator, prenume-prenume jucator,inaltime-inaltimea
    """
    def mod(self,nume,prenume,inaltime):
        return self.__repo.mod(nume,prenume,inaltime)
    
    """
    Formeaza o echipa de jucatori
    Date iesire: lista de jucatori dintr-o echipa
    """
    def echipa(self):
        return self.__repo.echipa()
    
    """
    Returneaza toata lista de elemente
    """
    def getAll(self):
        return self.__repo.getAll()