'''
Created on Jan 22, 2018

@author: PATI
'''
from repo.repoJ import RepoJ
from service.serviceJ import ServiceJ
from ui.console import Console
from teste.testJ import TestJ
from teste.testRepoF import TestRepoF
from teste.testRepoJ import TestRepoJ
from teste.testServiceF import TestServiceF
from teste.testServiceJ import TestServiceJ

test=TestJ()
test.run()
test=TestRepoF()
test.run()
test=TestRepoJ()
test.run()
test=TestServiceF()
test.run()
test=TestServiceJ()
test.run()

repo=RepoJ("jucatori.txt")
service=ServiceJ(repo)
console=Console(service)
console.run()