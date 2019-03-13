'''
Created on Jan 22, 2018

@author: PATI
'''
from repo.repoJ import RepoJ
from service.serviceJ import ServiceJ
from domain.jucator import Jucator

class TestServiceJ():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.__service=ServiceJ(RepoJ("testeJucatori.txt"))
        
    def testAdd(self):
        self.__service.add(Jucator("ana","bala",120,"Fundas"))
        assert self.__service.getAll()[0].get_nume()=="ana"
        assert self.__service.getAll()[0].get_prenume()=="bala"
        assert self.__service.getAll()[0].get_inaltime()==120
        assert self.__service.getAll()[0].get_post()=="Fundas"
        with open("testeJucatori.txt","w") as f:
            f.write("")
        
    def testAdd2(self):
        self.__service.add2(Jucator("ana","bala",120,"Fundas"))
        assert self.__service.getAll()[0].get_nume()=="ana"
        assert self.__service.getAll()[0].get_prenume()=="bala"
        assert self.__service.getAll()[0].get_inaltime()==120
        assert self.__service.getAll()[0].get_post()=="Fundas"
        with open("testeJucatori.txt","w") as f:
            f.write("")
            
    def testMod(self):
        self.__service.add2(Jucator("ana","bala",120,"Fundas"))
        self.__service.mod("ana", "bala", 150)
        assert self.__service.getAll()[0].get_nume()=="ana"
        assert self.__service.getAll()[0].get_prenume()=="bala"
        assert self.__service.getAll()[0].get_inaltime()==150
        assert self.__service.getAll()[0].get_post()=="Fundas"
        with open("testeJucatori.txt","w") as f:
            f.write("")
            
    def echipa(self):
        self.__service.add2(Jucator("ana1","bala",120,"Fundas"))
        self.__service.add2(Jucator("ana2","bala",120,"Fundas"))
        self.__service.add2(Jucator("ana3","bala",120,"Pivot"))
        self.__service.add2(Jucator("ana4","bala",120,"Extrema"))
        self.__service.add2(Jucator("ana5","bala",120,"Extrema"))
        rez=self.__service.echipa()
        
        assert rez[0].get_nume()=="ana1"
        assert rez[0].get_prenume()=="bala"
        assert rez[0].get_inaltime()==120
        assert rez[0].get_post()=="Fundas"
        
        assert rez[1].get_nume()=="ana2"
        assert rez[1].get_prenume()=="bala"
        assert rez[1].get_inaltime()==120
        assert rez[1].get_post()=="Fundas"
        
        assert rez[2].get_nume()=="ana3"
        assert rez[2].get_prenume()=="bala"
        assert rez[2].get_inaltime()==120
        assert rez[2].get_post()=="Pivot"
        
        assert rez[3].get_nume()=="ana4"
        assert rez[3].get_prenume()=="bala"
        assert rez[3].get_inaltime()==120
        assert rez[3].get_post()=="Extrema"
        
        assert rez[4].get_nume()=="ana5"
        assert rez[4].get_prenume()=="bala"
        assert rez[4].get_inaltime()==120
        assert rez[4].get_post()=="Extrema"
        
        with open("testeJucatori.txt","w") as f:
            f.write("")
        
    def run(self):
        self.testAdd()
        self.testAdd2()
        self.testMod()
        self.echipa()