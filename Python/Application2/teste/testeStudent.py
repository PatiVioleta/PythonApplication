from repository.repositoryStudent import inMemoryRepository
from service.studentController import StudentController

class testeStudent():
    def __init__(self):
        pass
    
    def testInitStudent(self):
        repo=inMemoryRepository()
        ctrl=StudentController(repo)
        st=ctrl.adaugaStudent(1, "ana")
        assert st.getIdstud()==1
        assert st.getNume()=="ana"
        
    def testAdaugaStudent(self):
        repo = inMemoryRepository()
        ctrl=StudentController(repo)
        st=ctrl.adaugaStudent(3,"ana")
        assert len(StudentController(repo).getAllStudenti())==1
        assert st.getNume()=="ana"
        assert st.getIdstud()==3
    
    def testUpdateStudent(self):
        repo = inMemoryRepository()
        ctrl=StudentController(repo)
        ctrl.adaugaStudent(3, "ana")
        st=ctrl.updateStudent(3, "pati")
        assert st.getIdstud()==3
        assert st.getNume()=="pati"
        
    def testStergeStudent(self):
        repo = inMemoryRepository()
        ctrl=StudentController(repo)
        ctrl.adaugaStudent(3, "ana")
        ctrl.stergeStudent(3)
        assert ctrl.getAllStudenti()==[]
        
    def testCautaStudentId(self):
        repo = inMemoryRepository()
        ctrl=StudentController(repo)
        ctrl.adaugaStudent(3, "ana")
        st=ctrl.cautaStudentId(3)
        assert st.getIdstud()==3
        assert st.getNume()=="ana"
        
    def testCautaStudentNume(self):
        repo = inMemoryRepository()
        ctrl=StudentController(repo)
        ctrl.adaugaStudent(3, "ana")
        st=ctrl.cautaStudentNume("ana")
        assert st[0].getIdstud()==3
        assert st[0].getNume()=="ana"
        
    def testGetAllStudenti(self):
        repo = inMemoryRepository()
        ctrl=StudentController(repo)
        st0=ctrl.adaugaStudent(3, "ana")
        st=ctrl.adaugaStudent(4,"alin")
        repo=ctrl.getAllStudenti()
        assert repo[1].getNume()==st.getNume()
        assert repo[1].getIdstud()==st.getIdstud()
        assert repo[0].getNume()==st0.getNume()
        assert repo[0].getIdstud()==st0.getIdstud()
        assert len(repo)==2
        
    def run(self):
        testeStudent.testInitStudent(self)
        testeStudent.testAdaugaStudent(self)
        testeStudent.testUpdateStudent(self)
        testeStudent.testStergeStudent(self)
        testeStudent.testCautaStudentId(self)
        testeStudent.testCautaStudentNume(self)
        testeStudent.testGetAllStudenti(self)
        