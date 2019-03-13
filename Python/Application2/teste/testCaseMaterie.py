'''
Created on Dec 7, 2017

@author: PATI
'''
from repository.repositoryStudent import inMemoryRepository
from repository.repositoryMaterie import inMemoryRepositoryD
from repository.repositoryNota import inMemoryRepositoryN
from service.studentController import StudentController
from service.materieController import DisciplinaController
from service.notaController import NotaController

from repository.repositoryMaterie import RepositoryExceptionD

from validari.validari import ValidatorException

import unittest


class TestDisciplina(unittest.TestCase):


    def setUp(self):
        self.ctrS=StudentController(inMemoryRepository())
        self.student=self.ctrS.adaugaStudent(1, "ana")
        
        self.ctrD=DisciplinaController(inMemoryRepositoryD())
        self.disciplina=self.ctrD.adaugaDisciplina(1, "info", "popescu")
        
        self.ctrN=NotaController(inMemoryRepositoryN())
        self.nota=self.ctrN.adaugaNota(1, 1, 10)

    def tearDown(self):
        pass


    def testAdaugaDisciplina(self):
        self.ctrD.adaugaDisciplina(2, "logica","predescu")
        self.assertTrue(len(self.ctrD.getAllDiscipline())==2)
        self.assertTrue(self.ctrD.getAllDiscipline()[1].getIddis()==2)
        
    def testUpdateDisciplina(self):
        self.ctrD.updateDisciplina(1, "pati","predescu")
        self.assertTrue(self.ctrD.getAllDiscipline()[0].getIddis()==1)
        self.assertTrue(self.ctrD.getAllDiscipline()[0].getProfesor()=="predescu")
        
    def testStergeDisciplina(self):
        self.ctrD.stergeDisciplina(1)
        self.assertTrue(len(self.ctrD.getAllDiscipline())==0)
        
    def testCautaDisciplinaId(self):
        self.assertTrue(self.ctrD.cautaDisciplinaId(1).getIddis()==1)
        
    def testCautaDisciplinaId2(self):
        self.assertTrue(self.ctrD.cautaDisciplinaId(1).getNume()=="info")
        self.assertTrue(self.ctrD.cautaDisciplinaId(1).getProfesor()=="popescu")
    
    def testCautaDisciplinaNume(self):
        self.assertTrue(self.ctrD.cautaDisciplinaNume("info")[0].getIddis()==1)
        
    def testCautaDisciplinaNume2(self):
        self.assertTrue(self.ctrD.cautaDisciplinaNume("info")[0].getNume()=="info")
        self.assertTrue(self.ctrD.cautaDisciplinaNume("info")[0].getProfesor()=="popescu")
    
    def testCautaDisciplinaProfesor(self):
        self.assertTrue(self.ctrD.cautaDisciplinaProfesor("popescu")[0].getIddis()==1)
        
    def testCautaDisciplinaProfesor2(self):
        self.assertTrue(self.ctrD.cautaDisciplinaProfesor("popescu")[0].getNume()=="info")
        self.assertTrue(self.ctrD.cautaDisciplinaProfesor("popescu")[0].getProfesor()=="popescu")
    
    def testGetAllDiscipline(self):
        self.ctrD.adaugaDisciplina(2, "logica","predescu")
        self.assertTrue(self.ctrD.getAllDiscipline()[0].getIddis()==1)
        self.assertTrue(self.ctrD.getAllDiscipline()[0].getNume()=="info")
        
    def testGetAllDiscipline2(self):
        self.ctrD.adaugaDisciplina(2, "logica","predescu")
        self.assertTrue(self.ctrD.getAllDiscipline()[0].getProfesor()=="popescu")
        self.assertTrue(self.ctrD.getAllDiscipline()[1].getIddis()==2)
        
    def testGetAllDiscipline3(self):  
        self.ctrD.adaugaDisciplina(2, "logica","predescu")
        self.assertTrue(self.ctrD.getAllDiscipline()[1].getNume()=="logica")
        self.assertTrue(self.ctrD.getAllDiscipline()[1].getProfesor()=="predescu")

    def testWhiteBoxAdaugare(self):
        self.assertRaises(RepositoryExceptionD,self.ctrD.adaugaDisciplina,1, "info","ion")
        self.assertTrue(len(self.ctrD.getAllDiscipline())==1)
        
    def testWhiteBoxAdaugare2(self):
        self.ctrD.adaugaDisciplina(2, "logica","predescu")
        self.assertTrue(len(self.ctrD.getAllDiscipline())==2)
        self.assertTrue(self.ctrD.getAllDiscipline()[1].getNume()=="logica")
        
    def testWhiteBoxAdaugare3(self):   
        self.ctrD.adaugaDisciplina(2, "logica","predescu")
        self.assertTrue(self.ctrD.getAllDiscipline()[1].getIddis()==2)
        self.assertTrue(self.ctrD.getAllDiscipline()[1].getProfesor()=="predescu")
        
    def testWhiteBoxAdaugare4(self):   
        self.ctrD.adaugaDisciplina(2, "logica","predescu")
        self.assertRaises(ValidatorException,self.ctrD.adaugaDisciplina,2, "","")
        self.assertRaises(ValidatorException,self.ctrD.adaugaDisciplina,-2, "ana","mn")
        
    def testWhiteBoxUpdate(self):
        self.ctrD.updateDisciplina(1, "algebra","modoi")
        self.assertTrue(self.ctrD.getAllDiscipline()[0].getNume()=="algebra")
        self.assertTrue(self.ctrD.getAllDiscipline()[0].getProfesor()=="modoi")
        
    def testWhiteBoxUpdate2(self):
        self.ctrD.updateDisciplina(1, "algebra","modoi")
        self.assertRaises(RepositoryExceptionD,self.ctrD.updateDisciplina ,2, "ana","ala")
        self.assertRaises(ValidatorException,self.ctrD.updateDisciplina,-2, "ana","da")
        
    def testWhiteBoxUpdate3(self):
        self.ctrD.updateDisciplina(1, "algebra","modoi")  
        self.assertRaises(ValidatorException,self.ctrD.updateDisciplina,2, "","da")
        self.assertRaises(ValidatorException,self.ctrD.updateDisciplina,2, "ana","")
        
    def testWhiteBoxSterge(self):
        self.assertRaises(ValidatorException,self.ctrD.stergeDisciplina,-2)
        self.assertRaises(RepositoryExceptionD,self.ctrD.stergeDisciplina,2)
        self.ctrD.stergeDisciplina(1)
        
    def testWhiteBoxCautaDisciplinaId(self):
        self.assertTrue(self.ctrD.cautaDisciplinaId(1).getIddis()==1)
        self.assertTrue(self.ctrD.cautaDisciplinaId(1).getNume()=="info")
        
    def testWhiteBoxCautaDisciplinaId2(self):
        self.assertTrue(self.ctrD.cautaDisciplinaId(1).getProfesor()=="popescu")
        
    def testWhiteBoxCautaDisciplinaId3(self):
        self.assertRaises(ValidatorException,self.ctrD.cautaDisciplinaId,-2)
        self.assertRaises(RepositoryExceptionD,self.ctrD.cautaDisciplinaId,2)
       
    def testWhiteBoxCautaDisciplinaNume(self):
        self.assertTrue(self.ctrD.cautaDisciplinaNume("info")[0].getIddis()==1)
        self.assertTrue(self.ctrD.cautaDisciplinaNume("info")[0].getNume()=="info")
        
    def testWhiteBoxCautaDisciplinaNume2(self):   
        self.assertTrue(self.ctrD.cautaDisciplinaNume("info")[0].getProfesor()=="popescu")
    
    def testWhiteBoxCautaDisciplinaNume3(self):
        self.assertRaises(ValidatorException,self.ctrD.cautaDisciplinaNume,"")
        self.assertRaises(RepositoryExceptionD,self.ctrD.cautaDisciplinaNume,"alin")
       
    def testWhiteBoxGetAllDiscipline(self):
        self.ctrD.adaugaDisciplina(2, "logica","predescu")
        self.assertTrue(self.ctrD.getAllDiscipline()[0].getIddis()==1)
        self.assertTrue(self.ctrD.getAllDiscipline()[0].getNume()=="info")
        
    def testWhiteBoxGetAllDiscipline2(self):
        self.ctrD.adaugaDisciplina(2, "logica","predescu")
        self.assertTrue(self.ctrD.getAllDiscipline()[0].getProfesor()=="popescu")
        self.assertTrue(self.ctrD.getAllDiscipline()[1].getIddis()==2)
        
    def testWhiteBoxGetAllDiscipline3(self):
        self.ctrD.adaugaDisciplina(2, "logica","predescu")
        self.assertTrue(self.ctrD.getAllDiscipline()[1].getNume()=="logica")
        self.assertTrue(self.ctrD.getAllDiscipline()[1].getProfesor()=="predescu")
        
    def testWhiteBoxGetAllDiscipline4(self):
        self.ctrD.adaugaDisciplina(2, "logica","predescu")
        self.assertTrue(len(self.ctrD.getAllDiscipline())==2)

        
    def testBlackBoxAdauga(self):
        self.ctrD.adaugaDisciplina(2, "logica","predescu")
        self.assertTrue(len(self.ctrD.getAllDiscipline())==2)
        self.assertTrue(self.ctrD.getAllDiscipline()[1].getNume()=="logica")
        
    def testBlackBoxAdauga2(self):
        self.ctrD.adaugaDisciplina(2, "logica","predescu")   
        self.assertTrue(self.ctrD.getAllDiscipline()[1].getIddis()==2)
        self.assertTrue(self.ctrD.getAllDiscipline()[1].getProfesor()=="predescu")
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()