'''
Created on Nov 18, 2017

@author: PATI
'''
class Nota:
    """
    Clasa nota
    Un obiect de tipul Nota contine Id student, Id disciplina si o liste de note
    """
    """
    Initializeaza Id-ul studentului, Id-ul disciplinei si lista de note
    Date intrare: iddis- Id-ul disciplinei, idstud- Id-ul studentului, note-lista de note
    """
    def __init__(self,idstud,iddis,note):
        self.__idstud = idstud
        self.__iddis = iddis
        self.__note=[]
        self.__note.append(note)
        
    """
    Adauga o nota la lista deja existenta de note a studentului la materia curenta
    Date intrare: nota- nota care trebuie sa fie adaugata
    """    
    def addNota(self,nota):
        self.__note=self.__note+nota

    """
    Returneaza Id-ul studentului
    """
    def getIdstud(self):
        return self.__idstud

    """
    Returneaza Id-ul disciplinei
    """
    def getIddis(self):
        return self.__iddis
    
    """
    Returneaza lista de note
    """
    def getNote(self):
        return self.__note
    
    """
    Defineste relatia de egalitate intre doua instante ca fiind egalitatea dintre id-urile studentilor din acestea
    """
    def eqS(self, other):
        if isinstance(other,self.__class__):       
            return self.__idstud==other.__idstud
        else:
            return False
    
    """
    Defineste relatia de egalitate intre doua instante ca fiind egalitatea dintre id-urile disciplinelor din acestea
    """
    def eqD(self, other):
        if isinstance(other,self.__class__):
            return int(self.__iddis)==int(other.__iddis)
        else:
            return False
    
    """
    Defineste relatia de egalitate intre doua instante ca fiind egalitatea dintre id-urile disciplinelor si id-urile studentilor din acestea
    """
    def eqSD(self, other):
        if isinstance(other,self.__class__):       
            return self.__iddis==other.__iddis and self.__idstud==other.__idstud
        else:
            return False
    
    """
    Returneaza instanta nota sub forma "<IdStudent> la disciplina <IdDisciplina> are nota/notele: <note>"
    """
    def __str__(self):
        return "Studentul cu Id= "+str(self.__idstud)+" la disciplina cu Id= "+str(self.__iddis)+" are nota/notele: "+str(self.__note)