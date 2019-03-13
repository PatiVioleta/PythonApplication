from domain.student import Student
from validari.validari import Validator

class StudentController:
    """
    Permite gestionarea listei de studenti
    """
    
    """
    Initializeaza campul repo cu lista de studenti (repo) si creeaza un camp de tipul validator in self.__validator
    Date intrare: repo- un obiect de tip repositoryStudent (lista de Studenti)
    """
    def __init__(self,repo):
        self.__repo = repo
        self.__validator = Validator()
    
    """
    Gestioneaza adaugarea unui student in lista de studenti
    Date intrare: ident- Id-ul noului student, nume- numele noului student
    Returneaza studentul introdus
    """
    def adaugaStudent(self,ident,nume):
        st = Student(ident,nume)                    #creeaza obiectul student cu Id-ul si numele dorite
        self.__validator.valideazaStudent(st)       #valideaza obiectul Student
        self.__repo.add(st)                         #apeleaza functia de adaugare
        return st

    """
    Gestioneaza modificarea unui student din lista de studenti
    Date intrare: ident- Id-ul studentului care trebuie modificat, nume- Noul nume al studentului
    Returneaza studentul modificat
    """
    def updateStudent(self, ident, nume):
        st = Student(ident, nume)                   #creeaza obiectul student cu Id-ul si numele dorite
        self.__validator.valideazaStudent(st)       #valideaza obiectul nou creat
        self.__repo.upd(st)                         #apeleaza functia de modificare
        return st
    
    """
    Gestioneaza stergerea unui student cu un anumit Id din lista de studenti
    Date intrare: ident- Id-ul elevului care trebuie sa fie eliminat
    """
    def stergeStudent(self, ident):
        st = Student(ident,"ion")                   #creeaza un student cu Id-ul care ne intereseaza si cu un nume oarecare
        self.__validator.valideazaStudent(st)       #valideaza obiectul st
        self.__repo.rem(st)                         #apeleaza functia de stergere

    """
    Gestioneaza cautarea unui student care are un anumit Id
    Date intrare: ident- Id-ul studentului cautat
    """
    def cautaStudentId(self,ident):
        st=Student(ident,"ion")
        self.__validator.valideazaStudent(st)
        return self.__repo.getId(st)
    
    """
    Gestioneaza cautarea unui student care are un anumit nume
    Date intrare: nume- numele studentului cautat
    """
    def cautaStudentNume(self,nume):
        st=Student(1,nume)
        self.__validator.valideazaStudent(st)
        return self.__repo.getNume(st)
    
    """
    Gestioneaza extragerea tuturor elementelor din lista de studenti
    """
    def getAllStudenti(self):
        return self.__repo.getAll()                 #returneaza apelul functiei care returneaza toate elementele din lista de studenti
    