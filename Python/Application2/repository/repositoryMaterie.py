'''
Created on Nov 12, 2017

@author: PATI
'''

class RepositoryExceptionD(Exception):
    """
    Clasa de erori pentru lista de discipline
    """
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

class inMemoryRepositoryD:
    """
    Clasa lista de discipline
    Contine o lista de discipline, fiecare disciplina are un Id, un nume si un profesor
    """
    
    """
    Initializeaza lista de discipline cu lista vida
    """
    def __init__(self):
        self.__elems=[]
    
    """
    Adauga la lista de discipline o noua disciplina
    Date de intrare: elem- noua disciplina
    """
    def add(self,elem):
        if elem in self.__elems:       #daca gaseste in lista o disciplina egala (functia __eq__ declara doua elemente egale daca au acelasi Id) cu cea pe care vrem sa o introducem, afiseaza mesajul "exista deja"
            raise RepositoryExceptionD("O disciplina cu acest Id exista deja!")
        self.__elems.append(elem)
        
    """
    Sterge din lista de discipline o disciplina cu un anumit Id
    Date intrare: elem-Disciplina cu Id-ul care trebuie sa fie eliminat
    """
    def rem(self,elem):
        if elem not in self.__elems:    #daca nu gaseste in lista o disciplina egala (functia __eq__ declara doua elemente egale daca au acelasi Id) cu cea pe care vrem sa o stergem, afiseaza mesajul "disciplina inexistent"
            raise RepositoryExceptionD("Disciplina inexistenta!") 
        self.__elems.remove(elem)       #elimina prima instanta din lista de discipline care este "egala" cu instanta elem care are id-ul instantei ce trebuie sa fie eliminata
        
    """
    Modifica numele unei discipline cu un anumit Id
    Date intrare: elem- Noua valoare a disciplinei ce trebuie modificata
    """
    def upd(self,elem):
        if elem not in self.__elems:
            raise RepositoryExceptionD("Disciplina inexistenta!")
        ind = self.__elems.index(elem)  #ind primeste prima pozitie unde apare Disciplina elem in lista de discipline
        self.__elems[ind]=elem          #elementul din lista de discipline de pe pozitia ind primeste o noua valoare (un nou nume si un nou profesor) adica pe elem
        
    
    """
    Returneaza Disciplina cu Id-ul disciplinei elem din lista de discipline
    Date intrare: elem- disciplina care are Id-ul disciplinei ce trebuie sa fie returnata
    """
    def getId(self,elem):
        if elem not in self.__elems:
            raise RepositoryExceptionD("Disciplina inexistenta!")

        ind = self.__elems.index(elem)  #ind primeste prima pozitie pe care apare elem
        return self.__elems[ind]        #returnam Disciplina elem
    
    """
    Returneaza Disciplinele cu Numele disciplinei elem din lista de discipline
    Date intrare: elem- disciplina care are Numele disciplinelor ce trebuie sa fie returnate
    """    
    def getNume(self,elem):
        lis=inMemoryRepositoryD()
        for el in self.__elems:
            if el.egalNume(elem):
                ind=self.__elems.index(el)
                lis.__elems.append(self.__elems[ind])
        if lis.size()!=0:
            return lis.getAll()
        else:
            raise RepositoryExceptionD("Disciplina inexistenta!")
    
    """
    Returneaza Disciplinele cu Profesorul disciplinei elem din lista de discipline
    Date intrare: elem- disciplina care are Profesorul disciplinelor ce trebuie sa fie returnate
    """  
    def getProfesor(self,elem):
        lis=inMemoryRepositoryD()
        for el in self.__elems:
            if el.egalProfesor(elem):
                ind=self.__elems.index(el)
                lis.__elems.append(self.__elems[ind])
        if lis.size()!=0:
            return lis.getAll()
        else:
            raise RepositoryExceptionD("Disciplina inexistenta!")
            
    """
    Returneaza lungimea listei de discipline
    """
    def size(self):
        return len(self.__elems)

    """
    Returneaza toata lista de discipline
    """
    def getAll(self):
        return self.__elems[:]