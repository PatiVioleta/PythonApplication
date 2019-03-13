
class RepositoryException(Exception):
    """
    Clasa de erori pentru lista de studenti
    """
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

class inMemoryRepository:
    """
    Clasa lista de studenti
    Contine o lista de studenti, fiecare student are un Id si un nume
    """
    
    """
    Initializeaza lista de studenti cu lista vida
    """
    def __init__(self):
        self.__elems=[]
    
    """ 
    Adauga la lista de studenti un nou student
    Date de intrare: elem- noul student
    """
    def add(self,elem):
        if elem in self.__elems:       #daca gaseste in lista un student egal (functia __eq__ declara doua elemente egale daca au acelasi Id) cu cel pe care vrem sa il introducem, afiseaza mesajul "exista deja"
            raise RepositoryException("Un student cu acest Id exista deja!")
        self.__elems.append(elem)
    
    """
    Sterge din lista de studenti un student cu un anumit Id
    Date intrare: elem-Studentul cu Id-ul care trebuie sa fie eliminat
    """
    def rem(self,elem):
        if elem not in self.__elems:    #daca nu gaseste in lista un student egal (functia __eq__ declara doua elemente egale daca au acelasi Id) cu cel pe care vrem sa il stergem, afiseaza mesajul "student inexistent"
            raise RepositoryException("S-a incercat stergerea unui student inexistent!")
        self.__elems.remove(elem)       #elimina prima instanta din lista de studenti care este "egala" cu instanta elem care are id-ul instantei ce trebuie sa fie eliminata
    
    """
    Modifica numele unui student cu un anumit Id
    Date intrare: elem- Noua valoare a studentului ce trebuie modificat
    """
    def upd(self,elem):
        if elem not in self.__elems:
            raise RepositoryException("S-a incercat accesarea unui student inexistent!")
        ind = self.__elems.index(elem)  #ind primeste prima pozitie unde apare Studentul elem in lista de studenti
        self.__elems[ind]=elem          #elementul din lista de studenti de pe pozitia ind primeste o noua valoare (un nou nume) adica pe elem
    
    """
    Returneaza Studentul cu Id-ul identic cu cel al lui elem din lista de studenti
    Date intrare: elem- studentul care care Id-ul studentului care trebuie returnat
    """
    def getId(self,elem):
        if elem not in self.__elems:    #cauta doar dupa Id
            raise RepositoryException("S-a incercat accesarea unui student inexistent!")
        ind = self.__elems.index(elem)  #ind primeste prima pozitie pe care apare elem
        return self.__elems[ind]        #returnam Studentul elem
    
    """
    Returneaza Studentul cu Numele identic cu cel al lui elem din lista de studenti
    Date intrare: elem- studentul care care Numele studentului care trebuie returnat
    """
    def getNume(self,elem):
        lis=inMemoryRepository()                       #lis-lista in care punem toti studentii care au numele respectiv
        for el in self.__elems:
            if el.egalNume(elem):                      #daca gasim un student cu numele respectiv
                ind=self.__elems.index(el)             #ii retinem indexul
                lis.__elems.append(self.__elems[ind])  #il adaugam in lista lis
        if lis.size()!=0:                              #daca avem elemente in lis atunci le returnam
            return lis.getAll()
        else:
            raise RepositoryException("S-a incercat accesarea unui student inexistent!")
    
    """
    Returneaza lungimea listei de studenti
    """
    def size(self):
        return len(self.__elems)

    """
    Returneaza toata lista de studenti
    """
    def getAll(self):
        return self.__elems[:]