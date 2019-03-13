'''
Created on Dec 7, 2017

@author: PATI
'''
from repository.repositoryMaterie import inMemoryRepositoryD
from domain.disciplina import Disciplina

class RepositoryExceptionD2(Exception):
    """
    Clasa de erori pentru lista de discipline
    """
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class disciplinaFileRepository(inMemoryRepositoryD):
    '''
    Clasa lista de discipline gestionata din fisiere
    Contine o lista de discipline, fiecare disciplina are un Id, un nume si un profesor
    '''

    def __init__(self):
        '''
        Initializam clasa mostenita
        '''
        inMemoryRepositoryD.__init__(self)

    """
    Extragem informatiile din fisier
    """
    def __loadFromFile(self):
        try:
            f=open("disciplina.txt","r")
        except IOError:
            rez=[]
        
        line=f.readline().strip()
        rez=[]
        while line!="":
            inf=line.split(";")
            el= Disciplina(int(inf[0]),inf[1],inf[2])
            rez.append(el)
            line=f.readline().strip()
        f.close()
        
        return rez
    
    """
    Punem informatiile din listaD in fisier
    Date intrare: listaD-lista de discipline
    """
    def __storeToFile(self,listaD):
        f=open("disciplina.txt","w")
        for i in listaD:
            el=str(i.getIddis())+";"+i.getNume()+";"+i.getProfesor()+"\n"
            f.write(el)
        f.close()
    
    """
    Adauga la lista de discipline o noua disciplina
    Date de intrare: el- noua disciplina
    """
    def add(self,el):
        inMemoryRepositoryD.add(self,el)
        
        self.__elems=self.__loadFromFile()
        
        if el in self.__elems:
            raise RepositoryExceptionD2("O disciplina cu acest Id exista deja!!!")
        
        self.__elems.append(el)
        self.__storeToFile(self.__elems)
        
        
    """
    Sterge din lista de discipline o disciplina cu un anumit Id
    Date intrare: el-Disciplina cu Id-ul care trebuie sa fie eliminat
    """
    def rem(self,el):
        #inMemoryRepositoryD.rem(self,el)
        
        self.__elems=self.__loadFromFile()
        
        if el not in self.__elems:    #daca nu gaseste in lista o disciplina egala (functia __eq__ declara doua elemente egale daca au acelasi Id) cu cea pe care vrem sa o stergem, afiseaza mesajul "disciplina inexistent"
            raise RepositoryExceptionD2("Disciplina inexistenta!") 
        
        self.__elems.remove(el)       #elimina prima instanta din lista de discipline care este "egala" cu instanta elem care are id-ul instantei ce trebuie sa fie eliminata
        self.__storeToFile(self.__elems)
        
    """
    Modifica numele unei discipline cu un anumit Id
    Date intrare: el- Noua valoare a disciplinei ce trebuie modificata
    """
    def upd(self,el):
        #inMemoryRepositoryD.upd(self,el)
        
        self.__elems=self.__loadFromFile()
        if el not in self.__elems:
            raise RepositoryExceptionD2("Disciplina inexistenta!")
        ind = self.__elems.index(el)  #ind primeste prima pozitie unde apare Disciplina elem in lista de discipline
        self.__elems[ind]=el          #elementul din lista de discipline de pe pozitia ind primeste o noua valoare (un nou nume si un nou profesor) adica pe elem
        self.__storeToFile(self.__elems)
        
    """
    Returneaza Disciplina cu Id-ul disciplinei elem din lista de discipline
    Date intrare: el- disciplina care are Id-ul disciplinei ce trebuie sa fie returnata
    """
    def getId(self,el):
        #inMemoryRepositoryD.getId(self,el)
        
        self.__elems=self.__loadFromFile()
        if el not in self.__elems:
            raise RepositoryExceptionD2("Disciplina inexistenta!")
        ind = self.__elems.index(el)  #ind primeste prima pozitie pe care apare elem
        return self.__elems[ind]        #returnam Disciplina elem
        self.__storeToFile(self.__elems)
        
    """
    Returneaza Disciplinele cu Numele disciplinei elem din lista de discipline
    Date intrare: elem- disciplina care are Numele disciplinelor ce trebuie sa fie returnate
    """    
    def getNume(self,elem):
        #inMemoryRepositoryD.getNume(self,elem)
        
        self.__elems=self.__loadFromFile()
        lis=[]
        for el in self.__elems:
            if el.egalNume(elem):
                ind=self.__elems.index(el)
                lis.append(self.__elems[ind])
        if len(lis)!=0:
            return lis[:]
        else:
            raise RepositoryExceptionD2("Disciplina inexistenta!")
        self.__storeToFile(self.__elems)
        
    """
    Returneaza Disciplinele cu Profesorul disciplinei elem din lista de discipline
    Date intrare: elem- disciplina care are Profesorul disciplinelor ce trebuie sa fie returnate
    """
    def getProfesor(self,elem):
        #inMemoryRepositoryD.getProfesor(self,elem)
        
        self.__elems=self.__loadFromFile()
        lis=[]
        for el in self.__elems:
            if el.egalProfesor(elem):
                ind=self.__elems.index(el)
                lis.append(self.__elems[ind])
        if len(lis)!=0:
            return lis[:]
        else:
            raise RepositoryExceptionD2("Disciplina inexistenta!")
        self.__storeToFile(self.__elems)
        
    """
    Returneaza lungimea listei de discipline
    """
    def size(self):
        inMemoryRepositoryD.size(self)
        self.__elems=self.__loadFromFile()
        return len(self.__elems)
        
    """
    Returneaza toata lista de discipline
    """
    def getAll(self):
        inMemoryRepositoryD.getAll(self)
        self.__elems=self.__loadFromFile()
        return self.__elems[:]