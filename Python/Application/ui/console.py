'''
Created on Jan 22, 2018

@author: PATI
'''
from repo.repoJ import ExceptionR
from repo.repoF import ExceptionRF
from domain.jucator import Jucator
from repo.repoF import RepoF
from service.serviceF import ServiceF
from random import random, randint
from test.test_buffer import randitems, rand_structure

class ExceptionC(Exception):
    """
    Clasa de exceptii pentru consola
    """
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)

class Console(object):
    '''
    Clasa consola care permite interactiunea cu utilizatorul
    '''


    def __init__(self, service):
        '''
        Initailizam campul service cu service-ul pentru  jucatori
        '''
        self.__service=service
        
    """
    Functia citeste de la tastatura un nume prenume o inaltime si un post 
    Functia adauga un jucator cu atributele de mai sus in fisier
    """
    def __uiAdaugaJucator(self):
        try:
            nume=input("Dati numele jucatorului: ")
            prenume=input("Dati prenumele jucatorului: ")
            inaltime=int(input("Dati inaltimea jucatorului: "))
            post=input("Dati postul: ")
            if nume=="" or prenume=="":
                raise ExceptionC("Numele si prenumele nu pot fi vide!!!")
            if inaltime<0:
                raise ExceptionC("Inaltimea trebuie sa fie pozitiva!!!")
            if post!="Fundas" and post!="Pivot" and post!="Extrema":
                raise ExceptionC("Postul trebuie sa fie unul dintre: Fundas, Pivot, Extrema")
            self.__service.add(Jucator(nume,prenume,inaltime,post))
            print("Jucator adaugat cu succes!")
            
        except ValueError:
            print("Valori invalide!!!")
            
    """
    Functia citeste de la tastatura un nume prenume o inaltime
    Functia modifica inaltimea unui jucator cu atributele de mai sus in fisier
    """
    def __uiModificaInaltime(self):
        try:
            nume=input("Dati numele jucatorului: ")
            prenume=input("Dati prenumele jucatorului: ")
            inaltime=int(input("Dati inaltimea jucatorului: "))
            if nume=="" or prenume=="":
                raise ExceptionC("Numele si prenumele nu pot fi vide!!!")
            if inaltime<0:
                raise ExceptionC("Inaltimea trebuie sa fie pozitiva!!!")
            self.__service.mod(nume,prenume,inaltime)
            print("Inaltime modificata cu succes!")
        except ValueError:
            print("Valori invalide!!!")
            
    """
    Functia returneaza o lista care contine jucatorii care alcatuiesc o echipa
    """
    def __uiEchipa(self):
        rez=self.__service.echipa()
        print("Echipa este:")
        for x in rez:
            print(x)
            
    """
    Citeste de la tastatura un nume de fisier si adauga in lista numele jucatorilor alaturi d eo inaltime si un post random
    """
    def __uiImport(self):
        try:
            nrinit=len(self.__service.getAll())
            nume=input("Dati numele fisierului existent: ")
            repoF=RepoF(nume)
            serviceF=ServiceF(repoF)
            alls=serviceF.getAll()
            for x in alls:
                nume=x[0]
                prenume=x[1]
                inaltime=randint(150,250)
                l=["Fundas","Pivot","Extrema"]
                poz=randint(0,2)
                post=l[poz]
                try:
                    if nume=="" or prenume=="":
                        raise ExceptionC("Numele si prenumele nu pot fi vide!!!")
                    if inaltime<0:
                        raise ExceptionC("Inaltimea trebuie sa fie pozitiva!!!")
                    if post!="Fundas" and post!="Pivot" and post!="Extrema":
                        raise ExceptionC("Postul trebuie sa fie unul dintre: Fundas, Pivot, Extrema")
                    self.__service.add2(Jucator(nume,prenume,inaltime,post))
                    
                except ValueError:
                    print("Valori invalide!!!")
            print("Jucatorii care nu existau deja in fisier au fost importati cu succes!")
            nrinit2=len(self.__service.getAll())
            print("Nr de jucatori adaugati este: ")
            print (nrinit2-nrinit)
            
        except ExceptionRF as ve:
            print(ve)
        
    """
    Functia care ruleaza aplicatia
    """
    def run(self):
        while True:
            print("")
            print("1. Adauga jucator")
            print("2. Modifica inaltimea")
            print("3. Tipareste echipa")
            print("4. Importa jucatori")
            print("5. Exit")
            print("")
            
            try:
                cmd=input("Alegeti optiunea dorita: ")
                if cmd=='1':
                    self.__uiAdaugaJucator()
                if cmd=='2':
                    self.__uiModificaInaltime()
                if cmd=='3':
                    self.__uiEchipa()
                if cmd=='4':
                    self.__uiImport()
                if cmd=='5':
                    return
                
            except ValueError:
                print("Valoare invalida!")
            except ExceptionC as ve:
                print(ve)
            except ExceptionR as ve:
                print(ve)