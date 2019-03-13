
'''
Created on Nov 12, 2017

@author: PATI
'''
from domain.disciplina import Disciplina
from validari.validari import Validator

class DisciplinaController:
    """
    Permite gestionarea listei de discipline
    """
    
    """
    Initializeaza campul repo cu lista de discipline (repo) si creeaza un camp de tipul validator in self.__validator
    Date intrare: repo- un obiect de tip repositoryDisciplina (lista de Discipline)
    """
    def __init__(self,repo):
        self.__repo = repo
        self.__validator = Validator()
    
    """
    Gestioneaza adaugarea unei discipline in lista de discipline
    Date intrare: ident- Id-ul disciplinei noi, nume- numele disciplinei noi, profesor- numele profesorului disciplinei noi
    """
    def adaugaDisciplina(self,ident,nume,profesor):
        st = Disciplina(ident,nume,profesor)        #creeaza obiectul disciplina cu Id-ul si numele dorite
        self.__validator.valideazaDisciplina(st)    #valideaza obiectul Disciplina
        self.__repo.add(st)                         #apeleaza functia de adaugare
        return st

    """
    Gestioneaza modificarea unei discipline din lista de discipline
    Date intrare: ident- Id-ul disciplinei care trebuie modificata, nume- Noul nume al disciplinei, profesor- noul profesor al disciplinei
    """
    def updateDisciplina(self, ident, nume, profesor):
        st = Disciplina(ident, nume, profesor)      #creeaza obiectul disciplina cu Id-ul si numele dorite
        self.__validator.valideazaDisciplina(st)    #valideaza obiectul nou creat
        self.__repo.upd(st)                         #apeleaza functia de modificare
        return st

    """
    Gestioneaza stergerea unei discipline cu un anumit Id din lista de discipline
    Date intrare: ident- Id-ul disciplinei care trebuie sa fie eliminata
    """
    def stergeDisciplina(self, ident):
        
        st = Disciplina(ident,"ion","ion")          #creeaza o disciplina cu Id-ul care ne intereseaza si cu un nume si profesor oarecare
        self.__validator.valideazaDisciplina(st)    #valideaza obiectul st
    
        self.__repo.rem(st)                         #apeleaza functia de stergere
        
    """
    Gestioneaza cautarea unui discipline cu un anumit Id
    Date intrare: ident- Id-ul disciplinei ce trebuie sa fie cautata
    """
    def cautaDisciplinaId(self,ident):
        st=Disciplina(ident,"ion","ion")
        self.__validator.valideazaDisciplina(st)
        return self.__repo.getId(st)
    
    """
    Gestioneaza cautarea disciplinelor cu un anumit nume
    Date intrare: nume-numele disciplinelor ce trebuie sa fie cautate
    """
    def cautaDisciplinaNume(self,nume):
        st=Disciplina(1,nume,"ala")
        self.__validator.valideazaDisciplina(st)
        return self.__repo.getNume(st)
    
    """
    Gestioneaza cautarea disciplinelor cu un anumit profesor
    Date intrare: profesor- profesorul disciplinelor ce trebuie sa fie cautate
    """
    def cautaDisciplinaProfesor(self,profesor):
        st=Disciplina(1,"ala",profesor)
        self.__validator.valideazaDisciplina(st)
        return self.__repo.getProfesor(st)

    """
    Gestioneaza extragerea tuturor elementelor din lista de discipline
    """
    def getAllDiscipline(self):
        return self.__repo.getAll()                 #returneaza apelul functiei care returneaza toate elementele din lista de discipline
