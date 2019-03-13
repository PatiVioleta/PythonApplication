'''
Created on Nov 18, 2017

@author: PATI
'''
from domain.nota import Nota
from validari.validari import Validator

class NotaController:
    """
    Permite gestionarea listei de note
    """
    
    """
    Initializeaza campul repo cu lista de note (repo) si creeaza un camp de tipul validator in self.__validator
    Date intrare: repo- un obiect de tip repositoryNota (lista de Note)
    """
    def __init__(self,repo):
        self.__repo = repo
        self.__validator = Validator()
    
    """
    Gestioneaza adaugarea unei note in lista de note
    Date intrare: idS- Id-ul studentului, idD- Id-ul disciplinei, nota- nota studentului la disciplina respectiva
    """
    def adaugaNota(self,idS,idD,nota):
        st = Nota(idS,idD,nota)                     #creeaza obiectul Nota cu Id-urile si nota dorite
        self.__validator.valideazaNota(st)          #valideaza obiectul Nota
        self.__repo.add(st)                         #apeleaza functia de adaugare
        return st

    """
    Gestioneaza stergerea unei discipline cu un anumit Id de student din lista de discipline
    Date intrare: idstud- Id-ul studentului caruia trebuie sa ii eliminam notele
    """
    def stergeNotaS(self, idstud):
        st = Nota(idstud,1,5)                       #creeaza o nota cu Id-ul care ne intereseaza si cu restul datelor aleatorii
        self.__validator.valideazaNota(st)          #valideaza obiectul nota
        self.__repo.remS(st)                        #apeleaza functia de stergere dupa id de student

    """
    Gestioneaza stergerea unei note cu un anumit Id de disciplina din lista de note
    Date intrare: iddis- Id-ul disciplinei careia trebuie sa ii stergem notele
    """
    def stergeNotaD(self, iddis):
        st = Nota(1,iddis,5)                        #creeaza o nota cu Id-ul care ne intereseaza si cu restul datelor aleatorii
        self.__validator.valideazaNota(st)          #valideaza obiectul nota
        self.__repo.remD(st)                        #apeleaza functia de stergere dupa id de disciplina

    """
    Gestioneaza returnarea unei liste de note care sunt asociate disciplinei cu id-ul egal cu iddis
    Date intrare: iddis-id-ul cu specificatia anterioara
    """
    def cautaNoteIddis(self,iddis):
        st=Nota(1,iddis,9)
        self.__validator.valideazaNota(st)
        return self.__repo.getIddis(st)
    

    """
    Gestioneaza extragerea tuturor elementelor din lista de note
    """
    def getAllNote(self):
        return self.__repo.getAll()                 #returneaza apelul functiei care returneaza toate elementele din lista de discipline