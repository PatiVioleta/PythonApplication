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

from repository.repositoryNota import RepositoryExceptionN

from validari.validari import ValidatorException

import unittest


class TestNota(unittest.TestCase):


    def setUp(self):
        self.ctrS=StudentController(inMemoryRepository())
        self.student=self.ctrS.adaugaStudent(1, "ana")
        
        self.ctrD=DisciplinaController(inMemoryRepositoryD())
        self.disciplina=self.ctrD.adaugaDisciplina(1, "info", "popescu")
        
        self.ctrN=NotaController(inMemoryRepositoryN())
        self.nota=self.ctrN.adaugaNota(1, 1, 10)

    def tearDown(self):
        pass


    def testAdaugaNota(self):
        self.ctrS.adaugaStudent(2,"ion")
        self.ctrD.adaugaDisciplina(2,"logica","pop")
        self.ctrN.adaugaNota(2,2 ,9)
        self.assertTrue(len(self.ctrN.getAllNote())==2)    
        self.assertTrue(self.ctrN.getAllNote()[1].getIdstud()==2 and self.ctrN.getAllNote()[1].getIddis()==2)
       
    def testAdaugaNota2(self):
        self.ctrS.adaugaStudent(2,"ion")
        self.ctrD.adaugaDisciplina(2,"logica","pop")
        self.ctrN.adaugaNota(2,2 ,9)   
        self.assertTrue(self.ctrN.getAllNote()[1].getIddis()==2)
        self.assertTrue(self.ctrN.getAllNote()[1].getNote()==[9])
        
    def testStergeNotaS(self):
        self.ctrN.stergeNotaS(1)
        self.assertTrue(len(self.ctrN.getAllNote())==0)
        
    def testStergeNotaD(self):
        self.ctrN.stergeNotaD(1)
        self.assertTrue(len(self.ctrN.getAllNote())==0)
        
    def testCautaNotaIddis(self):
        self.assertTrue(self.ctrN.cautaNoteIddis(1)[0].getIddis()==1)
        self.assertTrue(self.ctrN.cautaNoteIddis(1)[0].getIdstud()==1)
        
    def testCautaNotaIddis2(self):   
        self.assertTrue(self.ctrN.cautaNoteIddis(1)[0].getNote()==[10])
        
    def testGetAllNote(self):
        self.ctrS.adaugaStudent(2,"ion")
        self.ctrD.adaugaDisciplina(2,"logica","pop")
        self.ctrN.adaugaNota(2,2 ,9)
        self.assertTrue(self.ctrN.getAllNote()[0].getIddis()==1)
        self.assertTrue(self.ctrN.getAllNote()[0].getIdstud()==1)
        
    def testGetAllNote2(self):
        self.ctrS.adaugaStudent(2,"ion")
        self.ctrD.adaugaDisciplina(2,"logica","pop")
        self.ctrN.adaugaNota(2,2 ,9)
        self.assertTrue(self.ctrN.getAllNote()[0].getNote()==[10])
        self.assertTrue(self.ctrN.getAllNote()[1].getIddis()==2)
        
    def testGetAllNote3(self):
        self.ctrS.adaugaStudent(2,"ion")
        self.ctrD.adaugaDisciplina(2,"logica","pop")
        self.ctrN.adaugaNota(2,2 ,9)
        self.assertTrue(self.ctrN.getAllNote()[1].getIdstud()==2)
        self.assertTrue(self.ctrN.getAllNote()[1].getNote()==[9])
        
    def testGetAllNote4(self):
        self.ctrS.adaugaStudent(2,"ion")
        self.ctrD.adaugaDisciplina(2,"logica","pop")
        self.ctrN.adaugaNota(2,2 ,9)
        self.assertTrue(len(self.ctrN.getAllNote())==2)

    def testWhiteBoxAdaugare(self):
        self.ctrS.adaugaStudent(2,"ion")
        self.ctrD.adaugaDisciplina(2,"logica","pop")
        self.ctrN.adaugaNota(2,2 ,9)
        self.assertTrue(len(self.ctrN.getAllNote())==2)
        self.assertTrue(self.ctrN.getAllNote()[1].getIdstud()==2)
        
    def testWhiteBoxAdaugare2(self):
        self.ctrS.adaugaStudent(2,"ion")
        self.ctrD.adaugaDisciplina(2,"logica","pop")
        self.ctrN.adaugaNota(2,2 ,9)   
        self.assertTrue(self.ctrN.getAllNote()[1].getIddis()==2)
        self.assertTrue(self.ctrN.getAllNote()[1].getNote()==[9])
    
    def testWhiteBoxAdaugare3(self):
        self.ctrS.adaugaStudent(2,"ion")
        self.ctrD.adaugaDisciplina(2,"logica","pop")
        self.ctrN.adaugaNota(2,2 ,9)
        self.assertRaises(ValidatorException,self.ctrN.adaugaNota,2,-2,0)
        self.assertRaises(ValidatorException,self.ctrN.adaugaNota,-2, 1,0)
        
    def testWhiteBoxAdaugare4(self):
        self.ctrS.adaugaStudent(2,"ion")
        self.ctrD.adaugaDisciplina(2,"logica","pop")
        self.ctrN.adaugaNota(2,2 ,9)
        self.assertRaises(ValidatorException,self.ctrN.adaugaNota,2, 1,-3)
    
    def testWhiteBoxStergeS(self):
        self.assertRaises(ValidatorException,self.ctrN.stergeNotaS,-2)

        self.ctrN.stergeNotaS(1)
        self.assertTrue(len(self.ctrN.getAllNote())==0)
        
    def testWhiteBoxStergeD(self):
        self.assertRaises(ValidatorException,self.ctrN.stergeNotaD,-2)

        self.ctrN.stergeNotaD(1)
        self.assertTrue(len(self.ctrN.getAllNote())==0)
        
    def testWhiteBoxCautaNoteId(self):
        self.assertTrue(self.ctrN.cautaNoteIddis(1)[0].getIddis()==1)
        self.assertTrue(self.ctrN.cautaNoteIddis(1)[0].getIdstud()==1)
        
    def testWhiteBoxCautaNoteId2(self):
        self.assertTrue(self.ctrN.cautaNoteIddis(1)[0].getNote()==[10])
        self.assertRaises(ValidatorException,self.ctrN.cautaNoteIddis,-2)
        
    def testWhiteBoxCautaNoteId3(self):
        self.assertRaises(RepositoryExceptionN,self.ctrN.cautaNoteIddis,2)
       
    def testWhiteBoxGetAllNote(self):
        self.ctrS.adaugaStudent(2,"ion")
        self.ctrD.adaugaDisciplina(2,"logica","pop")
        self.ctrN.adaugaNota(2,2 ,9)
        self.assertTrue(self.ctrN.getAllNote()[0].getIddis()==1)
        self.assertTrue(self.ctrN.getAllNote()[0].getIdstud()==1)
        
    def testWhiteBoxGetAllNote2(self):
        self.ctrS.adaugaStudent(2,"ion")
        self.ctrD.adaugaDisciplina(2,"logica","pop")
        self.ctrN.adaugaNota(2,2 ,9)
        self.assertTrue(self.ctrN.getAllNote()[0].getNote()==[10])
        self.assertTrue(self.ctrN.getAllNote()[1].getIddis()==2)
        
    def testWhiteBoxGetAllNote3(self):
        self.ctrS.adaugaStudent(2,"ion")
        self.ctrD.adaugaDisciplina(2,"logica","pop")
        self.ctrN.adaugaNota(2,2 ,9)
        self.assertTrue(self.ctrN.getAllNote()[1].getIdstud()==2)
        self.assertTrue(self.ctrN.getAllNote()[1].getNote()==[9])
        
    def testBlackBoxAdauga(self):
        self.ctrS.adaugaStudent(2,"ion")
        self.ctrD.adaugaDisciplina(2,"logica","pop")
        self.ctrN.adaugaNota(2,2 ,9)
        self.assertTrue(len(self.ctrN.getAllNote())==2)
        self.assertTrue(self.ctrN.getAllNote()[1].getIdstud()==2)
        
    def testBlackBoxAdauga2(self):
        self.ctrS.adaugaStudent(2,"ion")
        self.ctrD.adaugaDisciplina(2,"logica","pop")
        self.ctrN.adaugaNota(2,2 ,9)
        self.assertTrue(self.ctrN.getAllNote()[1].getIddis()==2)
        self.assertTrue(self.ctrN.getAllNote()[1].getNote()==[9])
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()