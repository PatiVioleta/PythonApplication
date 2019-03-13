'''
Created on Nov 17, 2017

@author: PATI
'''
from repository.repositoryMaterie import inMemoryRepositoryD
from service.materieController import DisciplinaController

class testeDisciplina():
    def __init__(self):
        pass
    
    def testInitDisciplina(self):
        repo=inMemoryRepositoryD()
        ctrl=DisciplinaController(repo)
        st=ctrl.adaugaDisciplina(1, "mate","popescu")
        assert st.getIddis()==1
        assert st.getNume()=="mate"
        assert st.getProfesor()=="popescu"
        
    def testAdaugaDisciplina(self):
        repo = inMemoryRepositoryD()
        ctrl=DisciplinaController(repo)
        st=ctrl.adaugaDisciplina(3,"ana","bala")
        assert len(DisciplinaController(repo).getAllDiscipline())==1
        assert st.getIddis()==3
        assert st.getNume()=="ana"
        assert st.getProfesor()=="bala"
    
    def testUpdateDisciplina(self):
        repo = inMemoryRepositoryD()
        ctrl=DisciplinaController(repo)
        ctrl.adaugaDisciplina(3, "ana","bala")
        st=ctrl.updateDisciplina(3, "pati","bala")
        assert st.getIddis()==3
        assert st.getNume()=="pati"
        assert st.getProfesor()=="bala"
        
    def testStergeDisciplina(self):
        repo = inMemoryRepositoryD()
        ctrl=DisciplinaController(repo)
        ctrl.adaugaDisciplina(3, "ana","bala")
        ctrl.stergeDisciplina(3)
        assert ctrl.getAllDiscipline()==[]
        
    def testCautaDisciplinaId(self):
        repo = inMemoryRepositoryD()
        ctrl=DisciplinaController(repo)
        ctrl.adaugaDisciplina(3, "ana","bala")
        dis=ctrl.cautaDisciplinaId(3)
        assert dis.getIddis()==3
        assert dis.getNume()=="ana"
        assert dis.getProfesor()=="bala"
        
    def testCautaDisciplinaNume(self):
        repo = inMemoryRepositoryD()
        ctrl=DisciplinaController(repo)
        ctrl.adaugaDisciplina(3, "ana","bala")
        dis=ctrl.cautaDisciplinaNume("ana")
        assert dis[0].getIddis()==3
        assert dis[0].getNume()=="ana"
        assert dis[0].getProfesor()=="bala"
        
    def testCautaDisciplinaProfesor(self):
        repo = inMemoryRepositoryD()
        ctrl=DisciplinaController(repo)
        ctrl.adaugaDisciplina(3, "ana","bala")
        dis=ctrl.cautaDisciplinaProfesor("bala")
        assert dis[0].getIddis()==3
        assert dis[0].getNume()=="ana"
        assert dis[0].getProfesor()=="bala"
        
    def testGetAllDiscipline(self):
        repo = inMemoryRepositoryD()
        ctrl=DisciplinaController(repo)
        st0=ctrl.adaugaDisciplina(3, "ana","bala")
        st=ctrl.adaugaDisciplina(4,"alin","ala")
        repo=ctrl.getAllDiscipline()
        assert repo[1].getNume()==st.getNume()
        assert repo[1].getIddis()==st.getIddis()
        assert repo[1].getProfesor()==st.getProfesor()
        assert repo[0].getNume()==st0.getNume()
        assert repo[0].getIddis()==st0.getIddis()
        assert repo[0].getProfesor()==st0.getProfesor()
        assert len(repo)==2
        
    def run(self):
        testeDisciplina.testInitDisciplina(self)
        testeDisciplina.testAdaugaDisciplina(self)
        testeDisciplina.testUpdateDisciplina(self)
        testeDisciplina.testStergeDisciplina(self)
        testeDisciplina.testCautaDisciplinaId(self)
        testeDisciplina.testCautaDisciplinaNume(self)
        testeDisciplina.testCautaDisciplinaProfesor(self)
        testeDisciplina.testGetAllDiscipline(self)