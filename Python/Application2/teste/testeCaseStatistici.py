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
from service.statisticiController import StatisticiController

from repository.repositoryMaterie import RepositoryExceptionD
from repository.repositoryStudent import RepositoryException
from repository.repositoryNota import RepositoryExceptionN
from validari.validari import ValidatorException

import unittest


class TestNota(unittest.TestCase):

    def setUp(self):
        self.ctrS=StudentController(inMemoryRepository())
        self.ctrD=DisciplinaController(inMemoryRepositoryD())
        self.ctrN=NotaController(inMemoryRepositoryN())
        self.ctrSS=StatisticiController(inMemoryRepository,inMemoryRepositoryN,inMemoryRepositoryD,self.ctrS,self.ctrD,self.ctrN)
        
    def tearDown(self):
        pass
    
    def testOrdAlf(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[0].getIdstud()==3)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[0].getIddis()==1)
        
    def testOrdAlf2(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[0].getNote()==[7])
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[1].getIdstud()==2)
        
    def testOrdAlf3(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[1].getIddis()==1)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[1].getNote()==[6])
        
    def testOrdAlf4(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[2].getIdstud()==1)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[2].getIddis()==1)
        
    def testOrdAlf5(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[2].getNote()==[4])
        
    def testOrdNumeric(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        
        self.assertTrue(self.ctrSS.ordonareNumeric("mate")[0].getIdstud()==1)
        self.assertTrue(self.ctrSS.ordonareNumeric("mate")[0].getIddis()==1)
        
    def testOrdNumeric2(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareNumeric("mate")[0].getNote()==[4])
        self.assertTrue(self.ctrSS.ordonareNumeric("mate")[1].getIdstud()==2)
        
    def testOrdNumeric3(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareNumeric("mate")[1].getIddis()==1)
        self.assertTrue(self.ctrSS.ordonareNumeric("mate")[1].getNote()==[6])
        
    def testOrdNumeric4(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareNumeric("mate")[2].getIdstud()==3)
        self.assertTrue(self.ctrSS.ordonareNumeric("mate")[2].getIddis()==1)
        
    def testOrdNumeric5(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareNumeric("mate")[2].getNote()==[7])
    
    def test20(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrS.adaugaStudent(4, "maria")
        self.ctrS.adaugaStudent(5, "andrei")
        self.ctrS.adaugaStudent(6, "ionela")
        self.ctrS.adaugaStudent(7, "anastasia")
        self.ctrS.adaugaStudent(8, "dorel")
        self.ctrS.adaugaStudent(9, "miruna")
        self.ctrS.adaugaStudent(10, "stefan")
        
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrD.adaugaDisciplina(2, "info","ionescu")
        self.ctrD.adaugaDisciplina(3, "mate","ion")
        self.ctrD.adaugaDisciplina(4, "logica","predescu")
        
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(1,1 ,10)
        self.ctrN.adaugaNota(3,2 ,9)
        self.ctrN.adaugaNota(1,4 ,3)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(4,1 ,7)
        self.ctrN.adaugaNota(5,1 ,4)
        self.ctrN.adaugaNota(6,1 ,10)
        self.ctrN.adaugaNota(7,2 ,9)
        self.ctrN.adaugaNota(8,4 ,3)
        self.ctrN.adaugaNota(9,1 ,6)
        self.ctrN.adaugaNota(10,1 ,7)
        
        self.assertTrue(self.ctrSS.primi()[0][0]=="ionela")
        self.assertTrue(self.ctrSS.primi()[0][1]==10)
        
    def test202(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrS.adaugaStudent(4, "maria")
        self.ctrS.adaugaStudent(5, "andrei")
        self.ctrS.adaugaStudent(6, "ionela")
        self.ctrS.adaugaStudent(7, "anastasia")
        self.ctrS.adaugaStudent(8, "dorel")
        self.ctrS.adaugaStudent(9, "miruna")
        self.ctrS.adaugaStudent(10, "stefan")
        
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrD.adaugaDisciplina(2, "info","ionescu")
        self.ctrD.adaugaDisciplina(3, "mate","ion")
        self.ctrD.adaugaDisciplina(4, "logica","predescu")
        
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(1,1 ,10)
        self.ctrN.adaugaNota(3,2 ,9)
        self.ctrN.adaugaNota(1,4 ,3)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(4,1 ,7)
        self.ctrN.adaugaNota(5,1 ,4)
        self.ctrN.adaugaNota(6,1 ,10)
        self.ctrN.adaugaNota(7,2 ,9)
        self.ctrN.adaugaNota(8,4 ,3)
        self.ctrN.adaugaNota(9,1 ,6)
        self.ctrN.adaugaNota(10,1 ,7)
        self.assertTrue(self.ctrSS.primi()[1][0]=="alin")
        self.assertTrue(self.ctrSS.primi()[1][1]==9)
        
    def testWhiteBoxOrdAlf(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[0].getIdstud()==3)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[0].getIddis()==1)
        
    def testWhiteBoxOrdAlf2(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[0].getNote()==[7])
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[1].getIdstud()==2)
        
    def testWhiteBoxOrdAlf3(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[1].getIddis()==1)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[1].getNote()==[6])
        
    def testWhiteBoxOrdAlf4(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[2].getIdstud()==1)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[2].getIddis()==1)
        
    def testWhiteBoxOrdAlf5(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[2].getNote()==[4])
        
    def testWhiteBoxOrdAlf6(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertRaises(ValidatorException,self.ctrD.adaugaDisciplina,2, "","")
        self.assertRaises(ValidatorException,self.ctrD.adaugaDisciplina,-2, "ana","mn")
        
    def testWhiteBoxOrdAlf7(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[0].getIdstud()==3)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[0].getIddis()==1)
        
    def testWhiteBoxOrdAlf8(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[0].getNote()==[7])
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[1].getIdstud()==2)
        
    def testWhiteBoxOrdAlf9(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[1].getIddis()==1)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[1].getNote()==[6])
        
    def testWhiteBoxOrdAlf10(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[2].getIdstud()==1)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[2].getIddis()==1)
        
    def testWhiteBoxOrdAlf11(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertRaises(ValidatorException,self.ctrN.adaugaNota,2,-2,0)
        self.assertRaises(ValidatorException,self.ctrN.adaugaNota,-2, 1,0)
        
    def testWhiteBoxOrdAlf12(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[0].getIdstud()==3)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[0].getIddis()==1)
        
    def testWhiteBoxOrdAlf13(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[0].getNote()==[7])
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[1].getIdstud()==2)
        
    def testWhiteBoxOrdAlf14(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[1].getIddis()==1)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[1].getNote()==[6])
        
    def testWhiteBoxOrdAlf15(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[2].getIdstud()==1)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[2].getIddis()==1)
        
    def testWhiteBoxOrdAlf16(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertRaises(ValidatorException,self.ctrN.adaugaNota,2, 1,-3)
        self.assertRaises(ValidatorException,self.ctrS.adaugaStudent,2, "")
        
    def testWhiteBoxOrdAlf17(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[0].getIdstud()==3)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[0].getIddis()==1)
        
    def testWhiteBoxOrdAlf18(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[0].getNote()==[7])
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[1].getIdstud()==2)
        
    def testWhiteBoxOrdAlf19(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[1].getIddis()==1)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[1].getNote()==[6])
        
    def testWhiteBoxOrdAlf20(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[2].getIdstud()==1)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[2].getIddis()==1)
        
    def testWhiteBoxOrdAlf21(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[2].getNote()==[4])
        self.assertRaises(ValidatorException,self.ctrS.adaugaStudent,-2, "ana")
        
        
    def testWhiteBoxOrdNumeric(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        
        self.assertTrue(self.ctrSS.ordonareNumeric("mate")[0].getIdstud()==1)
        self.assertTrue(self.ctrSS.ordonareNumeric("mate")[0].getIddis()==1)
        
    def testWhiteBoxOrdNumeric2(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareNumeric("mate")[0].getNote()==[4])
        self.assertTrue(self.ctrSS.ordonareNumeric("mate")[1].getIdstud()==2)
        
    def testWhiteBoxOrdNumeric3(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareNumeric("mate")[1].getIddis()==1)
        self.assertTrue(self.ctrSS.ordonareNumeric("mate")[1].getNote()==[6])
        
    def testWhiteBoxOrdNumeric4(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareNumeric("mate")[2].getIdstud()==3)
        self.assertTrue(self.ctrSS.ordonareNumeric("mate")[2].getIddis()==1)

    def testWhiteBoxOrdNumeric5(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertRaises(ValidatorException,self.ctrD.adaugaDisciplina,2, "","")
        self.assertRaises(ValidatorException,self.ctrD.adaugaDisciplina,-2, "ana","mn")
        
    def testWhiteBoxOrdNumeric6(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertRaises(ValidatorException,self.ctrN.adaugaNota,2,-2,0)
        self.assertRaises(ValidatorException,self.ctrN.adaugaNota,-2, 1,0)
        
    def testWhiteBoxOrdNumeric7(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertRaises(ValidatorException,self.ctrN.adaugaNota,2, 1,-3)
        self.assertRaises(ValidatorException,self.ctrS.adaugaStudent,2, "")
        
    def testWhiteBoxOrdNumeric8(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertRaises(ValidatorException,self.ctrS.adaugaStudent,-2, "ana")
        
    
    def testWhiteBox20(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrS.adaugaStudent(4, "maria")
        self.ctrS.adaugaStudent(5, "andrei")
        self.ctrS.adaugaStudent(6, "ionela")
        self.ctrS.adaugaStudent(7, "anastasia")
        self.ctrS.adaugaStudent(8, "dorel")
        self.ctrS.adaugaStudent(9, "miruna")
        self.ctrS.adaugaStudent(10, "stefan")
        
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrD.adaugaDisciplina(2, "info","ionescu")
        self.ctrD.adaugaDisciplina(3, "mate","ion")
        self.ctrD.adaugaDisciplina(4, "logica","predescu")
        
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(1,1 ,10)
        self.ctrN.adaugaNota(3,2 ,9)
        self.ctrN.adaugaNota(1,4 ,3)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(4,1 ,7)
        self.ctrN.adaugaNota(5,1 ,4)
        self.ctrN.adaugaNota(6,1 ,10)
        self.ctrN.adaugaNota(7,2 ,9)
        self.ctrN.adaugaNota(8,4 ,3)
        self.ctrN.adaugaNota(9,1 ,6)
        self.ctrN.adaugaNota(10,1 ,7)
        
        self.assertTrue(self.ctrSS.primi()[0][0]=="ionela")
        self.assertTrue(self.ctrSS.primi()[0][1]==10)
        
    def testWhiteBox202(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrS.adaugaStudent(4, "maria")
        self.ctrS.adaugaStudent(5, "andrei")
        self.ctrS.adaugaStudent(6, "ionela")
        self.ctrS.adaugaStudent(7, "anastasia")
        self.ctrS.adaugaStudent(8, "dorel")
        self.ctrS.adaugaStudent(9, "miruna")
        self.ctrS.adaugaStudent(10, "stefan")
        
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrD.adaugaDisciplina(2, "info","ionescu")
        self.ctrD.adaugaDisciplina(3, "mate","ion")
        self.ctrD.adaugaDisciplina(4, "logica","predescu")
        
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(1,1 ,10)
        self.ctrN.adaugaNota(3,2 ,9)
        self.ctrN.adaugaNota(1,4 ,3)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(4,1 ,7)
        self.ctrN.adaugaNota(5,1 ,4)
        self.ctrN.adaugaNota(6,1 ,10)
        self.ctrN.adaugaNota(7,2 ,9)
        self.ctrN.adaugaNota(8,4 ,3)
        self.ctrN.adaugaNota(9,1 ,6)
        self.ctrN.adaugaNota(10,1 ,7)
        self.assertTrue(self.ctrSS.primi()[1][0]=="alin")
        self.assertTrue(self.ctrSS.primi()[1][1]==9)
        
        self.assertRaises(ValidatorException,self.ctrD.adaugaDisciplina,2, "","")
        self.assertRaises(ValidatorException,self.ctrD.adaugaDisciplina,-2, "ana","mn")
        
    def testWhiteBox203(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrS.adaugaStudent(4, "maria")
        self.ctrS.adaugaStudent(5, "andrei")
        self.ctrS.adaugaStudent(6, "ionela")
        self.ctrS.adaugaStudent(7, "anastasia")
        self.ctrS.adaugaStudent(8, "dorel")
        self.ctrS.adaugaStudent(9, "miruna")
        self.ctrS.adaugaStudent(10, "stefan")
        
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrD.adaugaDisciplina(2, "info","ionescu")
        self.ctrD.adaugaDisciplina(3, "mate","ion")
        self.ctrD.adaugaDisciplina(4, "logica","predescu")
        
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(1,1 ,10)
        self.ctrN.adaugaNota(3,2 ,9)
        self.ctrN.adaugaNota(1,4 ,3)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(4,1 ,7)
        self.ctrN.adaugaNota(5,1 ,4)
        self.ctrN.adaugaNota(6,1 ,10)
        self.ctrN.adaugaNota(7,2 ,9)
        self.ctrN.adaugaNota(8,4 ,3)
        self.ctrN.adaugaNota(9,1 ,6)
        self.ctrN.adaugaNota(10,1 ,7)
        self.assertRaises(ValidatorException,self.ctrN.adaugaNota,2,-2,0)
        self.assertRaises(ValidatorException,self.ctrN.adaugaNota,-2, 1,0)
        
    def testWhiteBox204(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrS.adaugaStudent(4, "maria")
        self.ctrS.adaugaStudent(5, "andrei")
        self.ctrS.adaugaStudent(6, "ionela")
        self.ctrS.adaugaStudent(7, "anastasia")
        self.ctrS.adaugaStudent(8, "dorel")
        self.ctrS.adaugaStudent(9, "miruna")
        self.ctrS.adaugaStudent(10, "stefan")
        
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrD.adaugaDisciplina(2, "info","ionescu")
        self.ctrD.adaugaDisciplina(3, "mate","ion")
        self.ctrD.adaugaDisciplina(4, "logica","predescu")
        
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(1,1 ,10)
        self.ctrN.adaugaNota(3,2 ,9)
        self.ctrN.adaugaNota(1,4 ,3)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(4,1 ,7)
        self.ctrN.adaugaNota(5,1 ,4)
        self.ctrN.adaugaNota(6,1 ,10)
        self.ctrN.adaugaNota(7,2 ,9)
        self.ctrN.adaugaNota(8,4 ,3)
        self.ctrN.adaugaNota(9,1 ,6)
        self.ctrN.adaugaNota(10,1 ,7)
        self.assertRaises(ValidatorException,self.ctrN.adaugaNota,2, 1,-3)
        self.assertRaises(ValidatorException,self.ctrS.adaugaStudent,2, "")
        
    def testWhiteBox205(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrS.adaugaStudent(4, "maria")
        self.ctrS.adaugaStudent(5, "andrei")
        self.ctrS.adaugaStudent(6, "ionela")
        self.ctrS.adaugaStudent(7, "anastasia")
        self.ctrS.adaugaStudent(8, "dorel")
        self.ctrS.adaugaStudent(9, "miruna")
        self.ctrS.adaugaStudent(10, "stefan")
        
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrD.adaugaDisciplina(2, "info","ionescu")
        self.ctrD.adaugaDisciplina(3, "mate","ion")
        self.ctrD.adaugaDisciplina(4, "logica","predescu")
        
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(1,1 ,10)
        self.ctrN.adaugaNota(3,2 ,9)
        self.ctrN.adaugaNota(1,4 ,3)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(4,1 ,7)
        self.ctrN.adaugaNota(5,1 ,4)
        self.ctrN.adaugaNota(6,1 ,10)
        self.ctrN.adaugaNota(7,2 ,9)
        self.ctrN.adaugaNota(8,4 ,3)
        self.ctrN.adaugaNota(9,1 ,6)
        self.ctrN.adaugaNota(10,1 ,7)
        self.assertRaises(ValidatorException,self.ctrS.adaugaStudent,-2, "ana")
        
        
    def testBlackBoxOrdAlf(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[0].getIdstud()==3)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[0].getIddis()==1)
        
    def testBlackBoxOrdAlf2(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[0].getNote()==[7])
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[1].getIdstud()==2)
        
    def testBlackBoxOrdAlf3(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[1].getIddis()==1)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[1].getNote()==[6])
        
    def testBlackBoxOrdAlf4(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[2].getIdstud()==1)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[2].getIddis()==1)
        
    def testBlackBoxOrdAlf5(self):
        self.ctrS.adaugaStudent(1, "ion")
        self.ctrS.adaugaStudent(2, "ana")
        self.ctrS.adaugaStudent(3, "alin")
        self.ctrD.adaugaDisciplina(1, "mate","popescu")
        self.ctrN.adaugaNota(1,1 ,4)
        self.ctrN.adaugaNota(2,1 ,6)
        self.ctrN.adaugaNota(3,1 ,7)
        self.assertTrue(self.ctrSS.ordonareAlfabetic("mate")[2].getNote()==[4])
        