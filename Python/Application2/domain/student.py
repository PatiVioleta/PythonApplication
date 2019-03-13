
class Student:
    """
    Clasa student
    Un obiect de tiplul Student contine un Id si un nume 
    """
    """
    Initializeaza Id-ul si numele studentului
    Date intrare: idstud- Id-ul studentului, nume- numele studentului 
    """
    def __init__(self,idstud,nume):
        self.__idstud = idstud
        self.__nume = nume
    
    """
    Returneaza numele studentului 
    """
    def getNume(self):
        return self.__nume
    
    """
    Returneaza Id-il studentului
    """
    def getIdstud(self):
        return self.__idstud

    """
    Seteaza un nou nume pentru student
    """
    def setNume(self,nume):
        self.__nume = nume

    """
    Defineste relatia de egalitate intre doua instante ca fiind egalitatea dintre id-urile acestora
    """
    def __eq__(self, other):
        if isinstance(other,self.__class__):       #daca self si other au acelasi tip returnam valoarea de adevar a egalitatii dintre id-urile celor doua instante
            return self.__idstud==other.__idstud
        else:
            return False
    
    """
    Defineste relatia de egalitate intre doua instante ca fiind egalitatea dintre numele acestora
    """
    def egalNume(self,other):
        if isinstance(other,self.__class__):
            return self.__nume==other.__nume
        else:
            return False

    """
    Returneaza instanta student sub forma "<Id> <nume>"
    """
    def __str__(self):
        return str(self.__idstud)+" "+self.__nume