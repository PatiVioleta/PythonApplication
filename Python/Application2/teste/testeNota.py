from repository.repositoryNota import inMemoryRepositoryN
from service.notaController import NotaController

class testeNota():
    def __init__(self):
        pass
    
    def testInitNota(self):
        repo=inMemoryRepositoryN()
        ctrl=NotaController(repo)
        st=ctrl.adaugaNota(1,1,10)
        assert st.getIdstud()==1
        assert st.getIddis()==1
        assert st.getNote()==[10]
        
    def testAdaugaNota(self):
        repo=inMemoryRepositoryN()
        ctrl=NotaController(repo)
        st=ctrl.adaugaNota(1,1,10)
        assert len(NotaController(repo).getAllNote())==1
        assert st.getIdstud()==1
        assert st.getIddis()==1
        assert st.getNote()==[10]
        
    def testStergeNotaS(self):
        repo=inMemoryRepositoryN()
        ctrl=NotaController(repo)
        ctrl.adaugaNota(1,1,10)
        ctrl.stergeNotaS(1)
        assert len(NotaController(repo).getAllNote())==0
            
    def testStergeNotaD(self):
        repo=inMemoryRepositoryN()
        ctrl=NotaController(repo)
        ctrl.adaugaNota(1,2,10)
        ctrl.stergeNotaD(2)
        assert len(NotaController(repo).getAllNote())==0    
        
    def testGetAllNote(self):
        repo = inMemoryRepositoryN()
        ctrl=NotaController(repo)
        st0=ctrl.adaugaNota(1,1,3)
        st=ctrl.adaugaNota(2,2,10)
        repo=ctrl.getAllNote()
        assert repo[1].getNote()==st.getNote()
        assert repo[1].getIdstud()==st.getIdstud()
        assert repo[1].getIddis()==st.getIddis()
        assert repo[0].getNote()==st0.getNote()
        assert repo[0].getIdstud()==st0.getIdstud()
        assert repo[0].getIddis()==st0.getIddis()
        assert len(repo)==2
    
    def run(self):
        testeNota.testInitNota(self)
        testeNota.testAdaugaNota(self)
        testeNota.testStergeNotaS(self)
        testeNota.testStergeNotaD(self)
        testeNota.testGetAllNote(self)
