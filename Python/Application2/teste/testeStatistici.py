'''
Created on Dec 1, 2017

@author: PATI
'''
from repository.repositoryStudent import inMemoryRepository
from repository.repositoryNota import inMemoryRepositoryN
from repository.repositoryMaterie import inMemoryRepositoryD
from service.studentController import StudentController
from service.notaController import NotaController
from service.materieController import DisciplinaController
from service.statisticiController import StatisticiController

class testeStatistici():
    def __init__(self):
        pass
    
    def testOrdAlf(self):
        repo=inMemoryRepository()
        repoN=inMemoryRepositoryN()
        repoD=inMemoryRepositoryD()
        ctrl=StudentController(repo)
        ctrlN=NotaController(repoN)
        ctrlD=DisciplinaController(repoD)
        ctrlS=StatisticiController(repo,repoN,repoD,ctrl,ctrlD,ctrlN)
        
        ctrl.adaugaStudent(1,"ion")
        ctrl.adaugaStudent(2,"ana")
        ctrl.adaugaStudent(3,"alin")
        
        ctrlD.adaugaDisciplina(1,"mate","popescu")
        
        ctrlN.adaugaNota(1,1,4)
        ctrlN.adaugaNota(2,1,6)
        ctrlN.adaugaNota(3,1,7)
        
        lis=ctrlS.ordonareAlfabetic("mate")
        
        assert lis[0].getIdstud()==3
        assert lis[0].getIddis()==1
        assert lis[0].getNote()==[7]
        assert lis[1].getIdstud()==2
        assert lis[1].getIddis()==1
        assert lis[1].getNote()==[6]
        assert lis[2].getIdstud()==1
        assert lis[2].getIddis()==1
        assert lis[2].getNote()==[4]
        
    def testOrdNum(self):
        repo=inMemoryRepository()
        repoN=inMemoryRepositoryN()
        repoD=inMemoryRepositoryD()
        ctrl=StudentController(repo)
        ctrlN=NotaController(repoN)
        ctrlD=DisciplinaController(repoD)
        ctrlS=StatisticiController(repo,repoN,repoD,ctrl,ctrlD,ctrlN)
        
        ctrl.adaugaStudent(1,"ion")
        ctrl.adaugaStudent(2,"ana")
        ctrl.adaugaStudent(3,"alin")
        
        ctrlD.adaugaDisciplina(1,"mate","popescu")
        
        ctrlN.adaugaNota(1,1,4)
        ctrlN.adaugaNota(2,1,6)
        ctrlN.adaugaNota(3,1,7)
        
        lis=ctrlS.ordonareNumeric("mate")
        assert lis[0].getIdstud()==1
        assert lis[0].getIddis()==1
        assert lis[0].getNote()==[4]
        assert lis[1].getIdstud()==2
        assert lis[1].getIddis()==1
        assert lis[1].getNote()==[6]
        assert lis[2].getIdstud()==3
        assert lis[2].getIddis()==1
        assert lis[2].getNote()==[7]
        
    def test20(self):
        repo=inMemoryRepository()
        repoN=inMemoryRepositoryN()
        repoD=inMemoryRepositoryD()
        ctrl=StudentController(repo)
        ctrlN=NotaController(repoN)
        ctrlD=DisciplinaController(repoD)
        ctrlS=StatisticiController(repo,repoN,repoD,ctrl,ctrlD,ctrlN)
        
        ctrl.adaugaStudent(1,"ion")
        ctrl.adaugaStudent(2,"ana")
        ctrl.adaugaStudent(3,"alin")
        ctrl.adaugaStudent(4,"maria")
        ctrl.adaugaStudent(5,"andrei")
        ctrl.adaugaStudent(6,"ionela")
        ctrl.adaugaStudent(7,"anastasia")
        ctrl.adaugaStudent(8,"dorel")
        ctrl.adaugaStudent(9,"miruna")
        ctrl.adaugaStudent(10,"stefan")
        
        ctrlD.adaugaDisciplina(1,"mate","popescu")
        ctrlD.adaugaDisciplina(2,"info","ionescu")
        ctrlD.adaugaDisciplina(4,"mate","ion")
        ctrlD.adaugaDisciplina(3,"logica","predescu")
        
        ctrlN.adaugaNota(1,1,4)
        ctrlN.adaugaNota(1,1,10)
        ctrlN.adaugaNota(3,2,9)
        ctrlN.adaugaNota(1,4,3)
        ctrlN.adaugaNota(2,1,6)
        ctrlN.adaugaNota(4,1,7)
        ctrlN.adaugaNota(5,1,4)
        ctrlN.adaugaNota(6,1,10)
        ctrlN.adaugaNota(7,2,9)
        ctrlN.adaugaNota(8,4,3)
        ctrlN.adaugaNota(9,1,6)
        ctrlN.adaugaNota(10,1,7)
        
        lis=ctrlS.primi()
        assert lis[0][0]=="ionela"
        assert lis[0][1]==10
        assert lis[1][0]=="alin"
        assert lis[1][1]==9
        
    def run(self):
        testeStatistici.testOrdAlf(self)
        testeStatistici.testOrdNum(self)
        testeStatistici.test20(self)
        