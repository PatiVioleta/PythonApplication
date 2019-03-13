'''
Created on Dec 7, 2017

@author: PATI
'''
from repository.repositoryStudent import inMemoryRepository
from domain.student import Student

class RepositoryException2(Exception):
    """
    Clasa de erori pentru lista de discipline
    """
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class studentFileRepository(inMemoryRepository):
    """
    Clasa lista de studenti gestionata din fisier
    Contine o lista de studenti, fiecare student are un Id si un nume
    """

    def __init__(self):
        '''
        Initializam clasa mostenita
        '''
        inMemoryRepository.__init__(self)

    """
    Extragem informatiile din fisier
    """
    def __loadFromFile(self):
        try:
            f=open("student.txt","r")
        except IOError:
            rez=[]
        
        line=f.readline().strip()
        rez=[]
        while line!="":
            inf=line.split(";")
            el= Student(int(inf[0]),inf[1])
            rez.append(el)
            line=f.readline().strip()
        f.close()
        
        return rez
    
    """
    Punem informatiile din listaD in fisier
    Date intrare: listaD-lista de discipline
    """
    def __storeToFile(self,listaS):
        f=open("student.txt","w")
        for i in listaS:
            el=str(i.getIdstud())+";"+i.getNume()+"\n"
            f.write(el)
        f.close()
    
    """ 
    Adauga la lista de studenti un nou student
    Date de intrare: elem- noul student
    """
    def add(self,el):
        inMemoryRepository.add(self,el)
        
        self.__elems=self.__loadFromFile()
        id=int(el.getIdstud())
        #print (type(id))
        if el in self.__elems:       #daca gaseste in lista un student egal (functia __eq__ declara doua elemente egale daca au acelasi Id) cu cel pe care vrem sa il introducem, afiseaza mesajul "exista deja"
            raise RepositoryException2("Un student cu acest Id exista deja!")
        
        self.__elems.append(el)
        self.__storeToFile(self.__elems)
        
        
    """
    Sterge din lista de studenti un student cu un anumit Id
    Date intrare: elem-Studentul cu Id-ul care trebuie sa fie eliminat
    """
    def rem(self,elem):
        #inMemoryRepository.rem(self,elem)
        
        self.__elems=self.__loadFromFile()
        
        if elem not in self.__elems:    #daca nu gaseste in lista un student egal (functia __eq__ declara doua elemente egale daca au acelasi Id) cu cel pe care vrem sa il stergem, afiseaza mesajul "student inexistent"
            raise RepositoryException2("S-a incercat stergerea unui student inexistent!")
        self.__elems.remove(elem)       #elimina prima instanta din lista de studenti care este "egala" cu instanta elem care are id-ul instantei ce trebuie sa fie eliminata
    
        self.__storeToFile(self.__elems)
        
    """
    Modifica numele unui student cu un anumit Id
    Date intrare: elem- Noua valoare a studentului ce trebuie modificat
    """
    def upd(self,elem):
        #inMemoryRepository.upd(self,elem)
        
        self.__elems=self.__loadFromFile()
        
        if elem not in self.__elems:
            raise RepositoryException2("S-a incercat accesarea unui student inexistent!")
        ind = self.__elems.index(elem)  #ind primeste prima pozitie unde apare Studentul elem in lista de studenti
        self.__elems[ind]=elem          #elementul din lista de studenti de pe pozitia ind primeste o noua valoare (un nou nume) adica pe elem
    
        self.__storeToFile(self.__elems)
        
    """
    Returneaza Studentul cu Id-ul identic cu cel al lui elem din lista de studenti
    Date intrare: elem- studentul care care Id-ul studentului care trebuie returnat
    """
    def getId(self,elem):
        
        #inMemoryRepository.getId(self,elem)
  
        self.__elems=self.__loadFromFile()
        
        
        if elem not in self.__elems:    #cauta doar dupa Id
            raise RepositoryException2("S-a incercat accesarea unui student inexistent!")
        ind = self.__elems.index(elem)  #ind primeste prima pozitie pe care apare elem
        return self.__elems[ind]        #returnam Studentul elem
    
        self.__storeToFile(self.__elems)
        
    """
    Returneaza Studentul cu Numele identic cu cel al lui elem din lista de studenti
    Date intrare: elem- studentul care care Numele studentului care trebuie returnat
    """   
    def getNume(self,elem):
        #inMemoryRepository.getNume(self,elem)
        
        self.__elems=self.__loadFromFile()
        lis=[]
        for el in self.__elems:
            if el.egalNume(elem):                      #daca gasim un student cu numele respectiv
                ind=self.__elems.index(el)             #ii retinem indexul
                lis.append(self.__elems[ind])  #il adaugam in lista lis
        if len(lis)!=0:                              #daca avem elemente in lis atunci le returnam
            return lis[:]
        else:
            raise RepositoryException2("S-a incercat accesarea unui student inexistent!")
    
        self.__storeToFile(self.__elems)
        
    """
    Returneaza lungimea listei de studenti
    """
    def size(self):
        inMemoryRepository.size(self)
        self.__elems=self.__loadFromFile()
        return len(self.__elems)
        
    """
    Returneaza toata lista de studenti
    """
    def getAll(self):
        inMemoryRepository.getAll(self)
        self.__elems=self.__loadFromFile()
        return self.__elems[:]