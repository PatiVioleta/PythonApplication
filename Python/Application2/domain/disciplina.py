'''
Created on Nov 12, 2017

@author: PATI
'''
class Disciplina:
    """
    Clasa disciplina
    Un obiect de tiplul Disciplina contine un Id, un nume disciplina si un nume profesor
    """
    """
    Initializeaza Id-ul, numele disciplinei si numele profesorului
    Date intrare: iddis- Id-ul disciplinei, nume- numele disciplinei, profesor- numele profesorului 
    """
    def __init__(self,iddis,nume,profesor):
        self.__iddis = iddis
        self.__nume = nume
        self.__profesor=profesor

    """
    Returneaza numele disciplinei
    """
    def getNume(self):
        return self.__nume

    """
    Returneaza Id-ul disciplinei
    """
    def getIddis(self):
        return self.__iddis
    
    """
    Returneaza numele profesorului
    """
    def getProfesor(self):
        return self.__profesor
 
    """
    Seteaza un nou nume pt disciplina
    """
    def setNume(self,nume):
        self.__nume = nume
        
    """
    Seteaza un nou nume pt profesor
    """
    def setProfesor(self,profesor):
        self.__profesor=profesor

    """
    Defineste relatia de egalitate intre doua instante ca fiind egalitatea dintre id-urile acestora
    """
    def __eq__(self, other):
        if isinstance(other,self.__class__):           #daca self si other au acelasi tip returnam valoarea de adevar a egalitatii dintre id-urile celor doua instante
            return self.__iddis==other.__iddis
        else:
            return False
        
    """
    Defineste relatia de egalitate intre doua instante ca fiind egalitatea dintre numele de discipline atasate acestora
    """
    def egalNume(self,other):
        if isinstance(other,self.__class__):
            return self.__nume==other.__nume
        else:
            
            return False
        
    """
    Defineste relatia de egalitate intre doua instante ca fiind egalitatea dintre numele de profesori atasate acestora
    """
    def egalProfesor(self,other):
        if isinstance(other,self.__class__):
            return self.__profesor==other.__profesor
        else:
            return False
    
    """
    Returneaza instanta disciplina sub forma "<Id> <nume> <profesor>"
    """
    def __str__(self):
        return str(self.__iddis)+" "+self.__nume+" "+str(self.__profesor)