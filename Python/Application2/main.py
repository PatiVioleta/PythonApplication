'''
Created on Nov 12, 2017

@author: PATI
'''
from repository.repositoryStudent import inMemoryRepository
from repository.repositoryMaterie import inMemoryRepositoryD
from repository.repositoryNota import inMemoryRepositoryN
from repository.repositoryMaterie2 import disciplinaFileRepository
from repository.repositoryNota2 import notaFileRepository
from repository.repositoryStudent2 import studentFileRepository

from service.studentController import StudentController
from service.materieController import DisciplinaController
from service.notaController import NotaController
from service.statisticiController import StatisticiController
from teste.testeStudent import testeStudent
from teste.testeMaterie import testeDisciplina
from teste.testeNota import testeNota
from teste.testeStatistici import testeStatistici
from ui.console import Console

testS=testeStudent()
testS.run()

testD=testeDisciplina()
testD.run()

testN=testeNota()
testN.run()

testSS=testeStatistici()
testSS.run()

#repo = inMemoryRepository()                   #repo un obiect de tipul inMemoryRepository (lista de studenti)
repo=studentFileRepository()

#repoD= inMemoryRepositoryD()                  #repoD un obiect de tipul inMemoryRepositoryD (lista de discipline)
repoD=disciplinaFileRepository()

#repoN= inMemoryRepositoryN()                  #repoN un obiect de tipul inMemoryRepositoryN (lista de note)
repoN=notaFileRepository()

cond=2
ctrl = StudentController(repo)                #ctrl un obiect de tipul StudentController
ctrlD= DisciplinaController(repoD)            #ctrlD un obiect de tipul DisciplinaController
ctrlN= NotaController(repoN)                  #ctrlN un obiect de tipul NotaController
ctrlS= StatisticiController(repo,repoD,repoN,ctrl,ctrlD,ctrlN) #ctrlS un obiect de tipul StatisticiController

console = Console(ctrl,ctrlD,ctrlN,ctrlS)     #console= obiectul de tip Console

console.run(cond)                                 #rulam consola
