'''
Created on Nov 18, 2017

@author: PATI
'''

class RepositoryExceptionN(Exception):
    """
    Clasa de erori pentru lista de note
    """
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

class inMemoryRepositoryN:
    """
    Clasa lista de note
    Contine o lista de obiecte de tip nota
    """
    
    """
    Initializeaza lista de note cu lista vida
    """
    def __init__(self):
        self.__elems=[]
    
    """
    Adauga la lista de note o noua nota daca studentul curent mai are cel putin o nota la materia curenta si creeaza o noua instanta nota in caz contar
    Date de intrare: elem- noua nota asociata unui student si unei discipline
    """
    def add(self,elem):
        for el in self.__elems:
            if elem.eqSD(el):
                el.addNota(elem.getNote())
                return 
        self.__elems.append(elem)
        
        
    """
    Sterge din lista de note notele asociate unui anumit student
    Date intrare: elem-Studentul
    """
    def remS(self,elem):
        for el in self.__elems:    
            if elem.eqS(el):
                self.__elems.remove(el)       
    
    """
    Sterge din lista de note notele asociate unui anumit student
    Date intrare: elem-Studentul
    """
    def remD(self,elem):
        for el in self.__elems:    
            if elem.eqD(el):
                self.__elems.remove(el)       
       
    """
    Returneaza lista de obiecte Nota care au id-ul disciplinei egal cu id-ul disciplinei Notei elem
    Date intrare: elem- nota care are id-ul de disciplina in functie de care etragem elemente din lista de note
    """
    def getIddis(self,elem):
        lis=inMemoryRepositoryN()
        
        for el in self.__elems:
            if el.eqD(elem):                                 
                ind=self.__elems.index(el)
                lis.__elems.append(self.__elems[ind])
        if lis.size()!=0:
            return lis.getAll()
        else:
            raise RepositoryExceptionN("Nota inexistenta!")  
        
    """
    Returneaza lungimea listei de note
    """
    def size(self):
        return len(self.__elems)

    """
    Returneaza toata lista de note
    """
    def getAll(self):
        return self.__elems[:]