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

from repository.repositoryStudent import RepositoryException

from validari.validari import ValidatorException

import unittest


class TestStudent(unittest.TestCase):


    def setUp(self):
        self.ctrS=StudentController(inMemoryRepository())
        self.student=self.ctrS.adaugaStudent(1, "ana")
        
        self.ctrD=DisciplinaController(inMemoryRepositoryD())
        self.disciplina=self.ctrD.adaugaDisciplina(1, "info", "popescu")
        
        self.ctrN=NotaController(inMemoryRepositoryN())
        self.nota=self.ctrN.adaugaNota(1, 1, 10)

    def tearDown(self):
        pass


    def testAdaugaStudent(self):
        self.ctrS.adaugaStudent(2, "anastasia")
        self.assertTrue(self.ctrS.getAllStudenti()[1].getNume()=="anastasia")
        self.assertTrue(self.ctrS.getAllStudenti()[1].getIdstud()==2)
        
    def testUpdateStudent(self):
        self.ctrS.updateStudent(1, "pati")
        self.assertTrue(self.ctrS.getAllStudenti()[0].getNume()=="pati")
        
    def testStergeStudent(self):
        self.ctrS.stergeStudent(1)
        self.assertTrue(len(self.ctrS.getAllStudenti())==0)
        
    def testCautaStudentId(self):
        self.assertTrue(self.ctrS.cautaStudentId(1).getIdstud()==1)
        self.assertTrue(self.ctrS.cautaStudentId(1).getNume()=="ana")
    
    def testCautaStudentNume(self):
        self.assertTrue(self.ctrS.cautaStudentNume("ana")[0].getIdstud()==1)
        self.assertTrue(self.ctrS.cautaStudentNume("ana")[0].getNume()=="ana")
    
    def testGetAllStudenti(self):
        self.ctrS.adaugaStudent(2, "anastasia")
        self.assertTrue(self.ctrS.getAllStudenti()[0].getIdstud()==1)
        self.assertTrue(self.ctrS.getAllStudenti()[1].getIdstud()==2)

    def testWhiteBoxAdaugare(self):
        self.ctrS.adaugaStudent(2, "anastasia")
        self.assertTrue(len(self.ctrS.getAllStudenti())==2)
        self.assertTrue(self.ctrS.getAllStudenti()[1].getIdstud()==2)
        
    def testWhiteBoxAdaugare2(self):
        self.assertRaises(ValidatorException,self.ctrS.adaugaStudent,-2, "ana")
        self.assertRaises(RepositoryException,self.ctrS.adaugaStudent,1, "alin")
        
    def testWhiteBoxAdaugare3(self):
        self.assertRaises(ValidatorException,self.ctrS.adaugaStudent,2, "")
        
    def testWhiteBoxUpdate(self):
        self.ctrS.updateStudent(1, "pati")
        self.assertTrue(self.ctrS.getAllStudenti()[0].getNume()=="pati")
        
    def testWhiteBoxUpdate2(self):
        self.assertRaises(RepositoryException,self.ctrS.updateStudent ,2, "ana")
        self.assertRaises(ValidatorException,self.ctrS.updateStudent,-2, "ana")
        
    def testWhiteBoxSterge(self):
        self.assertRaises(ValidatorException,self.ctrS.stergeStudent,-2)
        self.assertRaises(RepositoryException,self.ctrS.stergeStudent,2)
        
    def testWhiteBoxSterge2(self):
        self.ctrS.stergeStudent(1)
        self.assertTrue(len(self.ctrS.getAllStudenti())==0)
        
    def testWhiteBoxCautaStudentId(self):
        self.assertTrue(self.ctrS.cautaStudentId(1).getIdstud()==1)
        self.assertTrue(self.ctrS.cautaStudentId(1).getNume()=="ana")
        
    def testWhiteBoxCautaStudentId2(self):
        self.assertRaises(ValidatorException,self.ctrS.cautaStudentId,-2)
        self.assertRaises(RepositoryException,self.ctrS.cautaStudentId,2)
       
    def testWhiteBoxCautaStudentNume(self):
        self.assertTrue(self.ctrS.cautaStudentNume("ana")[0].getIdstud()==1)
        self.assertTrue(self.ctrS.cautaStudentNume("ana")[0].getNume()=="ana")
        
    def testWhiteBoxCautaStudentNume2(self):
        self.assertRaises(ValidatorException,self.ctrS.cautaStudentNume,"")
        self.assertRaises(RepositoryException,self.ctrS.cautaStudentNume,"alin")
       
    def testWhiteBoxGetAllStudenti(self):
        self.ctrS.adaugaStudent(2, "anastasia")
        self.assertTrue(self.ctrS.getAllStudenti()[1].getIdstud()==2)
        self.assertTrue(len(self.ctrS.getAllStudenti())==2)
        
    def testBlackBoxAdauga(self):
        self.ctrS.adaugaStudent(2, "anastasia")
        self.assertTrue(self.ctrS.getAllStudenti()[1].getNume()=="anastasia")
        self.assertTrue(self.ctrS.getAllStudenti()[1].getIdstud()==2)
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()